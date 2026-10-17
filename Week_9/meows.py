#MEOWS = 3
#for _ in range(MEOWS):
#    print("meow")

#class Cat:
#    MEOWS = 3

#    def meow(self):
#        for _ in range(Cat.MEOWS):
#            print("meow")

#cat = Cat()
#cat.meow() 
# 
# 


def meow(n: int) -> str:
    """
    Meow n times.
    :param n: Number of times to meow
    """
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")                  