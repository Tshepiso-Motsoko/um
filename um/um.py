import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # Regular expression pattern to match the word "um" as a separate word
    pattern = r"\bum\b"

    # Find all occurrences of the pattern in the input text
    matches = re.findall(pattern, s, flags=re.IGNORECASE)

    # Return the count of matches
    return len(matches)


if __name__ == "__main__":
    main()
