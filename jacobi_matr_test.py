import jacobi_matr
import unittest
from numpy.testing import assert_array_equal
from numpy import array, dot, eye

class TwoByTwoDiagonalization(unittest.TestCase):
  matrices = [arr.reshape(2,2) for arr in [
      array([1.0,1.0,1.0,2.0]),
      array([1.0,0.0,0.0,1.0]),
      array([3.0,0.0,0.0,10.0]),
      array([1.0,2.0,2.0,8.0])]]
  
  def testSanity(self):
    for matr in self.matrices:
      vals = jacobi_matr.diagonalize_2by2(matr)
      res =  dot(dot(vals[0], vals[1]), vals[2])
      assert_array_equal(matr, dot(dot(vals[0], vals[1]), vals[2]))
  
  def testEigenvalues(self):
    eigvals = jacobi_matr.eig_calc(eye(2))[0]
    self.assertEqual(eigvals[0], 1)
    self.assertEqual(eigvals[1], 1)
    self.assertEqual(len(eigvals), 2)

if __name__ == "__main__":
  unittest.main()
