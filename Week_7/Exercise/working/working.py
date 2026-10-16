
import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Match both times, including optional minutes and AM/PM.
    pattern = r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)"
    match = re.fullmatch(pattern, s)

    if not match:
        raise ValueError("Invalid time format")

    # Extract the two times from the matched groups.
    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    start = to_24_hour(start_hour, start_minute, start_period)
    end = to_24_hour(end_hour, end_minute, end_period)

    return f"{start} to {end}"


def to_24_hour(hour, minute, period):
    hour = int(hour)

    # Missing minutes mean exactly on the hour.
    minute = int(minute) if minute is not None else 0

    # Check the clock values before converting anything.
    if not 1 <= hour <= 12 or not 0 <= minute <= 59:
        raise ValueError("Invalid time")

    # Midnight starts at 00, while afternoon hours add 12.
    if period == "AM" and hour == 12:
        hour = 0
    elif period == "PM" and hour != 12:
        hour += 12

    # Keep hours and minutes in two-digit format.
    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
