import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from strength_check import evaluate_password, calculate_entropy

class TestPasswordChecker(unittest.TestCase):

    def test_weak_short(self):
        strength, _ = evaluate_password("abc")
        self.assertEqual(strength, "Weak")

    def test_common_password(self):
        strength, _ = evaluate_password("password123")
        self.assertEqual(strength, "Weak") # Weak beacuse it's a common password it's in the common password list

    def test_medium_password(self):
        strength, _ = evaluate_password("woollies1")
        self.assertEqual(strength, "Medium") 

    def test_strong_password(self):
        strength, _ = evaluate_password("Woolworths@123!")
        self.assertEqual(strength, "Strong")  
        

    def test_entropy_increases(self):
        e1 = calculate_entropy("abc")
        e2 = calculate_entropy("abc123ABC!")
        self.assertGreater(e2, e1)


if __name__ == "__main__":
    unittest.main()