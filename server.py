import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from pobbin.api.db.database import engine, Base
from pobbin.api.routes import pastes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(pastes.router)


def custom_openapi():
    """
    This method creates a custom override of the OpenAPI scheme
    to fix certain stuff that's not possible in FastAPI right now
    """
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="pob.codes API",
        version="1.0.0",
        routes=app.routes,
    )
    # @TODO: this is very ugly, but it works. It should really be easier to make this work -_-
    # right now this just replaces the /pastes "post" endpoint documentation and we pretend
    # it accepts xml
    openapi_schema["paths"]["/pastes"]["post"]["requestBody"] = {
        "content": {
            "application/xml": {
                "schema": {
                    "title": "Paste",
                    "type": "string"
                }
            }
        },
        "required": True
    }

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


def run():
    uvicorn.run(app, port=8888)


if __name__ == '__main__':
    run()
