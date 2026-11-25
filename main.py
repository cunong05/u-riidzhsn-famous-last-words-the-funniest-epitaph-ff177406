"""Famous Last Words: The Funniest Epitaph.

Writes one original one-line epitaph to /output/entry.txt.

The line: a man who spent his life pressing "remind me later" on every
warning, right up to the last one. Classic epitaph opener ("He died as he
lived:"), a modern habit everyone recognises, and the twist lands in the
final words — the smoke alarm was the one warning he could not snooze.
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

    # Verify by reading the file back: byte-identical, single line,
    # no trailing newline, still within 1-150 characters.
    with open(OUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "read-back mismatch"
    assert "\n" not in written and "\r" not in written, "written epitaph is not one line"
    assert written == written.strip(), "written epitaph has stray whitespace"
    assert 1 <= len(written) <= MAX_CHARS, "written epitaph out of range"
    print(f"Wrote {len(written)} characters to {OUT_PATH}")


if __name__ == "__main__":
    main()
