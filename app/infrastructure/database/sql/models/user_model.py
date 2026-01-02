# infrastructure/database/sql/models/user_model.py
import uuid
from sqlalchemy import (
    Text, Boolean, DateTime, func
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.uuid_generate_v4()
    )

    email: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(Text, nullable=False)

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="true"
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    last_login_at: Mapped[DateTime | None] = mapped_column(
        DateTime(timezone=True)
    )

    roles = relationship(
        "RoleModel",
        secondary="user_roles",
        back_populates="users"
    )

    conversations = relationship(
        "ConversationModel",
        back_populates="user"
    )
