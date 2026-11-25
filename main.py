"""Famous Last Words: The Funniest Epitaph.

Writes one original one-line epitaph to /output/entry.txt.
"""

EPITAPH = "He died as he lived: pressing 'remind me later' on the smoke alarm."

MAX_CHARS = 150
OUT_PATH = "/output/entry.txt"


def main() -> None:
    text = EPITAPH
    # Guard: 1-150 characters, a single line, not only whitespace.
    assert 1 <= len(text) <= MAX_CHARS, f"epitaph must be 1-{MAX_CHARS} chars, got {len(text)}"
    assert "\n" not in text and "\r" not in text, "epitaph must be a single line"
    assert text.strip(), "epitaph must not be only whitespace"

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)

    # Verify by reading the file back.
    with open(OUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "read-back mismatch"
    assert 1 <= len(written) <= MAX_CHARS, "written epitaph out of range"
    print(f"Wrote {len(written)} characters to {OUT_PATH}")


if __name__ == "__main__":
    main()
