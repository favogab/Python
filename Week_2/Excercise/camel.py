# This program converts a camelCase string to snake_case.
camel = input("camelCase: ")
snake = ""

# Convert camelCase to snake_case
for c in camel:
    if c.isupper():
        snake += "_" + c.lower()
    else:
        snake += c

print(snake)