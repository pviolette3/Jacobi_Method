import jacobi_math as jmath
import random as rand
import numpy as np
import jacobi_plotter as jplot 

filename = 'jacobi_data.txt'

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

jrec = jplot.Recorder(filename)
jmath.jacobi_diagonalize(random_diagonal_matrix(5, 10000), 10**-6, jrec.record,
    jrec.start, jrec.stop)

jplotter = jplot.Plotter(filename)
jplotter.plot()
