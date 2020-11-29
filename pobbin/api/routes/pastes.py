from fastapi import APIRouter, Request, Response, Depends
from sqlalchemy.orm import Session

from pobbin.api.controllers import build_controller
from pobbin.api.db.database import get_db
from pobbin.api.schemas.paste import PostPastebinView, GetPastebinView
from pobbin.util.pob_xml_verifier import is_valid_pob

router = APIRouter()


@router.get("/pastes/{key}", tags=["pastes"], response_model=GetPastebinView,
            description="Obtain a Build from PobBin including metadata")
async def get_paste(key: str, db: Session = Depends(get_db)) -> Response:
    return build_controller.get_paste(db, key)


@router.get("/pastes/{key}/raw", tags=["pastes"], response_model=str,
            description="Obtain a raw XML Build from PobBin")
async def get_paste_raw(key: str, db: Session = Depends(get_db)) -> Response:
    return Response(content=build_controller.get_raw_xml(db, key), media_type="application/xml")


@router.post("/pastes", tags=["pastes"], response_model=PostPastebinView,
             description="Post a raw XML Build to PobBin")
async def import_paste(request: Request, db: Session = Depends(get_db)) -> Response:
    content_type = request.headers.get('content-type')
    if content_type != "application/xml":
        return Response("Invalid content type, expected content type is 'application/xml'.", 406)

    build_xml = await request.body()
    if is_valid_pob(build_xml):
        decoded_build_xml = build_xml.decode()
        return build_controller.create_paste(db, decoded_build_xml)
    return Response("No valid build XML.", 400)
