#!/usr/bin/env python3
"""Entry program for One Word From Your Ex.

Writes exactly ONE word (at most 24 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
the word my ex would use to describe me. The word is
'intense' -- which is what 'a lot' becomes in the retelling.
"""

import os

WORD = "almost"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
