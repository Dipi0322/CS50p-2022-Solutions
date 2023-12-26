def main():
    # Get user input

    user_input = input("Enter an emoji: ")

    # Set user input as result

    result = convert(user_input)

    # Publish result

    print("Converted to: ", result)

def convert(user_input):
    # Replace :) with 🙂

    user_input = user_input.replace(":)", "🙂")

    # Replace :( with 🙁

    user_input = user_input.replace(":(", "🙁")

    # Return str

    return user_input

main()
