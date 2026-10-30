"""Converting the integer amounts the API sends to and from decimal text.

Every price, unit and cash amount on Flexemarkets is an integer counting the
smallest step. A market's ``price_decimals`` (and a marketplace's
``cash_decimals``) says where the decimal point goes: with 2 decimals, ``405``
is 4.05. This is the one place that knows that; nothing else in the robot
should multiply or divide by a power of ten.

Pass the market's own ``market.price_decimals`` (and the marketplace's
``cash_decimals``); the constants below are what the server gives one that
does not set them. Conversion is exact (``Decimal``), never ``float``.
"""

from decimal import Decimal

PRICE_DECIMALS = 2
"""A price's decimal places when the market does not set them."""

CASH_DECIMALS = 2
"""Cash's decimal places when the marketplace does not set them."""

UNIT_DECIMALS = 0
"""A unit count's decimal places when the market does not set them."""


def to_decimal(value: int, decimals: int) -> Decimal:
    """The exact decimal *value* counts, at *decimals* decimal places."""
    return Decimal(value).scaleb(-decimals)


def from_decimal(text: str | Decimal, decimals: int) -> int:
    """The integer count for decimal *text*, at *decimals* decimal places.

    Raises ``ValueError`` if *text* is not a number or has more decimal
    places than *decimals* allows; it never rounds.
    """
    try:
        value = Decimal(text)
    except ArithmeticError as e:
        raise ValueError(f"not a number: {text!r}") from e
    if not value.is_finite():
        raise ValueError(f"not a number: {text!r}")
    scaled = value.scaleb(decimals)
    if scaled != scaled.to_integral_value():
        raise ValueError(f"{text} has more than {decimals} decimal places")
    return int(scaled)


def format_amount(value: int, decimals: int, width: int = 0) -> str:
    """*value* as ``$`` and its decimal, right-aligned in *width* characters."""
    return f"${to_decimal(value, decimals):{width}.{decimals}f}"
