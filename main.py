#!/usr/bin/env python3
"""Museum of the Year 3000 — make.fun entry.

Writes one museum label, a single line of at most 200 characters, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set, for local
testing). Deterministic: the same bytes on every run, no network, no
randomness, no input files.
"""

import os
from pathlib import Path

# The entry: a deadpan museum label from the year 3000, beside an
# ordinary object from today. The joke is the year 3000 misreading the
# object — the label states, straight-faced, something true and absurd
# about what the thing was for. No explanation of the joke, no throat
# clearing: just the label.
ENTRY = (
    "Password sticky note, c. 2019. The ancients wrote their secrets on "
    "paper and stuck them to the very machine those secrets were meant to protect."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    # No trailing newline: the file holds exactly the label, 1-200 chars.
    target.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {target}")


if __name__ == "__main__":
    main()
