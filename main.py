"""One-Line Office Joke: 24-Hour Sprint — make.fun entry.

Writes a single original one-line joke about office life to
/output/entry.txt (UTF-8, 1-200 characters, one line).
Python standard library only.
"""

import os

JOKE = (
    "I typed 'per my last email' today and immediately felt like the most "
    "powerful person in the office."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
