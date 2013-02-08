import jacobi_matr
import unittest
from numpy import *

class TwoByTwoDiagonalization(unittest.TestCase):
  matrices = [array([[1.0,2.0],[2.0,8.0]])]
  def testSanity(self):
    for matr in self.matrices:
      vals = jacobi_matr.diagonalize_2by2(array([[1.0,2.0],[2.0,8.0]]))
      res =  dot(dot(vals[0], vals[1]), vals[2])
      print res
      self.assertEqual(matr.all(), dot(dot(vals[0], vals[1]), vals[2]).all())

if __name__ == "__main__":
  unittest.main()
