import unittest
from F87134_L9_T1 import *


class BisectionTest(unittest.TestCase):
    def test_bisection_should_throw_when_no_solution(self):
        def fake(x):
            return x ** 2 - 3 * x + 4

        self.assertRaises(ValueError, bisection, 0, 10, fake)

    
    def test_bisection_should_find_solution(self):
        def fake(x):
            return x * x * x + 3 * x - 5

        expected = 1.15417480469
        actual = bisection(0, 10, fake)

        self.assertAlmostEqual(expected, actual)

    
    def test_get_interval_should_throw_when_a_is_not_number(self):
        self.assertRaises(ValueError, get_interval, 'a', '10.0')

    
    def test_get_interval_should_throw_when_b_is_not_number(self):
        self.assertRaises(ValueError, get_interval, '10.0', 'b')

    
    def test_get_interval_should_parse_input(self):
        expected_a, expected_b = 0.0, 10.0
        actual_a, actual_b = get_interval('0.0', '10.0')

        self.assertItemsEqual([expected_a, expected_b], [actual_a, actual_b])



if __name__ == '__main__':
    unittest.main()