from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserSchema(BaseModel):
    uid: int
    user_name: str
    user_email: EmailStr

    # user password will be a hash of the password
    user_password: str
    createdOn: datetime
    updatedOn: datetime


class CreateUserSchema(BaseModel):
    user_name: str
    user_email: EmailStr
    user_password: str


class UpdateUserSchema(BaseModel):
    user_name: str
    user_email: EmailStr
    user_password: str