def main():
    camel = input(' ')
    snake = ''
    # 65 90
    for c in camel:
        if 65 <= ord(c) <= 90:
            snake += '_' + c.lower()
        else:
            snake += c
    print(snake)

main()
