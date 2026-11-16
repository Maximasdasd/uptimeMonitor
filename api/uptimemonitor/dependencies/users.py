from uptimemonitor.repositories.users import UserRepository
from uptimemonitor.db.database import get_async_session
from uptimemonitor.core.security import SecurityService
from pwdlib import PasswordHash
from uptimemonitor.services.users import UsersService
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from fastapi import Depends


def get_user_repository(
        session: Annotated[AsyncSession, Depends(get_async_session)]
        ) -> UserRepository:
    return UserRepository(session)


def get_security_service() -> SecurityService:
    return SecurityService(
        password_hasher=PasswordHash.recommended(),
    )

def get_user_service(user_repository: Annotated[UserRepository, Depends(get_user_repository)], 
        security: Annotated[SecurityService, Depends(get_security_service)]
        ) -> UsersService:
    return UsersService(user_repository, security)