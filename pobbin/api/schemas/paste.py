from datetime import datetime

from pobbin.api.schemas import BaseORMModel


class PostPastebinView(BaseORMModel):
    key: str
    created: datetime


class GetPastebinView(BaseORMModel):
    key: str
    created: datetime
    raw_xml: str

