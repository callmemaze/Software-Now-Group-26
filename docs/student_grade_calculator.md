# Question 3 – Student Grade Calculator

## 📌 Problem Description

This program collects student names and scores, assigns grades, and displays summary statistics.

## 🧠 Approach

Steps:

1. Collect validated input
2. Assign grades based on score ranges
3. Store data using a dataclass
4. Compute statistics (average, highest, lowest)
5. Display results in table format

## ⚙️ Key Functions

- calculate_grade(): Assigns grade based on score
- students_grade_calculator(): Collects input
- score_statistics(): Computes summary statistics

## ⚠️ Assumptions

- Scores are between 0–100
- Names contain only letters and spaces
- Minimum 3 students required

## 🚀 Enhancements

- Use of dataclass for structured data
- Dynamic table formatting
- Input validation and error handling

## 🧪 Testing

- Tested grade boundaries
- Tested empty student list
- Mocked user input
- Verified formatted output
