"""adds foreign key column to Cat model

Revision ID: 5a2cd0bc3e79
Revises: 06433da0e7fa
Create Date: 2024-11-05 13:12:34.915058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a2cd0bc3e79'
down_revision = '06433da0e7fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cat', schema=None) as batch_op:
        batch_op.add_column(sa.Column('caretaker_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'caretaker', ['caretaker_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cat', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('caretaker_id')

    # ### end Alembic commands ###