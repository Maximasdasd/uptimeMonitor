from uptimemonitor.repositories.users import UserRepository
from uptimemonitor.schemas.users_schemas import UserCreate, UserResponse
from uptimemonitor.db.database import get_async_session
from uptimemonitor.core.security import SecurityService
from uptimemonitor.core.config import settings
from starlette.concurrency import run_in_threadpool
from pwdlib import PasswordHash
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from fastapi import Depends, HTTPException

class UsersService:
    def __init__(self, user_repository: UserRepository, security: SecurityService):
        self.user_repository = user_repository
        self.security = security

    async def register(self, user_data: UserCreate) -> UserResponse:
        check_username = await self.user_repository.get_by_username(user_data.username)
        email = user_data.email.strip().lower()
        check_email = await self.user_repository.get_by_email(email)
        if check_email is not None:
            raise HTTPException(status_code=409, detail="Пользователь с такой почтой уже существует.")
        if check_username is not None:
            raise HTTPException(status_code=409, detail="Такой пользователь существует.")
        password_hash = await run_in_threadpool(self.security.hash_password, user_data.password)
        try:
            user = await self.user_repository.register(user_data.username, email, password_hash)
        except IntegrityError as exc:
            constraint_name = exc.orig.__cause__.constraint_name
            if constraint_name == "uq_user_username":
                raise HTTPException(status_code=409, detail="Такой пользователь существует.")
            if constraint_name == "uq_user_email":
                raise HTTPException(status_code=409, detail="Пользователь с такой почтой уже существует.")
            raise
        return UserResponse.model_validate(user)