from seasons import minutes_lived

def main():
    test_1()
    test_2()


def test_1():
    assert minutes_lived(1999, 1, 1) == "Twelve million, six hundred seven thousand, two hundred minutes"

def test_2():
    assert minutes_lived(2000, 5, 5) == "Eleven million, nine hundred one thousand, six hundred minutes"


if __name__ == "__main__":
    main()