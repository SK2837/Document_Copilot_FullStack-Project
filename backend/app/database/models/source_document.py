from __future__ import annotations

import uuid
from datetime import date, datetime

from sqlalchemy import Date, String, Text, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class SourceDocument(Base):
    """One row per SEC filing — stores filing metadata and normalized Markdown."""

    __tablename__ = "source_documents"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    ticker: Mapped[str] = mapped_column(String(10), nullable=False)
    company_name: Mapped[str] = mapped_column(String(255), nullable=False)
    filing_type: Mapped[str] = mapped_column(String(20), nullable=False)
    filing_date: Mapped[date] = mapped_column(Date, nullable=False)
    report_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    accession_number: Mapped[str] = mapped_column(String(25), nullable=False)
    source_url: Mapped[str] = mapped_column(Text, nullable=False)
    content_markdown: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    __table_args__ = (
        UniqueConstraint("accession_number", name="uq_source_documents_accession"),
    )
