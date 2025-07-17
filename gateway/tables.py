from sqlalchemy import (
    JSON,
    TIMESTAMP,
    UUID,
    Column,
    Enum,
    ForeignKey,
    Index,
    String,
    Table,
    UniqueConstraint,
)

from gateway.database import metadata


status = Enum("pending", "completed", "rejected", "refunded", "errored", name="status")

payments = Table(
    "payments",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("provider_id", String, nullable=True),
    Column("provider", String, nullable=False),
    Column("method", String, nullable=False),
    Column("amount", JSON, nullable=False),
    Column("net_amount", JSON, nullable=False),
    Column("status", status, nullable=False),
    Column("customer", JSON, nullable=False, default={}),
    Column("description", String, nullable=False),
    Column("commissions", JSON, nullable=False, default=[]),
    Column("meta", JSON, nullable=False, default={}),
    Column("created_at", TIMESTAMP, nullable=False, server_default="now()"),
    Column(
        "updated_at",
        TIMESTAMP,
        nullable=False,
        server_default="now()",
        onupdate="now()",
    ),
    # Constraints for unique payment.
    UniqueConstraint("id", "provider_id", "provider", name="unique_payment"),
)

notifications = Table(
    "notifications",
    metadata,
    Column("id", UUID, primary_key=True),
    Column(
        "payment_id",
        UUID,
        ForeignKey("payments.id", ondelete="RESTRICT"),
        nullable=False,
    ),
    Column("notification", JSON, nullable=False),
    Column("created_at", TIMESTAMP, nullable=False, server_default="now()"),
    Column("received_at", TIMESTAMP, nullable=False, server_default="now()"),
)


__all__ = [
    "payments",
    "notifications",
]
