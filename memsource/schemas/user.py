from pydantic import BaseModel


class User(BaseModel):
    email: str
    firstName: str
    id: str
    lastName: str
    role: str
    uid: str
    userName: str