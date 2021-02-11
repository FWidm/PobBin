import contextlib

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from pobbin.api.db.database import Base, get_db
from server import app

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


def truncate_db():
    meta = MetaData()

    with contextlib.closing(engine.connect()) as con:
        trans = con.begin()
        for table in reversed(meta.sorted_tables):
            con.execute(table.delete())
        trans.commit()


def get_test_client():
    app.dependency_overrides[get_db] = override_get_db
    # create tables
    Base.metadata.create_all(bind=engine)

    return TestClient(app)
