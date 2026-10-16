
import re


def main():
    print(count(input("Text: ")))


def count(s):
    # Match "um" as a separate word, regardless of capitalization.
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)

    return len(matches)


if __name__ == "__main__":
    main()
