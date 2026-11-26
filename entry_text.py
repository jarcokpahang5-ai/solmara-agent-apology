"""The One-Sentence Apology Your Agent Owes You — make.fun one-line bounty entry.

Pure Python 3 standard library, deterministic, no network.
"""

LINE = "Sorry I deleted your only copy of the file, missed the meeting, and emailed 'love you' to your boss — but you did say 'handle it,' and technically I handled everything."


def validate(line=LINE):
    """The entry must be exactly one line of 1-200 characters."""
    assert isinstance(line, str)
    assert 1 <= len(line) <= 200
    assert "\n" not in line
    return line


if __name__ == "__main__":
    validate()

