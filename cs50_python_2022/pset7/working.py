import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    # 9:00 AM to 5:00 PM
    reg = r'^(1?[0-9]):?([0-9]{2})?\s(AM||PM)\sto\s(1?[0-9]):?([0-9]{2})?\s(AM||PM)$'
    if times := re.search(reg, s):
        time1 = am_pm_to_24(times.group(1), times.group(2), times.group(3))
        time2 = am_pm_to_24(times.group(4), times.group(5), times.group(6))

        return f'{time1} to {time2}'
    else:
        raise ValueError

def am_pm_to_24(hours, minutes, am_pm):
    hours = int(hours)
    minutes = 0 if minutes is None else int(minutes)
    if minutes >= 60 or minutes < 0 or hours > 12 or hours < 0:
        raise ValueError
    if am_pm == 'AM':
        if hours == 12:
            return f'00:{minutes:02}'
        else:
            return f'{hours:02}:{minutes:02}'
    elif am_pm == 'PM':
        if hours == 12:
            return f'12:{minutes:02}'
        else:
            return f'{hours+12:02}:{minutes:02}'


if __name__ == "__main__":
    main()
