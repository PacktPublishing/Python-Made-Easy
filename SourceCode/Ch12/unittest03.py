import unittest

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

class PrimeTestCase(unittest.TestCase):
    def test_prime_number(self):
        self.assertTrue(is_prime(7))

    def test_non_prime_number(self):
        self.assertFalse(is_prime(10))

    def test_negative_number(self):
        self.assertFalse(is_prime(-5))

    def test_zero(self):
        self.assertFalse(is_prime(0))

    def test_one(self):
        self.assertFalse(is_prime(1))

if __name__ == '__main__':
    unittest.main()
