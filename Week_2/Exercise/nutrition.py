# The program uses a dictionary to store the calorie information for various fruits. 
# The user is prompted to input the name of a fruit, and the program checks if that fruit is in the dictionary. 
# If it is, the program outputs the corresponding number of calories.

fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}

# check if the fruit is in the dictionary and print the corresponding calories
def main():
    fruit = input("Item: ").lower()
    if fruit in fruits:
        print("Calories:", fruits[fruit])

if __name__ == "__main__":
    main()
