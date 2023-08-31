from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from .base import Base

if TYPE_CHECKING:
    from .users import User


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    creator_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    title: Mapped[str]

    users_rel: Mapped[list['User']] = relationship(secondary='users_tasks',
                                                   back_populates='tasks_rel',
                                                   passive_deletes=True)

    def __repr__(self):
        return f"Task(creator_id='{self.creator_id}', title='{self.title}')"

    def __str__(self):
        return f'"{self.title}"'