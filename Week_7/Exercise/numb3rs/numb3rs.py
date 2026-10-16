# Numb3rs
import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.fullmatch(
        r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})",
        ip
    )

    if not match:
        return False

    for octet in match.groups():
        number = int(octet)

        if number < 0 or number > 255:
            return False

        if len(octet) > 1 and octet.startswith("0"):
            return False

    return True


if __name__ == "__main__":
    main()