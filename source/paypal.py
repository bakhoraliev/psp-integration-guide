from decimal import Decimal
from typing import Any, TypedDict


class Amount(TypedDict):
    """Amount of the payment."""

    value: Decimal
    currency: str


class Payment(TypedDict):
    """
    Payment information.

    The payment must provide the provider, method, amount, customer, items, meta, and notifications.
    """

    provider: str
    method: str
    amount: Amount
    customer: dict[str, Any]
    description: str
    meta: dict[str, Any]
    notifications: list[dict[str, Any]]
