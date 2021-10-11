from memsource.schemas.base import BaseSchema
from memsource.schemas.user import User


class NetRateScheme(BaseSchema):
    id: str
    uid: str
    name: str
    dateCreated: str
    createdBy: User