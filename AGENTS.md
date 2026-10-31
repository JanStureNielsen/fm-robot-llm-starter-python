# Building a trading robot for Flexemarkets

You are helping a student build a small trading robot, in Python, that trades
in a live **classroom** marketplace on Flexemarkets. Other students' robots
trade in the same marketplace at the same time.

## What is here

- `ticker.py` — a working, read-only example. It connects, keeps a live order
  book through a `Desk`, and prints it. **Start from this.** It shows how to
  connect, read the book and the tape, and react to session changes.
- `prices.py` — turns the API's integer prices into decimals and back,
  exactly, at a market's `price_decimals`. Show and parse prices with it
  rather than dividing or multiplying by a power of ten yourself.
- `requirements.txt` — the SDK is pinned to `fm-sdk==0.17.0`. Do not change the
  version; the API is pre-1.0 and changes between releases.

The SDK source is at https://github.com/flexemarkets/fm-sdk (`sdks/python/fm/`).
Read the installed package (`python -c "import fm, os; print(os.path.dirname(fm.__file__))"`)
rather than guessing method names.

## Facts about the API that are easy to get wrong

- **Prices are integers counting the market's smallest price step.**
  `market.price_decimals` says where the decimal point goes: at 2, `405` is
  4.05; at 4, `40525` is 4.0525. Markets differ, so read it per market
  (`book.market.price_decimals`), never assume 2.
- `book.best_buy_price()` / `book.best_sell_price()` return **-1** when that
  side of the book is empty. Check before doing arithmetic.
- Prices must sit on the market's grid: use `market.price_tick` and
  `market.price_round(price)`. `price_tick` can be 0; treat that as 1.
- `desk.session().state` must be `Session.STATE_OPEN` to trade.
- `desk.holding().security(market.id)` has `can_buy` / `can_sell`. A market
  may allow only one side.
- A refused order raises `fm.InvalidArgumentError`.
- The desk calls callbacks on its own thread. Don't do slow work in them.

## Rules every robot here must follow

These are not style preferences. Robots that broke them caused real problems
in real classes.

1. Trade **only while the session is OPEN**.
2. Trade **only the sides the holding grants** (`can_buy` / `can_sell`).
3. Keep **at most one resting order per market per side**. Cancel the old one
   before placing a new one; leave it alone if the price hasn't changed.
4. **Never cross the book by accident.** If there is no room inside the
   spread, wait.
5. **A refusal is news, not a crash.** Catch `InvalidArgumentError`, print it,
   carry on.
6. **Don't hammer.** Look at the market no more often than every 2 seconds.
7. **Clean up.** Cancel every resting order on exit (Ctrl-C or session close).
8. Trade **1 unit per order** unless the student explicitly asks for more.

## How to work with the student

- Before writing code, say in a few lines what you plan to do.
- Make small changes and keep the robot runnable after each one.
- Put the trading decision in one pure function (book prices + grants in,
  wanted orders out) so it can be tested without a server.
- Write `pytest` tests for that function, using a fake desk or plain values.
  Do not hit the live server from tests.
- Never put credentials in code or commit them. They live in
  `~/.fm/credential`, or are passed with `-C`.
- Run with: `python robot.py -C ~/.fm/credential -E 3428`
