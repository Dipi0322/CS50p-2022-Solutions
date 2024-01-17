import validators

email = input("What's your email address? ")

match = validators.email(email)

if match:
    print("valid")
else:
    print("invalid")