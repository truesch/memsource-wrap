from typing import Optional

from memsource.schemas.base import BaseSchema
from memsource.schemas.user import User
from memsource.schemas.price_list import PriceList
from memsource.schemas.net_rate_scheme import NetRateScheme


class Client(BaseSchema):
    createdBy: User
    displayNoteInProject: bool
    externalId: Optional[str]
    id: str
    name: str
    netRateScheme: Optional[NetRateScheme]
    note: Optional[str]
    priceList: Optional[PriceList]
    uid: Optional[str]
