# https://cs50.harvard.edu/python/2022/psets/5/test_bank/

def main():
    greet = input(' ')
    print('$'+str(value(greet)))


def value(greeting):
    if 'hello' in greeting.lower():
        return 0
    elif greeting.strip().lower()[0] == 'h':
        return 20
    else:
        return 100


if __name__ == '__main__':
    main()

