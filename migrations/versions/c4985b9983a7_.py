"""empty message

Revision ID: c4985b9983a7
Revises: 5e89425576e3
Create Date: 2022-06-12 21:14:05.112257

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4985b9983a7'
down_revision = '5e89425576e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Show', 'artist_name')
    op.drop_column('Show', 'venue_name')
    op.drop_column('Show', 'artist_image_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('artist_image_link', sa.VARCHAR(length=300), autoincrement=False, nullable=True))
    op.add_column('Show', sa.Column('venue_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.add_column('Show', sa.Column('artist_name', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
