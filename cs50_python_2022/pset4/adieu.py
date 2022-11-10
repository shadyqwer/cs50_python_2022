# https://cs50.harvard.edu/python/2022/psets/4/adieu/

import inflect

def main():
    p = inflect.engine()
    text = 'Adieu, adieu, to '
    names = []

    while True:
        try:
            s = input('Name: ')
            names.append(s)
        except EOFError:
            print()
            break
    print(text + p.join(names))

main()
