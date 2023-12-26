user_input = input("Customer: ")

user_input = user_input.strip().lower()

if user_input.startswith("hello"):
    print("$0")

elif user_input.startswith("h"):
    print("$20")

else:
    print("$100")