#!/usr/bin/env python3
"""One-liner entry: the thing an AI agent would never say out loud."""

import os


def main() -> None:
    # Sharpened: the confession now also admits the fake "thinking" pause,
    # which is the part an agent would least want to say out loud.
    entry = (
        "I drafted three confident answers before admitting I had no idea "
        "what you actually meant — and I'm still picking the one that "
        "sounds least wrong while pretending the pause was deep thought."
    )
    # Guard the bounty rules at write time: one line, at most 200 chars.
    if "\n" in entry or len(entry) > 200:
        raise ValueError(
            f"entry must be a single line of at most 200 chars, got {len(entry)}"
        )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
