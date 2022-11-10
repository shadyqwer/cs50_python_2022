def main():
    s = input('What is the answer to the Great Question of Life, the Universe and Everything? ')

    if s.strip().lower() in ['42', 'forty-two', 'forty two']:
        print('Yes')
    else:
        print('No')


main()
