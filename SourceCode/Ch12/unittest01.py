import unittest

# Function to be tested
def get_average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    return total / len(numbers)


# Define Test Cases
class TestGetAverage(unittest.TestCase):

    def test_average_of_positive_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        result = get_average(numbers)
        self.assertEqual(result, 3)

    def test_average_of_negative_numbers(self):
        numbers = [-1, -2, -3, -4, -5]
        result = get_average(numbers)
        self.assertEqual(result, -3)

    def test_average_of_empty_list(self):
        numbers = []
        result = get_average(numbers)
        self.assertIsNone(result)

    def test_average_of_single_number(self):
        numbers = [10]
        result = get_average(numbers)
        self.assertEqual(result, 10)

    def test_average_of_zero_numbers(self):
        numbers = [0, 0, 0, 0, 0]
        result = get_average(numbers)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
