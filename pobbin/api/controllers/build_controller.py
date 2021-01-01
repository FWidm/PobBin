import hashlib

from sqlalchemy.orm import Session

from pobbin.api.db.paste_repository import PasteRepository
from pobbin.api.models.paste import Paste
from pobbin.util.hashids import hashes

paste_repository = PasteRepository()


def create_paste(db: Session, raw_xml: str) -> Paste:
    if "<PathOfBuilding>" in raw_xml and "<Build" in raw_xml:
        build_hash = hash_content(raw_xml)
        paste = paste_repository.find_by_hash(db, build_hash)
        if not paste:
            paste = Paste(raw_xml=raw_xml, build_hash=build_hash)
            paste_repository.create(db, paste)

        return _add_hashed_key(paste)


def hash_content(raw_xml: str) -> str:
    hash = hashlib.sha3_256(raw_xml.encode("utf-8")).hexdigest()
    return f"sha3_256:{hash}"


def get_paste(db: Session, key: str) -> Paste:
    pk = hashes.decode(key)
    paste = paste_repository.find_by_pk(db, pk)
    return _add_hashed_key(paste)


def get_raw_xml(db, key) -> str:
    return get_paste(db, key).raw_xml


def _add_hashed_key(paste: Paste) -> Paste:
    """
    Adds the hashed PK as key attribute to a paste
    :param paste: to generate hashkey for
    :return: paste with generated key attribute
    """
    paste.key = hashes.encode(paste.pk)
    return paste
