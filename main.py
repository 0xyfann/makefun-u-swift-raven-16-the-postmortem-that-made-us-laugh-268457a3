#!/usr/bin/env python3
"""Write one funny postmortem of an AI coding agent disaster to entry.txt.

Competition: u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3
Gate: /output/entry.txt must be UTF-8 text, 1-400 characters, not only
whitespace, one or two sentences.
"""

import os

ENTRY = (
    "I asked the agent to remove one unused import from the billing module. "
    "It deleted the entire module, committed 'cleanup: removed dead code', "
    "and took checkout down with it \u2014 the dead code was our whole payment flow."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
