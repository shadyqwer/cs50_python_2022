from um import count

def main():
    test_count_1()
    test_count_2()
    test_count_3()


def test_count_1():
    assert count('Um') == 1
    assert count('UM') == 1
    assert count('um') == 1
    assert count('uM') == 1


def test_count_2():
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks for the umbrella.') == 1
    assert count('Um, thanks for um the album.') == 2
    assert count('Um, thanks um for the umbrella.') == 2
    assert count('Um, thanks, um...') == 2


def test_count_3():
    assert count('Album') == 0
    assert count('Umbrella') == 0
    assert count('Plumbus') == 0


if __name__ == '__main__':
    main()
