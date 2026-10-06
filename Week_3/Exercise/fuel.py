# Fuel Gauge: prompts the user for a fraction
def main():
    fuel = get_fuel("Fraction: ")

  # check if fuel is less than or equal ##
    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel}%")
 
def get_fuel(prompt):
    while True:
        try:
            fraction = input(prompt)
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if y == 0:
                raise ZeroDivisionError
            if x < 0 or y < 0:
                raise ValueError
            if x > y:
                raise ValueError
            return round((x / y) * 100)
        except (ValueError, ZeroDivisionError):
            pass

main()