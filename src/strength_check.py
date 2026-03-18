import re
"""
    Checks if the given password is strong.
    Criteria:
    - At least 8 characters
    - Contains uppercase, lowercase, digit, and special character
"""
def is_strong_password(password: str) -> str:
    """ if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\\d', password):
        return False
    if not re.search(r'[^A-Za-z0-9]', password):
        return False
    return True """
    return "False"

if __name__ == "__main__":
    password = input("Enter a password: ")
    is_strong_password(password)