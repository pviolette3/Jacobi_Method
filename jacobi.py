import jacobi_math as jmath
import random as rand
import numpy as np

def generate_matrix(rows, cols, generating_function):
	result = []
	for i in range(rows):
		for j in range(cols):
			result.append(generating_function(i, j))
	return np.array(result, dtype=float).reshape(rows, cols)

def random_diagonal_matrix(size, max_element):
  reflected = {}
  def diag_generator(row, col):
    if row <= col:
      val = rand.random() * max_element
      reflected[(row, col)] = int(val + 1)
      return reflected[(row, col)]
    else:
      return reflected[(col, row)]
  return generate_matrix(size, size, diag_generator)

class Recorder:
	def __init__(self):
		self.i = 0

	def record_print(self, offset, diagonal, step):
		if self.i == 0:
			print "diagonalizing following matrix"
			print diagonal
		if self.i % 1000 == 0:
			print "(" + str(self.i) + "," + str(offset) + ")"
		self.i += 1

recorder = Recorder()
jmath.jacobi_diagonalize(random_diagonal_matrix(100, 10000), 1, recorder.record_print)