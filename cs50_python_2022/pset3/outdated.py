# https://cs50.harvard.edu/python/2022/psets/3/outdated/

def main():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    while True:
        date = input(' ')
        date = date.strip()
        if '/' in date:
            m, d, y = date.split('/')

        elif ',' in date:
            date = date.replace(',','')
            m, d, y = date.split(' ')
            if m in months:
                m = months.index(m) + 1
            else:
                continue
        else:
            continue
        try:
            if int(m) > 12 or int(d) > 31:
                continue
            else:
                break
        except ValueError:
            continue

    m = int(m)
    d = int(d)
    print('{}-{:02d}-{:02d}'.format(y, m, d))


main()
