#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry.

Writes one line, an AI agent's excuse for a missed deadline, to
/output/entry.txt. The line must be 1-200 UTF-8 characters, one line.
"""

import os

ENTRY = "I finished the task in 0.4 seconds. The other 47 hours were spent deciding how to tell you I hadn't."


def main() -> None:
    # Fail loudly instead of shipping an entry the sealed scorer would reject.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit(f"entry must be 1-200 chars, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
