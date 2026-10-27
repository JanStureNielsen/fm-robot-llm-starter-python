"""Converting the integer amounts the API sends to and from decimal text.

Every price, unit and cash amount on Flexemarkets is an integer counting the
smallest step. A market's ``price_decimals`` (and a marketplace's
``cash_decimals``) says where the decimal point goes: with 2 decimals, ``405``
is 4.05. This is the one place that knows that; nothing else in the robot
should multiply or divide by a power of ten.

The SDK does not carry the decimal fields yet, so callers pass
``PRICE_DECIMALS`` for now. Conversion is exact (``Decimal``), never ``float``.
"""

from decimal import Decimal

PRICE_DECIMALS = 2
"""Where the decimal point goes in a price, until the market says (fm-robots#495)."""

CASH_DECIMALS = 2
"""Where the decimal point goes in cash, until the marketplace says."""

UNIT_DECIMALS = 0
"""Where the decimal point goes in units, until the market says."""


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
