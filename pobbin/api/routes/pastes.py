from fastapi import APIRouter, Request, Response, Depends
from sqlalchemy.orm import Session

from pobbin.api.controllers import build_controller
from pobbin.api.db.database import get_db
from pobbin.api.schemas.paste import PostPastebinView, GetPastebinView

router = APIRouter()


@router.get("/pastes/{key}", tags=["pastes"], response_model=GetPastebinView,
            description="Obtain a Build from PobBin including metadata")
async def get_paste(key: str, db: Session = Depends(get_db)):
    return build_controller.get_paste(db, key)


@router.get("/pastes/{key}/raw", tags=["pastes"], response_model=str,
            description="Obtain a raw XML Build from PobBin")
async def get_paste_raw(key: str, db: Session = Depends(get_db)):
    return Response(content=build_controller.get_raw_xml(db, key), media_type="application/xml")


@router.post("/pastes", tags=["pastes"], response_model=PostPastebinView,
             description="Post a raw XML Build to PobBin")
async def import_paste(request: Request, db: Session = Depends(get_db)):
    content_type = request.headers.get('content-type')
    if content_type != "application/xml":
        return Response("Invalid content type", 400)

    build_xml = await request.body()

    return build_controller.create_paste(db, build_xml.decode("utf-8"))
