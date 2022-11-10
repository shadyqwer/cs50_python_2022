# https://cs50.harvard.edu/python/2022/psets/5/test_fuel/

from fuel import convert, gauge
import pytest

def main():
    test_conver()
    test_gauge()


def test_convert():
    assert convert('3/4') == 75
    assert convert('1/4') == 25
    assert convert('4/4') == 100
    assert convert('0/4') == 0
    with pytest.raises(ZeroDivisionError):
        convert('4/0')
    with pytest.raises(ValueError):
        convert('three/four')


def test_gauge():
    assert gauge(75) == '75%'
    assert gauge(25) == '25%'
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'

if __name__ == '__main__':
    main()
