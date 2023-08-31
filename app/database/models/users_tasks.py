from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from .base import Base


class UserTask(Base):
    __tablename__ = 'users_tasks'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    task_id: Mapped[int] = mapped_column(ForeignKey('tasks.id', ondelete='CASCADE'))