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

LABEL_WORDS = ("WARNING:", "CAUTION:", "DANGER:", "NOTICE:")


def validate(entry: str) -> str:
    """Enforce the bounty gate plus the label form the judge weighs.

    Gate: UTF-8 text of 1 to 160 characters, not only white space.
    Label form: one single line, no leading/trailing whitespace, opening
    with a real printed-label word so it reads as a warning label for
    humans rather than a plain sentence.
    """
    assert isinstance(entry, str)
    assert 1 <= len(entry) <= 160, f"entry is {len(entry)} chars, gate is 1-160"
    assert entry.strip() == entry, "entry has leading/trailing whitespace"
    assert "\n" not in entry and "\r" not in entry, "entry must be one line"
    assert entry.startswith(LABEL_WORDS), "entry must open as a label"
    return entry


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = validate(ENTRY)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
