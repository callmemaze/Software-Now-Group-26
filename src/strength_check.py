import re
password = input("Enter your password: ")

length = len(password)
has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)

if length < 6:
    print("Weak password")
elif 6 <= length <= 10 and has_digit:
    print("Medium password")
elif length > 10 and has_digit and has_upper:
    print("Strong password")
else:
    print("Weak password")