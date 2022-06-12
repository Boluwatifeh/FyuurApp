"""empty message

Revision ID: dd21615d328f
Revises: 605d5c71a0b1
Create Date: 2022-06-12 22:50:42.390148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd21615d328f'
down_revision = '605d5c71a0b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Area',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('state', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('genres', sa.String(length=120), nullable=True),
    sa.Column('image_link', sa.String(length=300), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('website_link', sa.String(length=120), nullable=True),
    sa.Column('seeking_venue', sa.String(), nullable=True),
    sa.Column('seeking_description', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Venue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('genres', sa.String(length=120), nullable=True),
    sa.Column('image_link', sa.String(length=300), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('website_link', sa.String(length=120), nullable=True),
    sa.Column('seeking_talent', sa.Boolean(), nullable=True),
    sa.Column('seeking_description', sa.String(), nullable=True),
    sa.Column('area', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['area'], ['Area.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Show')
    op.drop_table('Venue')
    op.drop_table('Artist')
    op.drop_table('Area')
    # ### end Alembic commands ###