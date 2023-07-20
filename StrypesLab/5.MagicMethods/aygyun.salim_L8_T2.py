import unittest
from aygyun.salim_L8_T1 import bisection



class TestBisection(unittest.TestCase):
    def test_finds_root(self):
        def f(x):
            return x*x*x - 2*x - 5

        self.assertAlmostEqual(bisection(1, 2, f), 1.768, places=3)
        self.assertAlmostEqual(bisection(0, 1, f), 0.791, places=3)

    def test_raises_type_error(self):
        with self.assertRaises(TypeError):
            bisection("a", 2, lambda x: x**2 - 1)

    def test_raises_value_error(self):
        with self.assertRaises(ValueError):
            bisection(1, 2, lambda x: x**2 + 1)
