import string
import random
import pyperclip

alphabets = string.ascii_letters
numbers = string.digits
special_char = string.punctuation

def get_length():
    while True:

        try:
            user_input_length = int(input("Enter your password's length:"))

            if user_input_length < 5:
                print("Your password is too short")

            else:
                return user_input_length

        except ValueError:
            print("Please enter numbers only.")

def get_choices():
    print("\nSelect all the character types you want in your password.")
    print("You can pick multiple options. Type the numbers separated by spaces (e.g., 1 2 3):\n")
    print("1. Letters (A-Z, a-z)")
    print("2. Numbers (0-9)")
    print("3. Special characters (!@#$...)")

    valid_choices = {"1", "2", "3"}

    while True:
        user_input_choice = input("Enter the numbers: ")
        user_input_choice = user_input_choice.split(" ")

        if all(c in valid_choices for c in user_input_choice):
            return user_input_choice

        else:
            print("Invalid selection.")

def generate_password(user_choice, user_length):
    password_chars = ""

    if "1" in user_choice:
        password_chars += alphabets

    if "2" in user_choice:
        password_chars += numbers

    if "3" in user_choice:
        password_chars += special_char

    password = ""

    for i in range(user_length):
        random_char = random.choice(password_chars)
        password += random_char

    return password

length = get_length()
choice = get_choices()
final_pass = generate_password(choice, length)
pyperclip.copy(final_pass)

print(f"Your final password is:{final_pass}. Password copied to clipboard")

