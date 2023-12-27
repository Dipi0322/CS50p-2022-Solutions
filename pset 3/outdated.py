month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")

    if "/" in date:
        try:
            mm,dd,yyyy = date.split("/")
            if int(mm) <= 12 and int(dd) <= 31:
                if 1 <= int(mm) <= 9 and 1 <= int(dd) <= 9:
                    print(f"{yyyy}-0{mm}-0{dd}".replace(" ",""))
                    break
                elif 10 <= int(mm) <= 12 and 10 <= int(dd) <= 31:
                    print(f"{yyyy}-{mm}-{dd}")
                    break
                elif 10 <= int(mm) <= 12 and 1 <= int(dd) <= 9:
                    print(f"{yyyy}-{mm}-0{dd}")
                    break
                elif 1 <= int(mm) <= 9 and 10 <= int(dd) <= 31:
                    print(f"{yyyy}-0{mm}-{dd}")
                    break
        except ValueError:
            pass

    elif "," in date:
        try:
            temp1,yyyy = date.split(", ")
            mm,dd = temp1.split(" ")
            mm = month.index(mm)+1
            if int(mm) <= 12 and int(dd) <= 31:
                if 1 <= int(mm) <= 9 and 1 <= int(dd) <= 9:
                    print(f"{yyyy}-0{mm}-0{dd}".replace(" ",""))
                    break
                elif 10 <= int(mm) <= 12 and 10 <= int(dd) <= 31:
                    print(f"{yyyy}-{mm}-{dd}")
                    break
                elif 10 <= int(mm) <= 12 and 1 <= int(dd) <= 9:
                    print(f"{yyyy}-{mm}-0{dd}")
                    break
                elif 1 <= int(mm) <= 9 and 10 <= int(dd) <= 31:
                    print(f"{yyyy}-0{mm}-{dd}")
                    break
        except ValueError:
            pass
