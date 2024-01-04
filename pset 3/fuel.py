while True:
    try:
        fraction = input("x/y: ")
        num,denom = fraction.split("/")
        num,denom = int(num),int(denom)

        percentage = round((num/denom)*100)

        if 1 < percentage < 99:
            print(f"{percentage}%")
            break
        elif percentage <= 1:
            print("E")
            break
        elif 100 >= percentage >= 99:
            print("F")
            break

    except (ValueError,ZeroDivisionError):
        pass
