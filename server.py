import uvicorn
from fastapi import FastAPI

from pobbin.api.db.database import engine, Base
from pobbin.api.routes import pastes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(pastes.router)

def run():
    uvicorn.run(app, port=8888)

if __name__ == '__main__':
    run()