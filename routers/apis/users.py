import sys

sys.path.append("..")

from fastapi import Depends, APIRouter, status
from database import get_db
import models
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .auth import (
    get_current_user,
    get_user_exception,
    verify_password,
    get_password_hash,
)


class UserVerification(BaseModel):
    username: str
    password: str
    new_password: str


router = APIRouter(
    prefix="/api/users",
    tags=["users"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Not found",
        },
    },
)


@router.get("/")
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Users).all()


@router.get("/{user_id}")
async def user_by_path(user_id: int, db: Session = Depends(get_db)):
    user_model = db.query(models.Users).filter(models.Users.id == user_id).first()

    if user_model is not None:
        return user_model

    return "Invalid user_id"


@router.get("/user/")
async def user_by_query(user_id: int, db: Session = Depends(get_db)):
    user_model = db.query(models.Users).filter(models.Users.id == user_id).first()

    if user_model is not None:
        return user_model

    return "Invalid user_id"


@router.put("/password")
async def user_password_change(
    user_verification: UserVerification,
    user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if user is None:
        raise get_user_exception()

    user_model = (
        db.query(models.Users).filter(models.Users.id == user.get("id")).first()
    )

    if user_model is not None:
        if user_verification.username == user_model.username and verify_password(
            user_verification.password, user_model.hashed_password
        ):
            user_model.hashed_password = get_password_hash(
                user_verification.new_password
            )
            db.add(user_model)
            db.commit()

            return "successful"

    return "Invalid user or request"


@router.delete("/")
async def delete_user(
    user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if user is None:
        raise get_user_exception()

    user_model = (
        db.query(models.Users).filter(models.Users.id == user.get("id")).first()
    )

    if user_model is None:
        return "Invalid user or request"

    db.query(models.Users).filter(models.Users.id == user.get("id")).delete()
    db.commit()

    return "Delete is Successful"
