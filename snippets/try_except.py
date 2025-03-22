def get_integer_from_input():
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        print(f"You entered the number: {number}")
    except Exception as e:
        print(f"An error occurred: {e}")

get_integer_from_input()

        