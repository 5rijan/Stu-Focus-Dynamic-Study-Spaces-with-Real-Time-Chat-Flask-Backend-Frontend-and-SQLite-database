"""empty message

Revision ID: 82174c0c5f5d
Revises: 
Create Date: 2023-12-23 00:33:03.428523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82174c0c5f5d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('room', schema=None) as batch_op:
        batch_op.add_column(sa.Column('passcode', sa.String(length=5), nullable=False))
        batch_op.add_column(sa.Column('user_count', sa.Integer(), nullable=True))
        batch_op.create_unique_constraint('uix_1', ['passcode'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('room', schema=None) as batch_op:
        # batch_op.drop_constraint('uix_1', type_='unique')
        #batch_op.drop_column('user_count')
        batch_op.drop_column('passcode')
    # ### end Alembic commands ###

    # ### end Alembic commands ###
