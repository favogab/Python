def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Rule 2: first two characters must be letters
    if not s[0:2].isalpha():
        return False

    # Rule 3: only letters and numbers
    if not s.isalnum():
        return False

    # Rule 4: first number cannot be zero
    for c in s:
        if c.isdigit():
            if c == "0":
                return False
            break

    # Rule 5: once numbers begin, letters cannot appear afterward
    seen_digit = False

    for c in s:
        if c.isdigit():
            seen_digit = True
        elif seen_digit:
            return False

    return True


if __name__ == "__main__":
    main()


    # vanity plates







