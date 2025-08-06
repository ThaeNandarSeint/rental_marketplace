from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6076d0b14bb8'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True,index=True),
        sa.Column('name', sa.String(50), nullable=False, index=True),
        sa.Column('email', sa.String(100), nullable=False, unique=True, index=True),
        sa.Column('password', nullable=False),
        sa.Column('phone_number', sa.String(100), nullable=False, index=True),
        sa.Column('type', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now()),
    )

def downgrade():
    op.drop_table('users')
