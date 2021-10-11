from pydantic.types import UUID1
from memsource.schemas.base import BaseSchema


class PriceList(BaseSchema):
    id: str
    uid: str
    name: str
