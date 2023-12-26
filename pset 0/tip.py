def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    new = ""
    for i in range(1,len(d)):
        new += d[i]
    return float(new)

def percent_to_float(p):
    p = p.replace("%","")
    p2 = float(p) / 100
    return p2

main()