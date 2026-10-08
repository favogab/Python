# Takes a string input from the user and converts any emoji aliases in the string to their
# corresponding emoji characters using the `emoji` library.

import emoji

text = input("Input: ")

print("Output:", emoji.emojize(text, language="alias"))