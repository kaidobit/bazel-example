import unittest

from projects.calculator_lib.calculator_lib import Calculator


class Test(unittest.TestCase):
    def test_add(self):
        underTest = Calculator()
        self.assertEquals(underTest.add(1, 1), 2)


if __name__ == '__main__':
    unittest.main()
