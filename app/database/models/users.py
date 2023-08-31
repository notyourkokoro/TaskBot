from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from .base import Base

if TYPE_CHECKING:
    from .tasks import Task


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(String(255))

    tasks_rel: Mapped[list['Task']] = relationship(secondary='users_tasks',
                                                   back_populates='users_rel',
                                                   cascade='all, delete')

    def __repr__(self):
        return f"User(tg_id={self.tg_id}, username:'{self.username}')"