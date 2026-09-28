# x = int(input("What's x? "))

# if x % 2 == 0:
#    print("Even")
# else:
#    print("Odd")     

# -----Boolen --------
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# ----Defining_a_Function ---------
def is_even(n):
    return n % 2 == 0      

main()