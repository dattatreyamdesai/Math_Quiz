import unittest
from math_quiz import generate_random_integer, generate_random_operator, perform_operation

class TestMathGame(unittest.TestCase):


    def testcase1_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def testcase2_generate_random_operator(self):
        # To test if the generated operator is one of the specified operators
        operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            rand_operator = generate_random_operator()
            self.assertTrue(rand_operator in operators)

    def testcase3_perform_operation(self):
        # To test if the operations are performing according to the function
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 6, '*', '4 * 6', 24),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = perform_operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem, "The test case if failed due to problem mismatch")
            self.assertEqual(answer, expected_answer, "The test case is failed due to answer mismatch")

if __name__ == "__main__":
    unittest.main()
