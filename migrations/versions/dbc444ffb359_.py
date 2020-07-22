"""empty message

Revision ID: dbc444ffb359
Revises: 
Create Date: 2020-07-20 16:13:49.096705

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'dbc444ffb359'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Person',
    sa.Column('id_person', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('embeddings', postgresql.ARRAY(sa.Float(), dimensions=1), nullable=False),
    sa.PrimaryKeyConstraint('id_person')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Person')
    # ### end Alembic commands ###
