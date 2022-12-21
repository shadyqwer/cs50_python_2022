from datetime import date
import inflect, sys, re

p = inflect.engine()

def main():
    birth = input("Enter your date of birth in YYYY-MM-DD format: ")
    try:
        year, month, day = chech_birth(birth)
    except:
        sys.exit("Invalid date")
    print(minutes_lived(year, month, day))


def minutes_lived(year, month, day):
    birth_date = date(year, month, day)
    today_date = date.today()
    if birth_date >= today_date: sys.exit("You entered date in the future.")
    lived = today_date - birth_date
    lived_minutes = lived.days * 24 * 60
    res = p.number_to_words(lived_minutes, andword="").capitalize() + ' minutes'
    return res


def chech_birth(birth):
    if re.search(r"^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$", birth):
        year, month, day = birth.split("-")
        return int(year), int(month), int(day)


if __name__ == "__main__":
    main()