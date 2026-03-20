import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from prime_number import (
    sieve_primes,
    calculate_statistics,
    display_results,
    get_limit
)


class TestPrimeAnalyzer(unittest.TestCase):

    # --------------------------
    # Test prime generation
    # --------------------------
    def test_sieve_primes_basic(self):
        self.assertEqual(sieve_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_sieve_primes_edge_cases(self):
        self.assertEqual(sieve_primes(0), [])
        self.assertEqual(sieve_primes(1), [])
        self.assertEqual(sieve_primes(2), [2])

    def test_sieve_primes_small_range(self):
        self.assertEqual(sieve_primes(10), [2, 3, 5, 7])

    # --------------------------
    # Test statistics
    # --------------------------
    def test_calculate_statistics(self):
        primes = [2, 3, 5, 7, 11]
        stats = calculate_statistics(primes)

        self.assertEqual(stats["count"], 5)
        self.assertEqual(stats["smallest"], 2)
        self.assertEqual(stats["largest"], 11)
        self.assertEqual(stats["sum"], 28)

    def test_calculate_statistics_empty(self):
        stats = calculate_statistics([])

        self.assertEqual(stats["count"], 0)
        self.assertIsNone(stats["smallest"])
        self.assertIsNone(stats["largest"])
        self.assertEqual(stats["sum"], 0)

    # --------------------------
    # Test display output (HD+)
    # --------------------------
    def test_display_results_output(self):
        primes = [2, 3, 5]

        captured_output = StringIO()
        sys.stdout = captured_output

        display_results(primes)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Header check
        self.assertIn("Prime Number Analysis", output)

        # Prime list check
        self.assertIn("2 3 5", output)

        # Flexible spacing checks (important!)
        self.assertRegex(output, r"Total primes found:\s+3")
        self.assertRegex(output, r"Smallest prime:\s+2")
        self.assertRegex(output, r"Largest prime:\s+5")
        self.assertRegex(output, r"Sum of all primes:\s+10")

    def test_display_results_no_primes(self):
        primes = []

        captured_output = StringIO()
        sys.stdout = captured_output

        display_results(primes)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("None", output)
        self.assertRegex(output, r"Total primes found:\s+0")
        self.assertIn("N/A", output)

    # --------------------------
    # Test input validation
    # --------------------------
    @patch('builtins.input', side_effect=["-10", "0", "101", "abc", "25"])
    def test_get_limit_validation(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output

        result = get_limit()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        # Check error messages appeared
        self.assertIn("❌ Error: Number must be between 1 and 100.", output)
        self.assertIn("❌ Error: Please enter a valid integer.", output)

        # Final valid input
        self.assertEqual(result, 25)


if __name__ == "__main__":
    unittest.main()