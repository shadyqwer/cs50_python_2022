import sys

def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif sys.argv[1].strip().endswith('.py') == False:
        sys.exit('Not a python file')
    else:
        try:
            with open(sys.argv[1], 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            sys.exit('File does not exits')
        count = 0
        for line in lines:
            if len(line.strip()) != 0 and line.lstrip().startswith('#') == False:
                count += 1
        print(count)
        return count


if __name__ == '__main__':
    main()
