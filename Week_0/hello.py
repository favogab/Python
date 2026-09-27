# Ask me user their name | Remove whitespce from str and capitalize each word 
# name = input("What's your name? ").strip().title()

# split user's name into first and last name
# first, last = name.split(" ")

# Say Hello to User using their name
# print(f"Hello, {first}")


# Capitalize first Word 
# name = name.capitalize()

# Capitalize username 
# name = name.title()

# -------------------------------------------------------------
# Defining  Functions
# def hello(to="you"):
#    print("Hello", to)

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="you"):
    print("hello,", to)

main()    

#--------- End of Lecture 0 --------------------