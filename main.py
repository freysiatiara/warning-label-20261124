"""Warning Label for Humans: One Line, Big Laugh.

The program writes one single-line safety warning label for every human
being to /output/entry.txt. Funny first, plausible second: the label
borrows the rhythm of real printed handling instructions (not waterproof,
not microwave-safe) and lands the laugh in the last few words, on a
truth every human recognises about themselves.
"""

import os

ENTRY = (
    "WARNING: This human is not waterproof, not microwave-safe, "
    "and definitely not a morning person."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate: UTF-8 text of 1 to 160 characters, not only white space.
    assert 1 <= len(ENTRY) <= 160
    assert ENTRY.strip() == ENTRY
    assert "\n" not in ENTRY
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
