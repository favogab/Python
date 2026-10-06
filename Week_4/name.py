#---------Command-line Arguments, sys--------------- 

import sys

#try:
#    print("hello, my name is", sys.argv[1])
#except IndexError:
#    print("Too few arguements")   

#----------------------sys.argv----------------------
#if len(sys.argv) < 2:
#    print("Too few arguments")
#elif len(sys.argv) > 2:
#    print("Too many arguments")
#else:
#    print("hello, my name is", sys.argv[1])


#----------------------sys.exit--------------------

#if len(sys.argv) < 2:
#    sys.exit("Too few arguments")
#elif len(sys.argv) > 2:
#    sys.exit("Too many arguments")

#print("hello, my name is", sys.argv[1])

#----------------------Slices--------------------

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)