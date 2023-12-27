print("Amount Due: 50")

a = 50

while a <= 50:

        i = int(input("Insert Coin: "))
        if i == 5 or i == 10 or i == 25:
            a = a-i
            if a != 0 and a > 0:
                print(f"Amount Due: {a}")
            elif a == 0:
                print(f"Change Owed: {a}")
                break
            elif a < 0:
                a = a * -1
                print(f"Change Owed: {a}")
                break
        else:
            print("Amount Due: 50")
