from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
x = figlet.getFonts()

if len(sys.argv) == 1:
    s = input("")
    y = random.choice(x)
    f = Figlet(font=y)
    print(f.renderText(s))

elif len(sys.argv) == 2:
    sys.exit("Invalid")

elif len(sys.argv) > 2:
    if sys.argv[1] in ["-f","--font"] and sys.argv[2] in x:
        s = input("")
        f = Figlet(font= sys.argv[2])
        print(f.renderText(s))
    elif sys.argv[1] not in ["-f","--font"] or sys.argv[2] not in x:
        sys.exit("Invalid")