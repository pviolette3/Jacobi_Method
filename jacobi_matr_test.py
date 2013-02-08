import jacobi_matr
import unittest
from numpy.testing import assert_array_equal
from numpy import array, dot

class TwoByTwoDiagonalization(unittest.TestCase):
  matrices = [array([[1.0,2.0],[2.0,8.0]])]
  def testSanity(self):
    for matr in self.matrices:
      vals = jacobi_matr.diagonalize_2by2(array([[1.0,2.0],[2.0,8.0]]))
      res =  dot(dot(vals[0], vals[1]), vals[2])
      print res
      assert_array_equal(matr, dot(dot(vals[0], vals[1]), vals[2]))

if __name__ == "__main__":
  unittest.main()
