"""
Question 4 - Sentence Analysis Program

This program:
- Accepts a sentence from the user
- Calculates total words
- Finds the longest word
- Displays multiple case transformations
- Displays the reversed sentence

Group Name: Sydney Group 26
Group Members:
Dipesh Shrestha - S394865
Aryan Shrestha - S396160
Priyanka Shakya - S396306
Nahida Aktar - S391730

"""

import re
import string


def get_valid_input():
    """
    Prompt user until a valid non-empty sentence is entered.
    Returns a cleaned sentence.
    """
    while True:
        user_input = input("Enter a sentence: ").strip()

        # Error handling: empty input
        if not user_input:
            print("❌ Error: Input cannot be empty. Please try again.\n")
            continue

        return user_input

def clean_words(sentence):
    """
    Splits sentence into words and removes punctuation.
    Returns a list of clean words.
    """
    words = sentence.split()

    # Remove punctuation from each word
    cleaned = []
    for word in words:
        w = word.strip(string.punctuation)
        w = re.sub(r"\d+", "", w)
        if w: # Ignore numbers
            cleaned.append(w)
    return cleaned

def count_words(words):
    """Return total number of words."""
    return len(words)


def find_longest_word(words):
    """
    Finds the longest word.
    If multiple words share the same max length,
    returns the first occurrence.
    """
    if not words:
        return None, 0

    longest = max(words, key=len)
    return longest, len(longest)

def transform_sentence(sentence):
    """
    Returns different transformations of the sentence.
    """
    return {
        "uppercase": sentence.upper(),
        "lowercase": sentence.lower(),
        "titlecase": sentence.title(),
        "reversed": sentence[::-1]
    }

def display_results(total_words, longest_word, length, transformations):
    """
    Displays results in a clean formatted way.
    """
    print("\n📊 Analysis Results")
    print("-" * 40)
    print(f"Total words   : {total_words}")
    if longest_word:
        print(f"Longest word  : {longest_word.capitalize()} ({length} letters)")
    else:
        print("Longest word  : None")
    print("\n🔤 Transformations")
    print("-" * 40)
    print(f"Uppercase     : {transformations['uppercase']}")
    print(f"Lowercase     : {transformations['lowercase']}")
    print(f"Title case    : {transformations['titlecase']}")
    print(f"Reversed      : {transformations['reversed']}")

# Run the program
if __name__ == "__main__":
    sentence = get_valid_input()
    words = clean_words(sentence)
    total_words = count_words(words)
    longest_word, length = find_longest_word(words)
    transformations = transform_sentence(sentence)
    display_results(total_words, longest_word, length, transformations)