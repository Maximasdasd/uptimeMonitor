from uptimemonitor.models.users_model import User
from uptimemonitor.models.role import Role
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime, timezone

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()
    
    async def get_by_username(self, username: str) -> User | None:
        stmt = select(User).where(User.username == username)
        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()


    async def register(self, username: str, email: str, password_hash: str) -> User:
        role_id = await self.session.scalar(
            select(Role.role_id).where(Role.name == "user")
        )
        if role_id is None:
            raise RuntimeError("Начальная роль user отсутствует в базе")
        created_at=datetime.now(timezone.utc)
        user = User(username=username, email=email, password_hash=password_hash, role_id=role_id, created_at=created_at)
        try:
            self.session.add(user)
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise
        return user