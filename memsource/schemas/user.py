from memsource.schemas.base import BaseSchema


class User(BaseSchema):
    email: str
    firstName: str
    id: str
    lastName: str
    role: str
    uid: str
    userName: str
