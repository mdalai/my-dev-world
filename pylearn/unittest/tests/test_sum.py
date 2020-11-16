import unittest
from fractions import Fraction
from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1,2,3]
        result = sum.sum(data)
        self.assertEqual(result, 2, "Failed to get Sum of integers")
    
    def test_list_fraction(self):
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum.sum(data)
        self.assertEqual(result, Fraction(9,10))



if __name__ == '__main__':
    unittest.main()