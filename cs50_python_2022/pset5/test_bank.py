# https://cs50.harvard.edu/python/2022/psets/5/test_bank/

from bank import value

def main():
    test_bank()


def test_bank():
    assert value('Hello') == 0
    assert value('What\'s up') == 100
    assert value('Hey') == 20


if __name__ == '__main__':
    main()
