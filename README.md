# 🔐 Password Generator (Python)

A simple and interactive command-line password generator written in Python.  
It allows users to choose what types of characters to include (letters, digits, special characters), and generates a random password of a specified length. The generated password is automatically copied to your clipboard.

---

## 📦 Features

- User-friendly terminal prompts
- Supports:
  - ✅ Letters (A-Z, a-z)
  - ✅ Numbers (0-9)
  - ✅ Special characters (!@#$...etc.)
- Ensures password length is at least 5 characters
- Copies generated password to clipboard (via `pyperclip`)
- Allows multiple character type selection

---

## 🛠 Requirements

- Python 3.x
- [pyperclip](https://pypi.org/project/pyperclip/)

Install `pyperclip` with:

```bash
pip install pyperclip
```

---

## 🚀 How to Use

Run the script in your terminal:

```bash
python password_generator.py
```

Follow the prompts:

1. Enter the desired password length (must be 5 or more).
2. Choose which types of characters to include:
   - Enter numbers like: `1 2 3`
   - `1` → Letters (A-Z, a-z)
   - `2` → Numbers (0-9)
   - `3` → Special characters

Once the password is generated:
- It will be printed in the terminal.
- It will be automatically copied to your clipboard.

---

## ✏️ Example

```
Enter your password's length: 12

Select all the character types you want in your password.
You can pick multiple options. Type the numbers separated by spaces (e.g., 1 2 3):

1. Letters (A-Z, a-z)
2. Numbers (0-9)
3. Special characters (!@#$...)

Enter the numbers: 1 2 3

Your final password is: V9@pwb!K3#az. Password copied to clipboard
```

---

## 📌 Notes

- This generator currently does **not guarantee** at least one character from each selected category will appear in every password. (You can add that if desired.)
- To make the password regeneration feature or enforce character category presence, check out possible improvements in the logic.

---

## 📄 License

This project is open source and free to use. No license specified.