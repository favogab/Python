
import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(rows, headers="firstrow", tablefmt="grid"))
