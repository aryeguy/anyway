"""CreateCodeTable

Revision ID: 561cfe4c2bf
Revises: 3c0d35fdbe2e
Create Date: 2018-02-23 16:26:49.225619

"""

# revision identifiers, used by Alembic.
revision = '561cfe4c2bf'
down_revision = '3c0d35fdbe2e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('codes',
                    sa.Column('var_name', sa.String(), nullable=False),
                    sa.Column('code', sa.Integer(), nullable=False),
                    sa.Column('description', sa.String(), nullable=False),
                    sa.Column('file', sa.String(), nullable=False))


def downgrade():
    op.drop_table('codes')