# Todo App Example using FastAPI

An example of a FastAPI Server

## Things learned

1. How to create sqlite database and how to connect to it
2. How to connect to postgresql
3. Routing to organize code into files
4. How to use alembic

## Environment Variables

```sh
SECRET_KEY
SQLALCHEMY_DB_URL
```

## Installed packages

```sh
pip install fastapi
pip install sqlalchemy
pip install "uvicorn[standard]"
pip install "passlib[bcrypt]"
pip install "python-multipart"
pip install "python-jose[cryptography]"
pip install python-dotenv
pip install psycopg2-binary # for postgres
pip install alembic
```

## Shell commands used

```sh
alembic init alembic # to initialize alembic
alembic revision -m '' # to make a migration file with a message
alembic upgrade <revision> # to upgrade db to a specific revision alembic.versions folder
alembic downgrade -1 # to downgrade from the latest migration
```

## To generate secret key

```python
from secrets import token_hex
SECRET_KEY=token_hex(32)
```

## VS-code extensions used

Thunder Client (by Ranga Vadhineni)
