#! /usr/local/bin/python
import jacobi_math as jmath
import random as rand
import numpy as np
import jacobi_plotter as jplot 

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


filename_base = 'jacobi_data'
filename_end = '.txt'
num_mats = 10
def file_of(i):
  return filename_base + str(i) + filename_end
for i in range(num_mats):
  print "-------JACOBI MATRIX DIAGONALIZATION-------------"
  print "Diagonalizing " + str(num_mats) + " randomly generated 5 by 5 symmetric matrices..."
  filename = file_of(i) 
  jrec = jplot.Recorder(filename)
  jmath.jacobi_diagonalize(random_diagonal_matrix(5, 10000), 10**-6, jrec.record,
      jrec.start, jrec.stop)

filenames = map(file_of, range(num_mats)) 
jplotter = jplot.MultiPlotter(filenames)
jplotter.plot()
