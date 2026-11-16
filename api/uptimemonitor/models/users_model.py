from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, String, UniqueConstraint, ForeignKey, func
from uptimemonitor.models.base import Base
from datetime import datetime



class User(Base):
    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(),)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    email_verified_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("role.role_id"), nullable=False)

    role: Mapped["Role"] = relationship(back_populates="users")

    
    __table_args__ = (
       UniqueConstraint("username", name="uq_user_username"),
       UniqueConstraint("email", name="uq_user_email"),
    )