"""Write the deterministic Two Robots in an Elevator entry."""

import os
from pathlib import Path


SETUP = "I've logged your six 'Door Close' presses as a motor fault. "
PUNCHLINE = "You're welcome."
ENTRY = SETUP + PUNCHLINE


def main():
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
