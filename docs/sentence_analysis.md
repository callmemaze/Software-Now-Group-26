# Question 4 – Sentence Analysis Program

## 📌 Problem Description

This program analyzes a sentence by counting words, identifying the longest word, and applying transformations.

## 🧠 Approach

Steps:

1. Validate user input
2. Clean words (remove punctuation and numbers)
3. Count valid words
4. Find longest word
5. Generate transformations
6. Display results

## ⚙️ Key Functions

- clean_words(): Removes punctuation and ignores numbers
- count_words(): Counts valid words
- find_longest_word(): Finds longest word
- transform_sentence(): Applies transformations

## ⚠️ Assumptions

- Numbers (e.g., 26) are ignored
- Words with mixed characters (e.g., abc123) are kept
- Empty input is not allowed

## 🚀 Enhancements

- Handles real-world messy input
- Ignores numeric-only tokens
- Clean formatted output
- Modular design

## 🧪 Testing

- Tested sentences with punctuation
- Tested numeric inputs (ignored correctly)
- Tested empty input validation
- Verified transformations and output
