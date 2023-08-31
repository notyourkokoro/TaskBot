"""not fkeys

Revision ID: c36e75bfa24a
Revises: 3ea408b1e111
Create Date: 2023-08-19 18:55:22.735318

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c36e75bfa24a'
down_revision: Union[str, None] = '3ea408b1e111'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('projects_creator_id_fkey', 'projects', type_='foreignkey')
    op.drop_column('projects', 'creator_id')
    op.drop_constraint('tasks_creator_id_fkey', 'tasks', type_='foreignkey')
    op.drop_column('tasks', 'creator_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('creator_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('tasks_creator_id_fkey', 'tasks', 'users', ['creator_id'], ['id'])
    op.add_column('projects', sa.Column('creator_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('projects_creator_id_fkey', 'projects', 'users', ['creator_id'], ['id'])
    # ### end Alembic commands ###
