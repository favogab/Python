# A program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
text = input("Input: ")
output = ""

# Iterate through each character in the input text
for c in text:
    if c not in "AEIOUaeiou":
        output += c

print(output)