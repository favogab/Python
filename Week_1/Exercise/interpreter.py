# This program takes a mathematical expression as input and evaluates it.
expression = input("Expression: ")
x, y, z = expression.split(" ")

# Convert x and z to integers
x = float(x)
z = float(z)

# Perform the calculation based on the operator
if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)
