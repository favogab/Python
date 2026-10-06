#-------------Packages-cowsay-------- ## 
#import cowsay
#import sys

#if len(sys.argv) == 2:
#    cowsay.cow("hello, " + sys.argv[1])
#    cowsay.trex("hello, " + sys.argv[1])

#-------testing_my_Libraries_from_saying_file------ ## 

import sys

from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])







