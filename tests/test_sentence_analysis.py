import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from sentence_analysis import (
    get_valid_input,
    clean_words,
    count_words,
    find_longest_word,
    transform_sentence,
    display_results
)


class TestSentenceAnalysis(unittest.TestCase):

    # --------------------------
    # Input validation
    # --------------------------
    @patch('builtins.input', side_effect=["", "   ", "Hello world"])
    def test_get_valid_input(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output

        result = get_valid_input()

        sys.stdout = sys.__stdout__
        self.assertEqual(result, "Hello world")

    # --------------------------
    # Clean words
    # --------------------------
    def test_clean_words_basic(self):
        sentence = "Hello, world! 123 test."
        self.assertEqual(clean_words(sentence), ["Hello", "world", "test"])

    def test_numbers_are_ignored(self):
        sentence = "I am 26 years old"
        words = clean_words(sentence)

        self.assertEqual(words, ["I", "am", "years", "old"])
        self.assertEqual(count_words(words), 4)

        longest, length = find_longest_word(words)
        self.assertEqual(longest, "years")
        self.assertEqual(length, 5)

    def test_numbers_with_punctuation(self):
        sentence = "Hello!!! I have 2 apples, 10 bananas."
        words = clean_words(sentence)

        self.assertEqual(words, ["Hello", "I", "have", "apples", "bananas"])

    def test_numbers_inside_words(self):
        sentence = "abc123 test456"
        self.assertEqual(clean_words(sentence), ["abc123", "test456"])

    # --------------------------
    # Count words
    # --------------------------
    def test_count_words(self):
        self.assertEqual(count_words(["a", "b", "c"]), 3)
        self.assertEqual(count_words([]), 0)

    # --------------------------
    # Longest word
    # --------------------------
    def test_find_longest_word(self):
        words = ["cat", "elephant", "dog"]
        word, length = find_longest_word(words)

        self.assertEqual(word, "elephant")
        self.assertEqual(length, 8)

    def test_find_longest_word_empty(self):
        word, length = find_longest_word([])
        self.assertIsNone(word)
        self.assertEqual(length, 0)

    # --------------------------
    # Transformations
    # --------------------------
    def test_transform_sentence(self):
        result = transform_sentence("Hello World")

        self.assertEqual(result["uppercase"], "HELLO WORLD")
        self.assertEqual(result["lowercase"], "hello world")
        self.assertEqual(result["titlecase"], "Hello World")
        self.assertEqual(result["reversed"], "dlroW olleH")

    # --------------------------
    # Display results
    # --------------------------
    def test_display_results_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        display_results(
            3,
            "elephant",
            8,
            {
                "uppercase": "HELLO",
                "lowercase": "hello",
                "titlecase": "Hello",
                "reversed": "olleH"
            }
        )

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Analysis Results", output)
        self.assertRegex(output, r"Total words\s*:\s*3")
        self.assertIn("Elephant (8 letters)", output)

    def test_display_results_no_words(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        display_results(0, None, 0, {
            "uppercase": "",
            "lowercase": "",
            "titlecase": "",
            "reversed": ""
        })

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertRegex(output, r"Total words\s*:\s*0")
        self.assertIn("Longest word  : None", output)


if __name__ == "__main__":
    unittest.main()