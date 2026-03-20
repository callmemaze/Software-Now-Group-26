"""
Strength Checker 
Features:
• Regex-based validation
• Entropy calculation
• Character diversity checks
• Common password blacklist
• Dictionary word detection
• Password cracking time estimation

Group Name: Sydney Group 26
Group Members:
Dipesh Shrestha - S394865
Aryan Shrestha - S396160
Priyanka Shakya - S396306
Nahida Aktar - S391730

"""

import re
import math

# Common weak passwords
COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty",
    "abc123", "password123", "admin", "letmein"
}

# Simple dictionary words 
COMMON_WORDS = {
    "hello", "welcome", "admin", "user", "login", "test"
}

def get_password() -> str:
    while True:
        password = input("Enter your password: ").strip()
        if not password:
            print("❌ Error: Password cannot be empty.")
            continue
        return password

# Regex checks
def has_digit(p: str) -> bool:
    return bool(re.search(r"\d", p))

def has_uppercase(p: str) -> bool:
    return bool(re.search(r"[A-Z]", p))

def has_lowercase(p: str) -> bool:
    return bool(re.search(r"[a-z]", p))

def has_symbol(p: str) -> bool:
    return bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", p))

# Weakness detection
def is_common_password(p: str) -> bool:
    return p.lower() in COMMON_PASSWORDS

def contains_dictionary_word(p: str) -> bool:
    p_lower = p.lower()
    return any(word in p_lower for word in COMMON_WORDS)

# Entropy calculation
def calculate_entropy(p: str) -> float:
    charset = 0
    if has_lowercase(p):
        charset += 26
    if has_uppercase(p):
        charset += 26
    if has_digit(p):
        charset += 10
    if has_symbol(p):
        charset += 32

    if charset == 0:
        return 0

    return len(p) * math.log2(charset)

# Crack time estimation
def estimate_crack_time(entropy: float) -> str:
    """
    Estimate brute-force cracking time assuming 1e10 guesses/sec
    """
    guesses_per_second = 1e10
    total_guesses = 2 ** entropy
    seconds = total_guesses / guesses_per_second

    if seconds < 60:
        return "seconds"
    elif seconds < 3600:
        return "minutes"
    elif seconds < 86400:
        return "hours"
    elif seconds < 31536000:
        return "days"
    else:
        return "years"

# Strength evaluation
def evaluate_password(p: str) -> tuple[str, float]:
    length = len(p)
    entropy = calculate_entropy(p)

    # Immediate weak conditions
    if length < 6 or is_common_password(p):
        return "Weak", entropy

    if contains_dictionary_word(p):
        return "Weak", entropy

    # Medium rules
    if 6 <= length <= 10:
        if has_digit(p):
            return "Medium", entropy
        return "Weak", entropy

    # Strong rules
    if length > 10:
        if has_digit(p) and has_uppercase(p):
            return "Strong", entropy
            
    return "Weak", entropy


# display result
def display_result(password: str, strength: str, entropy: float):
    crack_time = estimate_crack_time(entropy)

    print("\n🔐 Password Analysis")
    print("-" * 40)
    print(f"Strength        : {strength}")
    print(f"Entropy         : {entropy:.2f} bits")
    print(f"Crack Time      : {crack_time}")

    # Feedback
    print("\n💡 Suggestions:")
    if strength == "Weak":
        print("• Use at least 10+ characters")
        print("• Include uppercase, digits, and symbols")
        print("• Avoid common words or patterns")
    elif strength == "Medium":
        print("• Add symbols (!@#$...)")
        print("• Increase length for better security")
    else:
        print("• Excellent password! Keep it secure ✅")

if __name__ == "__main__":
    password = get_password()
    strength, entropy = evaluate_password(password)
    display_result(password, strength, entropy)