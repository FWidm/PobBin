from sqlalchemy.orm import Session

from pobbin.api.models.paste import Paste


class PasteRepository:
    @staticmethod
    def create(db: Session, paste: Paste):
        db.add(paste)
        db.commit()

    @staticmethod
    def find_by_hash(db: Session, md5: str) -> Paste:
        return db.query(Paste).filter(Paste.md5 == md5).one_or_none()

    @staticmethod
    def find_by_key(db: Session, key: str) -> Paste:
        return db.query(Paste).filter(Paste.key == key).one_or_none()
