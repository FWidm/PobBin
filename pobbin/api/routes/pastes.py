import logging
from fastapi import APIRouter, Request, Response, Depends
from sqlalchemy.orm import Session

from pobbin.api.controllers import build_controller
from pobbin.api.db.database import get_db

router = APIRouter()
logger = logging.getLogger("api")


@router.get(f"/pastes", tags=["pastes"])
async def read_pastes():
    return [{"username": "Foo"}, {"username": "Bar"}]


@router.get("/pastes/{key}", tags=["pastes"])
async def get_paste(key: str, db: Session = Depends(get_db)):
    return build_controller.get_paste(db, key)


@router.post("/pastes", tags=["pastes"])
async def import_paste(request: Request, db: Session = Depends(get_db)):
    content_type = request.headers.get('content-type')
    if content_type != "application/xml":
        return Response("Invalid content type", 400)

    build_xml = await request.body()

    return build_controller.create_paste(db, build_xml.decode("utf-8"))
