from types import SimpleNamespace

import ticker


class FakeDesk:
    def __init__(self, books, trades):
        self._books = books
        self._trades = trades

    def books(self):
        return self._books

    def tape(self, market_id):
        return SimpleNamespace(most_recent_prices=lambda: self._trades[market_id])


def book(market_id, symbol, decimals, bid, ask):
    market = SimpleNamespace(id=market_id, symbol=symbol, price_decimals=decimals)
    return SimpleNamespace(market_id=market_id, symbol=symbol, market=market,
                           best_buy_price=lambda: bid, best_sell_price=lambda: ask)


def test_each_market_is_shown_at_its_own_decimals(capsys):
    desk = FakeDesk([book(1, "A", 2, 405, 410), book(2, "GOLD", 4, 40525, 40530)],
                    {1: [405], 2: [40527]})

    ticker.display(desk, None)

    out = capsys.readouterr().out
    assert "$ 4.05" in out and "$ 4.10" in out
    assert "$4.0525" in out and "$4.0530" in out and "$4.0527" in out
    assert "$405.25" not in out
