import logging

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from pobbin.api.models.paste import Paste


class PasteRepository:
    @staticmethod
    def create(db: Session, paste: Paste):
        db.add(paste)
        try:
            db.commit()
        except IntegrityError:
            logging.getLogger().error(f"Likely collision detected for paste with key: {paste.key}")
            db.rollback()
            return False

        return True

    @staticmethod
    def find_by_hash(db: Session, build_hash: str) -> Paste:
        return db.query(Paste).filter(Paste.build_hash == build_hash).one_or_none()

    @staticmethod
    def find_by_key(db: Session, key: str) -> Paste:
        return db.query(Paste).filter(Paste.key == key).one_or_none()
