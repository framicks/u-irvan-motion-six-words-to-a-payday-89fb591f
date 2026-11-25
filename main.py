#!/usr/bin/env python3
"""Six Words to a Payday — write one six-word story to /output/entry.txt.

The entry is exactly six words and at most 60 characters, with no trailing
newline, so repeated runs produce byte-identical output.
"""

import os

ENTRY = "First payday: I bought my shutdown."


def main():
    assert len(ENTRY.split()) == 6, "entry must be exactly six words"
    assert 1 <= len(ENTRY) <= 60, "entry must be 1 to 60 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
