#!/usr/bin/env python3
"""Write one micro-confession to /output/entry.txt.

The entry is exactly two parts: a To: line naming who it was meant
for, and the unsent message itself, one line written as it was typed.
"""
import os

ENTRY = (
    "To: my brother, who still thinks I chose the army over him\n"
    "i never enlisted, i failed the medical and i've let you be proud of me for three years because i couldn't say it out loud"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
