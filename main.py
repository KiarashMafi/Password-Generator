import random
import string


def generate_password():
    password_length = 0
    password_chars = ""
    alphabets = string.ascii_letters
    numbers = string.digits
    spec_chars = string.punctuation

    while True:
        try:
            password_length = int(input("How many characters do you want in your password? "))

            if password_length < 5:
                print("Your password should be at least 5 characters Long.")

            else:
                break

        except:
            print("Please enter numbers only.")

    while True:
        try:
            choice = int(input("Pick a number: "))

            if choice == 1:
                password_chars += alphabets

            elif choice == 2:
                password_chars += numbers

            elif choice == 3:
                password_chars += spec_chars

            elif choice == 4:
                break

            else:
                print("Error: please pick a number from 1 to 4!")

        except:
            print("Please enter numbers only.")

    password = []
    for i in range(password_length):
        random_char = random.choice(password_chars)
        password.append(random_char)

    password = "".join(password)
    return password


random_pass = generate_password()
print(random_pass)
