# https://cs50.harvard.edu/python/2022/psets/3/grocery/

def main():
    grocery = {}
    while True:
        try:
            item = input(' ')
            item = item.upper()
            if item  not in grocery:
                grocery[item] = 1
            else:
                grocery[item] += 1
        except EOFError:
            break
    for key, value in sorted(grocery.items()):
        print('{} {}'.format(value, key))

main()
