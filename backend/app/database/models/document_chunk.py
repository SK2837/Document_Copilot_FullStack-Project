from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any

from pgvector.sqlalchemy import Vector
from sqlalchemy import Computed, ForeignKey, Integer, Text, func, text
from sqlalchemy.dialects.postgresql import JSONB, TSVECTOR, UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class DocumentChunk(Base):
    """Retrieval-ready passage — stores text, embedding, and full-text search vector."""

    __tablename__ = "document_chunks"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    document_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("source_documents.id", ondelete="CASCADE"),
        nullable=False,
    )
    chunk_index: Mapped[int] = mapped_column(Integer, nullable=False)
    chunk_text: Mapped[str] = mapped_column(Text, nullable=False)
    token_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    page: Mapped[int | None] = mapped_column(Integer, nullable=True)
    section: Mapped[str | None] = mapped_column(Text, nullable=True)
    # Populated by the ingestion pipeline via OpenAI embeddings
    embedding: Mapped[Any] = mapped_column(Vector(1536), nullable=True)
    # Generated column — populated automatically by Postgres from chunk_text
    search_vector: Mapped[Any] = mapped_column(
        TSVECTOR,
        Computed("to_tsvector('english', chunk_text)", persisted=True),
        nullable=True,
    )
    # ticker, company, filing_type, filing_date, year, accession_number, page, section
    chunk_metadata: Mapped[dict] = mapped_column(
        JSONB, nullable=False, server_default=text("'{}'::jsonb")
    )
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
