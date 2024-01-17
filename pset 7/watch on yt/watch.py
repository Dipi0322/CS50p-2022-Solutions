import re


def main():
    print(parse(input("HTML: ")))


def parse(html):
    if "width" in html and "youtube" in html:
        new = re.sub(r"<iframe(?:\s+width=\"560\"\s+height=\"315\"\s+src=\")?(https?://)?(www\.)?youtube\.com/embed/", r"https://youtu.be/", html)

    elif "width" not in html and "youtube" in html and "iframe" in html:
        new = re.sub(r"^(<iframe )?(src=\")?(https?://)?(www\.)?youtube\.com/embed/", r"https://youtu.be/", html)

    elif "youtube" not in html or "iframe" not in html:
        return None

    new_url = ""
    for i in new:
        if i != '"':
            new_url += i
        elif i == '"':
            break
    return new_url

if __name__ == "__main__":
    main()
