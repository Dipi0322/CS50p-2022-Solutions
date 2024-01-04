def main():
    greeting = input("")
    print(f"${value(greeting)}")

def value(greeting):
    value0 = "Hellohello"
    if greeting in value0:
        return 0
    elif greeting[0] == "h" or greeting[0] == "H":
        return 20
    elif greeting[0] != "h" or greeting[0] != "H":
        return 100

if __name__ == '__main__':
    main()