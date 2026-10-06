# Outdated

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        try:
            date = input("Date: ").strip()

            # Parsehe date in different formats
            if "/" in date:
                month, day, year = date.split("/")

                month = int(month)
                day = int(day)
                year = int(year)

                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break

            # Parse the date in the format "Month Day, Year"
            else:
                month, day, year = date.split()

                #  Check for comma at the end of the day
                if not day.endswith(","):
                    continue

                day = day.strip(",")

                if month in months:
                    month = months.index(month) + 1
                    day = int(day)
                    year = int(year)

                    if 1 <= day <= 31:
                        print(f"{year}-{month:02}-{day:02}")
                        break

        except ValueError:
            pass


main()