# Replaces emoticons in a given text with emoji.
def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

# Get user input, convert it, and show the result.
def main():
    message = input()
    result = convert(message)
    print(result)


main()