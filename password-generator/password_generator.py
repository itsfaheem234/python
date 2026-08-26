import random
import string


def generate_password(length, include_numbers, include_symbols):
    characters = string.ascii_letters

    if include_numbers:
        characters += string.digits

    if include_symbols:
        characters += string.punctuation

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


print("===== PASSWORD GENERATOR =====")

try:
    length = int(input("enter password length: "))

    if length <= 0:
        print("password length must be greater than 0.")

    else:
        numbers = input("include numbers? (y/n): ").lower()
        symbols = input("include symbols? (y/n): ").lower()

        include_numbers = numbers == "y"
        include_symbols = symbols == "y"

        password = generate_password(
            length,
            include_numbers,
            include_symbols
        )

        print("\ngenerated password:")
        print(password)

except ValueError:
    print("please enter a valid number.")
