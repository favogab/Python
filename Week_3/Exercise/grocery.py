# Grocery List
groceries = {}

# Main function
def main():
    while True:
        try:
            item = input().strip().upper()

            if item:
                if item in groceries:
                    groceries[item] += 1
                else:
                    groceries[item] = 1

        except EOFError:
            break

    for item in sorted(groceries):
        print(f"{groceries[item]} {item}")


if __name__ == "__main__":
    main()