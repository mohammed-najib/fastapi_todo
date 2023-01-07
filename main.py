from fastapi import FastAPI
import models
from database import engine
from routers import todos as todosSite, auth as authSite, users as usersSite, static
from routers.apis import auth, todos, users, address
from starlette import status
from starlette.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)


# app.include_router(static.router)

app.include_router(authSite.router)
app.include_router(todosSite.router)
app.include_router(usersSite.router)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(users.router)
app.include_router(address.router)
