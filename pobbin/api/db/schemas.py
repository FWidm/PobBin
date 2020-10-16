from typing import List, Optional

from pydantic import BaseModel


class PasteBase(BaseModel):
    key: str


class Paste(PasteBase):
    password: str


class Paste(PasteBase):
    key: str
    created: str


    class Config:
        orm_mode = True