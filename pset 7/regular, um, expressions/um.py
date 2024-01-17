def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    count = 0

    for i in range(len(s)):
        if s[i] == "u" and i == 0 and (i+1) == (len(s)-1):
            if s[i+1] == "m":
                count += 1

        elif s[i] == "u" and i != (len(s)-2) and i != 0:
            if s[i+1] == "m":
                x = ord(s[i-1])
                y = ord(s[i+2])

                if 97 <= x <= 122 or 97 <= y <= 122:
                    continue
                else:
                    count += 1

            else:
                continue

        elif s[i] == "u" and i == (len(s)-2):
            if s[i+1] == "m":
                x = ord(s[i-1])

                if 97 <= x <= 122:
                    continue
                else:
                    count += 1

            else:
                continue

        elif s[i] == "u" and i == 0:
            if s[i+1] == "m":
                y = ord(s[i+2])

                if 97 <= y <= 122:
                    continue
                else:
                    count += 1

            else:
                continue

    return count

if __name__ == "__main__":
    main()