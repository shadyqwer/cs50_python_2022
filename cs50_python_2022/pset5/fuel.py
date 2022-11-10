# https://cs50.harvard.edu/python/2022/psets/5/test_fuel/


def main():
    while True:
        f = input(' ')
        try:
            p = convert(f)
        except:
            continue
        print(gauge(p))

def convert(fraction):
    x, y = fraction.split('/')
    if int(y) == 0:
        raise ZeroDivisionError
    if int(x) > int(y):
        raise ValueError
    try:
        return int(round(int(x) / int(y), 2) * 100)
    except ValueError:
        raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return str(int(percentage)) + '%'


if __name__ == "__main__":
    main()