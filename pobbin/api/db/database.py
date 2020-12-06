from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from os import environ as envget

DB_HOST = envget['DB_HOST']
DB_PORT = envget['DB_PORT']
DB_NAME = envget['DB_NAME']
DB_USER = envget['DB_USER']
DB_PWD = envget['DB_PASSWORD']
DB_CONNECTION = envget['DB_CONNECTION']

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


