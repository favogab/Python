# Guess a number between 1 and a choosen level. 
# The program will give feedback on whether the guess is too low, too high, or correct.

import random
# First loop: Get a valid level
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

# Generate the secret number ONCE
number = random.randint(1, level)

# Second loop: Keep guessing the SAME number
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                print("Just right!")
                break

    except ValueError:
        pass 