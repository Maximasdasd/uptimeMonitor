from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, String, UniqueConstraint, ForeignKey, func
from datetime import datetime
from uptimemonitor.models.base import Base


class UserSession(Base):
    __tablename__ = "sessions"
    session_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    token_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    csrf_token: Mapped[str] = mapped_column(String(64), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(),)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    revoked_at: Mapped[datetime | None ] = mapped_column(DateTime(timezone=True),nullable=True)

    user: Mapped["User"] = relationship(back_populates="user_session")

    __table_args__ = (
    UniqueConstraint("token_hash", name="uq_sessions_token_hash"),
    )