import unittest
from hector_code import *


class MyTest1(unittest.TestCase):
    def setUp(self):
        self.l1 = [[1, 2], [3, 4]]

    def test_init(self):
        m1 = Matrix(self.l1)
        self.assertEqual(m1.rows, [[1, 2], [3, 4]])
        self.assertEqual(m1.nrows, 2)
        self.assertEqual(m1.ncols, 2)

    def test_add(self):
        pass
# make a lot of tests
if __name__ == '__main__':
    unittest.main()

