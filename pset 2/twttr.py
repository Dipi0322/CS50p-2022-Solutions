user_input = input("Input: ")
print("Output: ", end="")

for letter in user_input:
    if not letter.lower() in ["a","e","i","o","u"]:
        print(letter, end="")

print()