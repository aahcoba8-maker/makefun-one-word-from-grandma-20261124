"""One Word From Grandma — entrypoint.

Writes the single chosen word to entry.txt in the output directory.
The word is the whole entry: one word, no spaces, nothing else.
"""

import os

# The word: "eat" is the whole of grandma in one breath — her greeting at
# the door, her diagnosis for every problem, and her proof of love, served
# on a plate whether you are hungry or not.
WORD = "eat"


def main():
    # Guard: the entry must stay exactly one word — no spaces, no padding.
    assert WORD == WORD.strip() and " " not in WORD and WORD != ""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(WORD)


if __name__ == "__main__":
    main()
