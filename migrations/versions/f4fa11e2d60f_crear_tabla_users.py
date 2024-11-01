"""Crear tabla users

Revision ID: f4fa11e2d60f
Revises: 
Create Date: 2024-10-31 20:53:29.950808

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f4fa11e2d60f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "pacientes",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("run", sa.String(length=12), nullable=False),
        sa.Column("historia", sa.Text(), nullable=True),
        sa.Column("creado_en", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("run"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=120), nullable=False),
        sa.Column("password_hash", sa.String(length=128), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "atenciones",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("paciente_id", sa.String(), nullable=False),
        sa.Column("detalle", sa.Text(), nullable=True),
        sa.Column("creado_en", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["paciente_id"],
            ["pacientes.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("atenciones")
    op.drop_table("users")
    op.drop_table("pacientes")
    # ### end Alembic commands ###
