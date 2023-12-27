grocery = {}

try:
    while True:
        item = input("")
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1

except EOFError:
    pass

for item in sorted(grocery):
    print(grocery[item],item.upper())