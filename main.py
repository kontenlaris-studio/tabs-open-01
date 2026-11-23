#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — writes one line to /output/entry.txt.

Stdlib only. Deterministic: the same line every run.
"""

import os

LINE = "31 tabs open: one for the work I'm doing, thirty for the person I keep promising myself I'll become."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
