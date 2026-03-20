# Question 2 – Prime Number Analyzer

## 📌 Problem Description

This program finds all prime numbers up to a user-defined limit (1–100) and displays statistics.

## 🧠 Approach

The Sieve of Eratosthenes algorithm is used for efficient prime generation.

Steps:

1. Generate primes using sieve
2. Compute statistics (count, min, max, sum)
3. Display formatted results

## ⚙️ Key Functions

- sieve_primes(): Generates primes efficiently
- calculate_statistics(): Computes required statistics
- display_results(): Outputs formatted results

## ⚠️ Assumptions

- Input range is restricted to 1–100
- If no primes exist, outputs are handled gracefully

## 🚀 Enhancements

- Efficient algorithm (O(n log log n))
- Clean formatted output
- Robust input validation

## 🧪 Testing

- Edge cases: 0, 1, empty prime list
- Input validation (negative, >100, non-integer)
- Output tested using captured stdout
