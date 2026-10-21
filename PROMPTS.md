# Prompt sheet

You don't have to type these word for word. They show what a good prompt
contains: **what to read, what to build, what "done" looks like.**

After every step: **read the diff, run it, and check the ticker** in a second
terminal to see what your robot did to the market. Then post "step N done"
in the chat.

## Step 1 — Understand before building

> Read `ticker.py` and `AGENTS.md`. Explain in plain English how the ticker
> gets live prices, and which SDK calls we'd need to place and cancel orders.
> Don't write any code yet.

Check: could you explain the `Desk` in two sentences in the chat?

## Step 2 — A robot that only watches

> Create `robot.py`, based on `ticker.py`. Every 2 seconds, while the session
> is OPEN, print each market's best bid, best ask, and what we are allowed to
> trade (`can_buy` / `can_sell`). No orders yet.

Check: it prints nothing while the session is paused, and stops when it closes.

## Step 3 — The decision, as a testable function

> Add a pure function `quotes(market, best_buy, best_sell, can_buy, can_sell)`
> that returns the prices to quote one unit at: a bid one tick above the best
> bid and an offer one tick below the best offer. Leave a side out if it isn't
> granted, the book is empty on that side, or it would cross. Write pytest
> tests for it first, including the edge cases, then make them pass.

Check: `pytest` passes. Read the tests. Do they test the edge cases you care about?

## Step 4 — Place orders

> Make the robot place the orders `quotes()` returns. Keep at most one resting
> order per market per side: if the price changed, cancel and re-place; if
> not, leave it. Catch refused orders, print them, and carry on.

Check: in the ticker, you see your quotes appear one tick inside the spread,
and there is never more than one of yours per side.

## Step 5 — Guardrails

> Add: cancel all our resting orders on Ctrl-C and when the session closes; a
> limit on how many units we may hold in each market; and a counter that
> stops the robot if more than 10 orders are refused in a minute.

Check: press Ctrl-C. Did your orders disappear from the ticker?

## Stretch goals (pick one)

- **A real strategy.** Only buy when the last trade is below the average of
  the last N trades, and sell when it's above.
- **Inventory-aware quoting.** Quote less aggressively on the side you
  already hold a lot of.
- **A P&L log.** Write each fill to a CSV and print your running profit.
- **Review.** Ask the agent: "Review robot.py against the rules in AGENTS.md
  and list every way it could break one." Then fix what it finds.

## Prompting habits that work

- Point at real code ("based on `ticker.py`") rather than describing from scratch.
- Ask for a plan or an explanation **before** code.
- One step at a time. Keep it runnable.
- Say what "done" means: a test, an output, a behaviour you can see.
- When it fails, paste the **whole** error, not your summary of it.
- You are responsible for every order your robot sends. Read the code.
