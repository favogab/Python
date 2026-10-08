# program that generates a simple math quiz for the user based on the selected difficulty level. 
# The user is prompted to enter a level (1, 2, or 3), and then the program generates 10 random addition problems with numbers 
# appropriate for that level. The user has three attempts to answer each problem correctly, and the program keeps track of the user's score.

import random


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level

        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        for _ in range(3):
            try:
                guess = int(input(f"{x} + {y} = "))

                if guess == answer:
                    score += 1
                    break
                else:
                    print("EEE")

            except ValueError:
                print("EEE")

        else:
            print(f"{x} + {y} = {answer}")

    print(score)