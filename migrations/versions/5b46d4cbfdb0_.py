"""empty message

Revision ID: 5b46d4cbfdb0
Revises: 4146a619f2f1
Create Date: 2022-06-09 22:34:50.071839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b46d4cbfdb0'
down_revision = '4146a619f2f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'Artist', ['name'])
    op.add_column('Venue', sa.Column('area', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'Venue', ['name'])
    op.create_foreign_key(None, 'Venue', 'Area', ['area'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Venue', type_='foreignkey')
    op.drop_constraint(None, 'Venue', type_='unique')
    op.drop_column('Venue', 'area')
    op.drop_constraint(None, 'Artist', type_='unique')
    # ### end Alembic commands ###
