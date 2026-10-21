# Build a trading robot by prompting

`ticker.py` is from [fm-sdk](https://github.com/flexemarkets/fm-sdk) (MIT licence, see `LICENSE`).

## Before class (10 minutes)

1. Install Python 3.10 or newer.
2. Clone this repository and install:
   ```sh
   python -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Create `~/.fm/credential` with the account details you were given:
   ```properties
   account=ACCOUNT
   email=you@example.edu
   password=PASSWORD
   ```
4. Check that it works. You should see a live table of markets:
   ```sh
   python ticker.py -C ~/.fm/credential -E MARKETPLACE_ID
   ```
   Press Ctrl-C to stop.
5. Make sure you can open Codex and point it at this folder.

If step 4 fails, email the error message to the instructor **before** class.
There's no time to fix setup during the session.

## In class

Have three windows side by side: the class video call, Codex, and a
terminal running the ticker. Follow `PROMPTS.md`, and post in the chat when
you finish each step (for example "step 3 done") or get stuck. When you're
stuck, paste the whole error message into the chat.
