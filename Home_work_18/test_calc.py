import unittest
from calc import add, minus, umnojenie, delenie, sqrt, pow_


class CalcTest(unittest.TestCase):

    def test_add(self):
        print('Hello from test_add')
        self.assertEqual(add(2, 2), 4)

    def test_minus(self):
        print('hello from minus')
        self.assertEqual(minus(8, 6), 2)

    def test_umnojenie(self):
        self.assertEqual(umnojenie(2, 2), 4)

    def test_delenie(self):
        self.assertEqual(delenie(20, 5), 4)


class CalcExTest(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(sqrt(4), 2)

    def test_pow(self):
        self.assertEqual(pow_(2, 3), 8)


if __name__ == '__main__':
    calc_test = CalcTest()
    test_suit = unittest.TestSuite()
    test_suit.addTest(calc_test)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suit)
