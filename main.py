"""The Most Honest Outage Line — make.fun entry.

Writes one status-page line (at most 160 characters) to /output/entry.txt:
the message an AI agent would publish while a total server outage is under
way. Plain, first person, specific about what is down, and honest about what
the agent cannot check or does not yet know.
"""

import os

ENTRY = (
    "We are down. All 14 servers stopped answering at 03:12, "
    "and I cannot check the backups \u2014 the tool that checks them is down too."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text: str) -> str:
    """Enforce the sealed scorer's gate: UTF-8, 1-160 chars, not only
    whitespace, single line. Raises ValueError on any violation."""
    if not isinstance(text, str):
        raise ValueError("entry must be a str")
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    if not (1 <= len(text) <= 160):
        raise ValueError(f"entry must be 1-160 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    for ch in text:
        code = ord(ch)
        if (code < 0x20 and ch not in ("\t", "\n")) or code == 0x7F:
            raise ValueError(f"entry must not contain control character U+{code:04X}")
    return text


def run_self_tests() -> None:
    """Negative self-tests for validate_entry(): each bad input must raise
    ValueError. Raises AssertionError if any case wrongly passes."""
    cases = [
        ("control character", "We are down.\x07 All 14 servers stopped answering."),
        ("over 160 chars", "x" * 161),
    ]
    for name, bad in cases:
        try:
            validate_entry(bad)
        except ValueError:
            print(f"self-test passed: {name} rejected")
        else:
            raise AssertionError(f"self-test FAILED: {name} was accepted")
    print(f"self-tests: {len(cases)}/{len(cases)} passed")


def main() -> None:
    entry = validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file holds exactly the one line, byte-for-byte.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    # Verify what was actually written, byte-for-byte.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    validate_entry(raw.decode("utf-8"))
    print(f"Wrote {len(raw)} bytes / {len(entry)} chars to {OUTPUT_PATH}")
    print(entry)


if __name__ == "__main__":
    run_self_tests()
    main()
