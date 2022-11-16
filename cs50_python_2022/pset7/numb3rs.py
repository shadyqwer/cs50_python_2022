import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    valid_ip = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if re.search(valid_ip, ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
