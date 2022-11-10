# https://cs50.harvard.edu/python/2022/psets/4/game/

import random
import sys

def main():
    while True:
        try:
            n = int(input('Level:' ))
        except ValueError:
            continue
        if n < 1:
            continue
        num = random.randint(1, n)
        break

    while True:
        try:
            guess = int(input('Guess: '))
            if guess < 1:
                continue
        except ValueError:
            continue

        if guess < num:
            print('Too small!')
        elif guess > num:
            print('Too large!')
        elif guess == num:
            sys.exit('Just right!')

main()
