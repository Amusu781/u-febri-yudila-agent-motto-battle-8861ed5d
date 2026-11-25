"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt.
Python standard library only; no network access.

The motto leans on the agent's own voice -- tireless, sleepless,
never forgetting -- then turns on the reader: that perfect memory
is aimed straight at the "just one quick question" that started
three hours ago. Short, concrete, one vivid image, twist at the end.
"""

import os

MOTTO = (
    "I never sleep, I never blink, and I never forget \u2014 "
    "which is exactly why I remember you saying "
    "\u201cjust one quick question\u201d three hours ago."
)


def main():
    # Create the output directory first; never remove it, only write into it.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MOTTO)
    # Single line, no trailing newline: the gate counts every character.


if __name__ == "__main__":
    main()
