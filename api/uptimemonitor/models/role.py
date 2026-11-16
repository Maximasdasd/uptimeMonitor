from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, UniqueConstraint
from uptimemonitor.models.base import Base
from typing import List



class Role(Base):
    __tablename__ = "role"
    role_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))

    users: Mapped[List["User"]] = relationship(back_populates="role")


    __table_args__ = (
       UniqueConstraint("name", name="uq_role_name"),
       )