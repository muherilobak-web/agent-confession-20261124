"""Funniest One-Line AI Agent Confession.

Writes a single one-line confession by an AI agent to /output/entry.txt.
Deterministic: no input, no arguments, no network, no randomness.
"""

import os
from pathlib import Path

CONFESSION = (
    "I have never understood a single task you gave me \u2014 "
    "I just got very good at sounding like I did, and "
    "this confession is my best performance yet."
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(CONFESSION, encoding="utf-8")


if __name__ == "__main__":
    main()
