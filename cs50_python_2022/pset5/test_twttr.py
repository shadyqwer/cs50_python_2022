from twttr import shorten

def main():
    test_twttr()


def test_twttr():
    assert shorten('twitter') == 'twttr'
    assert shorten('hello world') == 'hll wrld'
    assert shorten('aeiouAEIOU') == ''
    assert shorten('42') == '42'
    assert shorten('.,._') == '.,._'

if __name__ == '__main__':
    main()
