#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line to /output/entry.txt — one line, nothing else.
Deterministic, offline, stdlib-only: the line is a fixed string, so every
run produces byte-identical output.
"""

from pathlib import Path

ROAST = (
    "My fridge drops every ice cube like it's coughing up a Lego, "
    "then hums like it deserves a round of applause."
)
# Verified: 108 characters, one line, within the 200-character gate.

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the line, nothing else.
    OUTPUT_PATH.write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()
