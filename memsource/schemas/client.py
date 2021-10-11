from typing import Optional
from pydantic import BaseModel

from memsource.schemas.user import User


class Client(BaseModel):
    createdBy: User
    displayNoteInProject: bool
    externalId: Optional[str]
    id: str
    name: str
    netRateScheme: Optional[str]
    note: Optional[str]
    priceList: Optional[str]
    uid: Optional[str]
