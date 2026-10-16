
from validator_collection import checkers


def main():
    email = input("Email: ")

    # Check the email's format without looking up its domain.
    if checkers.is_email(email):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
