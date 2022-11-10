# https://cs50.harvard.edu/python/2022/psets/3/fuel/

def main():
    while True:
        f = input('Fuel: ')
        try:
            x, y = f.split('/')
            x = int(x)
            y = int(y)
            fuel = x / y
            if x > y:
                continue
            break
        except (ValueError, ZeroDivisionError):
            continue
    fuel = round(fuel, 2)
    fuel *= 100
    if fuel >= 99:
        print('F')
    elif fuel <= 1:
        print('E')
    else:
        print(str(int(fuel)) + '%')


main()
