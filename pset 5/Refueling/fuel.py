def main():
    while True:
        try:
            fraction = input("x/y: ")
            print(gauge(convert(fraction)))
            break

        except (ValueError,ZeroDivisionError):
            pass

def convert(fraction):
    num, denom = fraction.split("/")
    num, denom = int(num), int(denom)
    percentage = round((num / denom) * 100)

    return percentage

def gauge(percentage):
    if 1 < percentage < 99:
        return f"{percentage}%"
    elif percentage <= 1:
        return "E"
    elif 100 >= percentage >= 99:
        return "F"

if __name__ == '__main__':
    main()