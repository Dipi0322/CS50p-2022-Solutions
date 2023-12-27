from fractions import Fraction

while True:
    try:
        x = input("Fraction:")
        num,denom = x.split("/")
        if int(num) > int(denom):
            print("Invalid prompt")
            continue
        z = Fraction(x)
        y = z*100
        y = round(y)
        if y > 1 and y < 99:
            print(f"{y}%")
        elif y <= 1:
            print("E")
        elif 99 <= y <= 100:
            print("F")
    except (ValueError,ZeroDivisionError):
        pass
    else:
        break