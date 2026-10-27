import pytest

from prices import PRICE_DECIMALS, format_amount, from_decimal, to_decimal


def test_cents_format_as_before():
    for value in (0, 1, 5, 99, 100, 405, 12345, -1, -405, 10**12 + 7):
        assert format_amount(value, PRICE_DECIMALS, 5) == f"${value / 100:5.2f}"
        assert format_amount(value, PRICE_DECIMALS) == f"${value / 100:.2f}"


def test_other_scales():
    assert format_amount(405, 0) == "$405"
    assert format_amount(405, 3) == "$0.405"
    assert str(to_decimal(29, 2)) == "0.29"


def test_parse_is_exact():
    assert from_decimal("0.29", 2) == 29
    assert from_decimal("4.05", 2) == 405
    assert from_decimal("4", 2) == 400
    assert from_decimal("-1.5", 2) == -150
    assert from_decimal("0.123", 3) == 123


@pytest.mark.parametrize("text", ["0.295", "abc", "", "nan", "inf"])
def test_parse_refuses(text):
    with pytest.raises(ValueError):
        from_decimal(text, 2)
