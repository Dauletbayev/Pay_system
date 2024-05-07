from fastapi import APIRouter, Request
from pydantic import BaseModel
from database.userservice import *


users_router = APIRouter(tags=['Управление пользователями'], prefix='/users')

class User(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str
    password: str
    country: str


# @users_router.post('/api/register')
# async def register_user(user_model: User):
#     new_user