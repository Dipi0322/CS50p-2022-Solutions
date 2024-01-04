def main():
    s = input("")
    print(shorten(s))


def shorten(word):
    vowel = "aeiouAEIOU"
    new = ""

    for i in word:
        if i in vowel:
            continue
        elif i not in vowel:
            new += i

    return new


if __name__ == '__main__':
    main()