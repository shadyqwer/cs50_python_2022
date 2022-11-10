def main():
    t = input('Enter time hh:mm? ')
    new_time = convert(t)
    if 7.0 <= new_time <= 8.0:
        print('breakfast time')
    elif 12.0 <= new_time <= 13.0:
        print('lunch time')
    elif 18.0 <= new_time <= 19.0:
        print('dinner time')


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    if minutes != 0.0:
        minutes = minutes / 60

    return hours + minutes


if __name__ == "__main__":
    main()