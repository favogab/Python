# This program greets the user and determines the appropriate monetary greeting based on the input.
greeting = input("Greeting: ")

# Strip any leading or trailing whitespace and convert the greeting to lowercase for consistent comparison.
greeting = greeting.strip().lower()

# Check the greeting and print the corresponding monetary value.
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")