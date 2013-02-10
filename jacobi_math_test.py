import math
import jacobi_math
import unittest
from numpy.testing import assert_array_almost_equal
from numpy import array, dot, eye

def to_wolfram_alpha_string(vals):
 return  vals.replace("[", "{").replace("]", "}").replace('  ', ',').replace('.', '')

class TwoByTwoDiagonalization(unittest.TestCase):
  matrices = [arr.reshape(2,2) for arr in [
      array([1.0,0.0,0.0,1.0]),
      array([3.0,0.0,0.0,10.0]),
      array([1.0,2.0,2.0,8.0]),
      array([1.0,1.0,1.0,2.0])]]
  

  def testSanity(self):
    for matr in self.matrices:
      vals = jacobi_math.diagonalize_2by2(matr)
      res =  dot(dot(vals[0], vals[1]), vals[2])
      assert_array_almost_equal(matr, dot(dot(vals[0], vals[1]), vals[2]), 10)
  
  def testEigenvalues(self):
    eigvals = jacobi_math.eig_calc(eye(2))[0]
    self.assertEqual(eigvals[0], 1)
    self.assertEqual(eigvals[1], 1)
    self.assertEqual(len(eigvals), 2)

  def testDiagonalization(self):
    vals = jacobi_math.diagonalize_2by2(array([2,1,1,2]).reshape(2,2))
    assert_array_almost_equal(vals[1], array([3,0,0,1]).reshape(2,2), 10)
    assert_array_almost_equal(vals[0], ((1/math.sqrt(2))*array([1,1,1,-1])).reshape(2,2))

class JacobiDiagonalization(unittest.TestCase):
  
  def testCarlenCase(self):
    carl_arr = array([2,1,1,1,2,1,1,1,2]).reshape(3,3)
    result = jacobi_math.jacobi_diagonalize(carl_arr, 10**-6)
    assert_array_almost_equal(array([4,0,0,0,1,0,0,0,1]).reshape(3,3),
        result[1], 5)
    assert_array_almost_equal(carl_arr, reduce(dot, result,
      eye(3)))

if __name__ == "__main__":
  unittest.main()
