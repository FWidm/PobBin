from sqlalchemy import Column, Integer, String, Text, func, DateTime

from pobbin.api.db.database import Base


class Paste(Base):
    __tablename__ = 'pastes'

    pk = Column(Integer, primary_key=True, index=True)
    key = Column(String(255), nullable=False, unique=True)
    raw_xml = Column(Text, nullable=False, unique=False)
    build_hash = Column(Text, nullable=False, unique=False)
    created = Column(DateTime(timezone=True), server_default=func.now())
