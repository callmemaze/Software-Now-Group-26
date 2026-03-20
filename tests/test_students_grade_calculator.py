import unittest
from unittest.mock import patch
from io import StringIO
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from students_grade_calculator import (
    Student, calculate_grade, score_statistics,
    students_grade_calculator, display_results, get_input
)


class TestQuestion3HDPlus(unittest.TestCase):

    def setUp(self):
        self.students = [
            Student("Alice", 78, "D"),
            Student("Bob", 92, "HD"),
            Student("Carol", 45, "F")
        ]

    # --------------------------
    # Grade tests
    # --------------------------
    def test_calculate_grade_boundaries(self):
        self.assertEqual(calculate_grade(85), "HD")
        self.assertEqual(calculate_grade(75), "D")
        self.assertEqual(calculate_grade(65), "C")
        self.assertEqual(calculate_grade(50), "P")
        self.assertEqual(calculate_grade(0), "F")

    # --------------------------
    # Statistics tests
    # --------------------------
    def test_score_statistics(self):
        avg, highest, lowest = score_statistics(self.students)

        self.assertAlmostEqual(avg, (78 + 92 + 45) / 3)
        self.assertEqual(highest.name, "Bob")
        self.assertEqual(lowest.name, "Carol")

    def test_empty_statistics(self):
        with self.assertRaises(ValueError):
            score_statistics([])

    # --------------------------
    # Input tests
    # --------------------------
    @patch('builtins.input', side_effect=[
        "3",
        "Alice", "78",
        "Bob", "92",
        "Carol", "45"
    ])
    def test_students_input(self, mock_input):
        students = students_grade_calculator()

        self.assertEqual(len(students), 3)
        self.assertEqual(students[1].grade, "HD")

    @patch('builtins.input', side_effect=["101", "90"])
    def test_invalid_score(self, mock_input):
        captured = StringIO()
        sys.stdout = captured

        result = get_input("Enter: ", 0, 100)

        sys.stdout = sys.__stdout__

        self.assertEqual(result, 90)
        self.assertIn("Scores must be between", captured.getvalue())

    @patch('builtins.input', side_effect=["abc", "50"])
    def test_non_integer(self, mock_input):
        captured = StringIO()
        sys.stdout = captured

        result = get_input("Enter: ", 0, 100)

        sys.stdout = sys.__stdout__

        self.assertEqual(result, 50)
        self.assertIn("Invalid input", captured.getvalue())

    @patch('builtins.input', side_effect=[
        "3",
        "", "Alice", "78",
        "Bob123", "Bob", "92",
        "Carol", "45"
    ])
    def test_invalid_name(self, mock_input):
        students = students_grade_calculator()
        self.assertEqual(students[0].name, "Alice")
        self.assertEqual(students[1].name, "Bob")

    @patch('builtins.input', side_effect=[
        "2", "3",
        "Alice", "80",
        "Bob", "70",
        "Carol", "60"
    ])
    def test_invalid_student_count(self, mock_input):
        students = students_grade_calculator()
        self.assertEqual(len(students), 3)

    # --------------------------
    # Output test
    # --------------------------
    def test_display_results(self):
        captured = StringIO()
        sys.stdout = captured

        display_results(self.students)

        sys.stdout = sys.__stdout__

        output = captured.getvalue()

        self.assertIn("Name", output)
        self.assertIn("Average Score", output)
        self.assertIn("Bob", output)
        self.assertIn("Carol", output)


if __name__ == "__main__":
    unittest.main()