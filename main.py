import random
import string

password_length = 6
password_chars = ""

alphabets = string.ascii_letters
numbers = string.digits
spec_chars = string.punctuation

while True:
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

password = []
for i in range(password_length):

    random_char = random.choice(password_chars)
    password.append(random_char)

password = "".join(password)
print(f"Your password is: {password}")




# Access Token: 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