
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit("Not a Python file")

count = 0

try:
    with open(filename, "r") as file:
        for line in file:
            if not line.strip() or line.lstrip().startswith("#"):
                continue

            count += 1

except FileNotFoundError:
    sys.exit("File does not exist")

print(count)
