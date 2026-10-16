# Watch 
import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = (
        r'<iframe\b[^>]*\bsrc="'
        r'https?://(?:www\.)?youtube\.com/embed/'
        r'([A-Za-z0-9_-]+)"'
    )

    match = re.search(pattern, s)

    if not match:
        return None

    video_id = match.group(1)
    return f"https://youtu.be/{video_id}"


if __name__ == "__main__":
    main()
