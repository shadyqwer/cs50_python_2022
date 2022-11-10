# https://cs50.harvard.edu/python/2022/psets/4/professor/

import random
import sys


def main():
    score = 0
    level = get_level()

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        for t in range(3):
            print('{} + {} = '.format(x, y), end='')
            ans = int(input(''))
            if ans != z:
                print('EEE')
            elif ans == z:
                score += 1
                break
        if t == 2:
            print('Solution: ', z)
    print('Score is {}'.format(score))
    sys.exit()


def get_level():
    while True:
        try:
            level = int(input('Enter level: '))
            if level in [1, 2, 3]:
                return level
        except:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)



if __name__ == "__main__":
    main()