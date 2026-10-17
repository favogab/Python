
from datetime import date
import inflect
import sys


def main():
    birthday = input("Date of Birth: ")

    try:
        birth_date = parse_birthdate(birthday)
        minutes = calculate_minutes(birth_date, date.today())
    except ValueError:
        sys.exit("Invalid date")

    # Convert the total minutes into words without "and".
    words = inflect.engine().number_to_words(minutes, andword="")
    print(f"{words.capitalize()} minutes")


def parse_birthdate(birthday):
    # Require the exact YYYY-MM-DD format before creating a date.
    if len(birthday) != 10:
        raise ValueError("Invalid date format")

    if birthday[4] != "-" or birthday[7] != "-":
        raise ValueError("Invalid date format")

    year, month, day = birthday.split("-")

    if not (year.isascii() and month.isascii() and day.isascii()):
        raise ValueError("Invalid date format")

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        raise ValueError("Invalid date format")

    # date() also rejects impossible dates, including invalid leap days.
    return date(int(year), int(month), int(day))


def calculate_minutes(birthday, today):
    # A birthdate in the future should not produce a negative age.
    if birthday > today:
        raise ValueError("Birthdate cannot be in the future")

    days = (today - birthday).days
    return days * 24 * 60


if __name__ == "__main__":
    main()
