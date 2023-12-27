def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    p = ",.-!?"
    # no ., space, punctuation
    for _ in s:
        if _ in p:
            return False

    # maximum 6 characters & minimum 2 characters
    if len(s) > 6 or len(s) < 2:
        return False

    elif 2 <= len(s) <= 6:
    # must start with at least two letters
        for i in range(0,1):
            x = ord(s[i])
            if 65 <= x <= 90:
                for j in range(2,len(s)):
                    # numbers can't be in middle
                    y = ord(s[j])
                    if 65 <= y <= 90:
                        z= s[-1]
                        b = s[-2]
                        k= ord(z)
                        j = ord(b)
                        if 65 <= k <= 90:
                            continue

                    elif 48 <= y <= 57:
                        if j == 2 and s[j] == "0":
                            return False

                        z = s[-1]
                        e = s[-2]
                        k = ord(z)
                        f = ord(e)
                        if 48 <= k <= 57:
                            if 48 <= f <= 57:
                                break
                            elif 65 <= f <= 90:
                                return False

                        elif 65 <= k <= 90:
                            return False

    return True


main()
