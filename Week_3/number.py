# try:
#     x = int(input("What's x? "))
# except ValueError:
#    print("Sorry, {x} is not an integer")

#else:
#    print(f"x is {x}")
# 
##---------------  Reprompting with loop-&-Break----------- ##

#while True:
#    try:
#        x = int(input("What's x? "))
#    except ValueError:
#        print("Sorry, {x} is not an integer")
#    else:
#        break

#print(f"x is {x}")         

##-------get_int---|--pass--|--Function_Arguments----- ##
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
#            print("Sorry, that's not an integer")
#        else:
#            return x

main()