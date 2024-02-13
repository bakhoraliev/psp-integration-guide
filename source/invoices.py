from decimal import Decimal
from typing import Any, TypedDict


class Customer(TypedDict):
    """
    Customer of the invoice.

    The customer must provide an email address and ip, but in some cases,
        may also provide another information such as name, address, etc.
    """

    ip: str
    email: str


class Money(TypedDict):
    """Amount and currency of the invoice."""

    amount: Decimal
    currency: str


class Invoice(TypedDict):
    """Invoice to be paid."""

    provider: str
    method: str
    amount: Money
    customer: Customer
    items: list[str]
    meta: dict[str, Any]
    notifications: list[dict[str, Any]]


def create_redirect_link(invoice: Invoice) -> str:
    """Create a redirect link to the payment provider based on the invoice."""
