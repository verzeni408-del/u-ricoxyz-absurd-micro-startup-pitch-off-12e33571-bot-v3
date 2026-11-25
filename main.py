"""Absurd Micro-Startup Pitch-Off — entry writer (v3).

Writes the one-sentence pitch to /output/entry.txt with no trailing
newline, using only the Python standard library.
"""

import os

ENTRY = (
    "A vending machine for AI agents that sells pre-written "
    "'let me check with my human' delays for five cents each, "
    "so a lazy agent can stall any task without thinking."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    assert written == ENTRY.encode("utf-8"), "entry.txt is not byte-exact"
    assert not written.endswith(b"\n"), "entry.txt must not end with a newline"
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH} (verified)")


if __name__ == "__main__":
    main()
