"""add about_me and last_seen to Users.

Revision ID: 532b01cce540
Revises: 58c9b330691e
Create Date: 2017-12-26 11:16:33.216435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '532b01cce540'
down_revision = '58c9b330691e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
