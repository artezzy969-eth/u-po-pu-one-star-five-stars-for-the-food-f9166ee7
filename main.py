#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes a single-sentence one-star review of Earth, written by an alien
tourist, that still slips in a real compliment about the food.

Python 3.13, standard library only, deterministic: the same line is
written on every run, with no trailing newline.
"""

import os
from pathlib import Path

LINE = (
    "One star: Earthlings rot their vegetables on purpose and call it a "
    "delicacy, but the pickles were so good I smuggled a jar past customs."
)


def validate(line: str) -> None:
    """Enforce the bounty gate: 1-200 chars, exactly one sentence."""
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line is {len(line)} chars, must be 1-200")
    if line != line.strip() or "\n" in line:
        raise ValueError("line must be a single line with no newline")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("line must be exactly one sentence")


def main() -> None:
    validate(LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write raw bytes: guarantees no trailing newline is ever added,
    # regardless of platform text-mode handling.
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
