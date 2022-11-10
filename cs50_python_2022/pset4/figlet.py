# https://cs50.harvard.edu/python/2022/psets/4/figlet/

from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    if len(sys.argv) == 1:
        s = input(' ')
        figlet.setFont(font=random.choice(figlet.getFonts()))
        print(figlet.renderText(s))
    elif len(sys.argv) == 3:
        if (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in figlet.getFonts():
            s = input(' ')
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(s))
        else:
            sys.exit('Invalid usage')
    else:
        sys.exit('Invalid usage')

main()
