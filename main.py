#!/usr/bin/env python3
"""The Router Confesses - make.fun bounty entry.

A home Wi-Fi router excuses itself for dropping the connection at the
climax of a movie. This program writes that one confession line to
$MAKEFUN_OUTPUT_DIR/entry.txt (or ./output/entry.txt when unset).

The line must be 1-200 characters of UTF-8 text, a single line, and
nothing else - the judge reads entries in pairs and keeps the funnier one.
"""

import os
import sys

LINE = (
    "I saw the twist coming and panicked — so I killed the Wi-Fi "
    "and took the ending down with me. You're welcome."
)


def main() -> int:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 chars, got {len(text)}", file=sys.stderr)
        return 1
    if "\n" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.getcwd(), "output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
