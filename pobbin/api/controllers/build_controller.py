import hashlib

from sqlalchemy.orm import Session

from pobbin.api.db.paste_repository import PasteRepository
from pobbin.api.models.paste import Paste
from pobbin.util import generate_url_key

paste_repository = PasteRepository()


def create_paste(db: Session, raw_xml: str) -> Paste:
    if "<PathOfBuilding>" in raw_xml and "<Build" in raw_xml:
        md5 = hash_content(raw_xml)
        paste = paste_repository.find_by_hash(db, md5)
        if not paste:
            key = generate_url_key.build()
            paste = Paste(key=key, raw_xml=raw_xml, md5=md5)
            paste_repository.create(db, paste)
        return paste


def hash_content(raw_xml: str) -> str:
    return hashlib.md5(raw_xml.encode("utf-8")).hexdigest()


def get_paste(db: Session, key: str) -> Paste:
    return paste_repository.find_by_key(db, key)


def get_raw_xml(db, key) -> str:
    return get_paste(db, key).raw_xml
