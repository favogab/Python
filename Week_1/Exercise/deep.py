# This program asks the user for the answer to the ultimate question of life, the universe, and everything. 
# If the user inputs "42", "forty-two", or "forty two", it prints "Yes". Otherwise, it prints "No".

answer = input("What is the answer to the ultimate question of life, the universe, and everything? ")

answer = answer.strip().lower()

# Check if the answer is correct
if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")

