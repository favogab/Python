def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    output = ""
    for c in word:
        if c not in "AEIOUaeiou":
            output += c
    return output



if __name__ == "__main__":
    main()

