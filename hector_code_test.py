import unittest
from hector_code import *


class MyTest1(unittest.TestCase):
    def setUp(self):
        self.l1 = [[1, 2], [3, 4]]
        self.l2 = [[5, 6], [7, 8]]

    def test_init(self):
        m1 = Matrix(self.l1)
        self.assertEqual(m1.rows, [[1, 2], [3, 4]])
        self.assertEqual(m1.nrows, 2)
        self.assertEqual(m1.ncols, 2)

    def test_add(self):
        m1 = Matrix(self.l1)
        m2 = Matrix(self.l2)
        m3 = m1 + m2
        self.assertEqual(m3.rows, [[6, 8], [10, 12]])
        self.assertEqual(m3.nrows, 2)
        self.assertEqual(m3.ncols, 2)

    def test_sub(self):
        m1 = Matrix(self.l1)
        m2 = Matrix(self.l2)
        m3 = m1 - m2
        self.assertEqual(m3.rows, [[-4, -4], [-4, -4]])
        self.assertEqual(m3.nrows, 2)
        self.assertEqual(m3.ncols, 2)

    def test_prod(self):
        m1 = Matrix(self.l1)
        m2 = Matrix(self.l2)
        m3 = m1.prod(m2)
        print m1
        print m2
        print m3
        self.assertEqual(m3.rows, [[19, 22], [43, 50]])
        self.assertEqual(m3.nrows, 2)
        self.assertEqual(m3.ncols, 2)

    def test_prod(self):
        m1 = Matrix(self.l1)
        matrix_string = str(m1)
        self.assertEqual(matrix_string[0], "|")
        self.assertEqual(matrix_string[1], " ")
        self.assertEqual(matrix_string[2], "1")
        self.assertEqual(matrix_string[3], " ")
        self.assertEqual(matrix_string[4], "2")
        self.assertEqual(matrix_string[5], " ")
        self.assertEqual(matrix_string[6], "|")

if __name__ == '__main__':
    unittest.main()
