from os import environ

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DB_HOST = environ.get('DB_HOST', None)
DB_PORT = environ.get('DB_PORT', 0)
DB_NAME = environ.get('DB_NAME', None)
DB_USER = environ.get('DB_USER', None)
DB_PWD = environ.get('DB_PASSWORD', None)
DB_CONNECTION = environ.get('DB_CONNECTION', 'postgresql')

SQLALCHEMY_DATABASE_URL = f'{DB_CONNECTION}://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
