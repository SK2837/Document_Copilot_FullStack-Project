from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Profile(Base):
    """One row per Supabase auth user — id mirrors auth.users.id."""

    __tablename__ = "profiles"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
