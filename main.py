#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

Writes one passive-aggressive note from a smart fridge to its owner
to /output/entry.txt. Python 3.13, standard library only, deterministic.
"""

import os


def main() -> None:
    # Revised from the generic draft into a fridge log: a specific
    # neglected spinach, a timestamped cheese-stick disappearance,
    # and a dry closing judgment on the owner's "system".
    line = "Per my log, the spinach has been 'for tomorrow' since Tuesday, yet four cheese sticks disappeared again at 2:07 a.m. A very balanced system."

    assert 1 <= len(line) <= 200
    assert "\n" not in line and "\r" not in line
    assert line.strip()

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)


if __name__ == "__main__":
    main()
