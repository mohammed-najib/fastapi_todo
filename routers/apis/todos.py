import sys

sys.path.append("..")

from typing import Optional
from fastapi import Depends, HTTPException, status, APIRouter
import models
from database import get_db
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from routers.apis.auth import get_current_user, get_user_exception
from .auth import get_current_user, get_user_exception

router = APIRouter(
    prefix="/api/todos",
    tags=["todos"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Not found",
        },
    },
)


class Todo(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(gt=0, lt=6, description="The priority must be between 1-5")
    complete: bool


@router.get("/")
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()


@router.get("/user")
async def read_all_by_user(
    user: dict = Depends(get_current_user), db: Session = Depends(get_db)
):
    if user is None:
        raise get_user_exception()

    return db.query(models.Todos).filter(models.Todos.owner_id == user.get("id")).all()


@router.get("/{todo_id}")
async def read_todo(
    todo_id: int, user: dict = Depends(get_current_user), db: Session = Depends(get_db)
):
    if user is None:
        raise get_user_exception()

    todo_model = (
        db.query(models.Todos)
        .filter(models.Todos.id == todo_id)
        .filter(models.Todos.owner_id == user.get("id"))
        .first()
    )

    if todo_model is not None:
        return todo_model

    raise http_exception()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_todo(
    todo: Todo, user: dict = Depends(get_current_user), db: Session = Depends(get_db)
):
    if user is None:
        raise get_current_user()

    todo_model = models.Todos()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete
    todo_model.owner_id = user.get("id")

    db.add(todo_model)
    db.commit()

    successful_response(status_code=status.HTTP_201_CREATED)


@router.put("/{todo_id}")
async def update_todo(
    todo_id: int,
    todo: Todo,
    user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if user is None:
        raise get_user_exception()

    todo_model = (
        db.query(models.Todos)
        .filter(models.Todos.id == todo_id)
        .filter(models.Todos.owner_id == user.get("id"))
        .first()
    )

    if todo_model is None:
        raise http_exception()

    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete

    db.add(todo_model)
    db.commit()

    return successful_response(status_code=status.HTTP_200_OK)


@router.delete("/{todo_id}")
async def delete_todo(
    todo_id: int, user: dict = Depends(get_current_user), db: Session = Depends(get_db)
):
    if user is None:
        raise get_user_exception()

    todo_model = (
        db.query(models.Todos)
        .filter(models.Todos.id == todo_id)
        .filter(models.Todos.owner_id == user.get("id"))
        .first()
    )

    if todo_model is None:
        raise http_exception()

    db.query(models.Todos).filter(models.Todos.id == todo_id).delete()
    db.commit()

    return successful_response(status_code=status.HTTP_200_OK)


def successful_response(status_code: int):
    return {
        "status": status_code,
        "transaction": "Successful",
    }


def http_exception():
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
