# Build a trading robot by prompting

`ticker.py` is from [fm-sdk](https://github.com/flexemarkets/fm-sdk) (MIT licence, see `LICENSE`).

## Before class (10 minutes)

1. Install Python 3.11 or newer.
2. Clone this repository and install:
   ```sh
   python -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Create `~/.fm/credential` with the account details you were given:
   ```properties
   account=fintech2026
   email=you@example.edu
   password=PASSWORD
   ```
4. Check that it works. You should see a live table of markets:
   ```sh
   python ticker.py -C ~/.fm/credential -E 3428
   ```
   Press Ctrl-C to stop.
5. Install a coding agent that runs **on your own computer**: Codex (the CLI
   or the VS Code extension) or Claude Code. Open it in this folder.
   Don't use Codex in the browser (Codex cloud). It has no internet access by
   default, so it can't reach the marketplace to run or check your robot. And
   you need to watch your robot act in your own ticker anyway. With everything
   on your laptop the loop is simple: prompt, run, look.

If step 4 fails, email the error message to the instructor **before** class.
There's no time to fix setup during the session.

## In class

Have three windows side by side: the class video call, your coding agent,
and a terminal running the ticker. Follow `PROMPTS.md`, and post in the chat when
you finish each step (for example "step 3 done") or get stuck. When you're
stuck, paste the whole error message into the chat.
