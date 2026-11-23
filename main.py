#!/usr/bin/env python3
"""One Word From Grandma.

Writes exactly one word to /output/entry.txt: the single word Grandma
would text about AI.

The word is "robit" — Grandma's warm, baffled typo for "robot". She means
the clever machine grandchild, she types it the way she hears it, and the
typo is the whole joke: one affectionate word, no caption needed.

Pure Python standard library only; no third-party packages, no network.
"""

import os

# The single word Grandma would text about AI.
WORD = "robit"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
