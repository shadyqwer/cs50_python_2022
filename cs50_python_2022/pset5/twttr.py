# https://cs50.harvard.edu/python/2022/psets/5/test_twttr/
import re

def main():
    string = input(' ')
    print(shorten(string))

def shorten(word):
    return re.sub('[aeiouAEIOU]', '', word)


if __name__ == "__main__":
    main()
