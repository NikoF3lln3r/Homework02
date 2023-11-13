import unittest
from math_quiz import random_integer, random_math_operator, math_operation


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_math_operator(self):
        # test if random operator works properly
        for _ in range(1000): # test large number of random operators
            rand_operator = random_math_operator()
            self.assertTrue(rand_operator=="+" or rand_operator=="-" or rand_operator=="*")
        pass

    def test_math_operation(self):
        # some test cases to test the complete operation process
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (3, 2, '*', '3 * 2', 6),
            (4, 2, '-t', '4 - 2', 2)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, result = math_operation(num1, num2, operator)
            self.assertTrue(problem == expected_problem)
            self.assertTrue(result == expected_answer)
            pass

if __name__ == "__main__":
    unittest.main()
