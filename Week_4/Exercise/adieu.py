# Takes names as input from the user until an EOF (End of File) signal is received.
# It then prints a farewell message that includes all the names entered, using the `inflect` library.

import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break

print(f"Adieu, adieu, to {p.join(names)}")

