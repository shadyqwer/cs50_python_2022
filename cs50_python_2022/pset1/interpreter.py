def main():
    s = input(' ')
    x, y, z = s.split(' ')
    x = float(x)
    z = float(z)
    if y == '+':
        print(x + z)
    elif y == '-':
        print(x - z)
    elif y == '*':
        print(x * z)
    elif y == '/':
        print(x / z)


main()
