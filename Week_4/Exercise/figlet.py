# 
    
import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    fonts = figlet.getFonts()
    selected = random.choice(fonts)
    figlet.setFont(font=selected)

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in figlet.getFonts():
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")      

text = input("Input: ")
print(figlet.renderText(text))      