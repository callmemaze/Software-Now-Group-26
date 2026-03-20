# Question 1 – Password Strength Checker

## 📌 Problem Description

This program evaluates the strength of a user-entered password based on length and character composition.

## 🧠 Approach

The program uses rule-based validation:

- The program checks against a list of **commonly used passwords** and automatically classifies them as Weak.
- Weak: < 6 characters and common words and password
- Medium: 6–10 characters with at least one digit
- Strong: > 10 characters with at least one digit and uppercase letter

Regex and helper functions are used to detect digits and uppercase letters.

## ⚙️ Key Functions

- evaluate_password(): Determines password strength
- has_digit(): Checks for numeric characters
- has_uppercase(): Checks for uppercase letters
- is_common_password(): Checks against a predefined list of weak passwords

## ⚠️ Assumptions

- Input is treated as a plain string
- Empty input is rejected
- Special characters are optional
- Common passwords (e.g., "password", "123456") are always considered weak

## 🚀 Enhancements

- Regex-based validation
- Entropy-based strength estimation (advanced version)
- Clean modular design
- Detection of common weak passwords
- Suggestion for weak and medium passwords

## 🧪 Testing

- Tested weak, medium, and strong passwords
- Edge cases: empty input, short passwords
