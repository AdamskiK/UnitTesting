# import
from fractions import Fraction
import unittest
from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(2, 4), Fraction(2, 4), Fraction(3, 6)]
        result = sum(data)
        self.assertEqual(result, 1.5)

    def test_bad_type(self):
        data = [1, 2]

        # a code syntax for python 2
        self.assertRaises(TypeError, sum(data))

        # a code syntax for python 2
        # with self.assertRaises(TypeError):
        #
        #     sum(data)


if __name__ == '__main__':
    unittest.main()
