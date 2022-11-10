# https://cs50.harvard.edu/python/2022/psets/5/test_plates/

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if s.isalnum() == False or s[0:2].isalpha() == False:
        return False
    for i, j in enumerate(s):
        if j.isdigit():
            if s[i] == '0' or s[i:].isdigit() == False:
                return False
            break
    return True

if __name__ == '__main__':
    main()
