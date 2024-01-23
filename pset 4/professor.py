import random


def main():
    calculate()


def get_level():
    while True:
        try:
            level = int(input("Enter level (1, 2, or 3): "))
            if 1 <= level <= 3:
                break
            else:
                raise ValueError
        except ValueError:
            pass
    return level


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return [x,y]

def calculate():
    i = get_level()
    score = 0
    for _ in range(10):
        integers = generate_integer(i)
        x = integers[0]
        y = integers[1]
        z = x + y
        error = 0
        while True:
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans == z:
                    score += 1
                    break
                else:
                    error += 1
                    raise ValueError
            except ValueError:
                if error < 3:
                    print("EEE")
                    continue
                elif error == 3:
                    print(z)
                    break

    print(score)

if __name__ == "__main__":
    main()
