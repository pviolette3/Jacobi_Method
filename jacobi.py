from optparse import OptionParser
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
      val = rand.random() * max_element * (-1)**rand.randint(0,1)
      reflected[(row, col)] = int(val + 1)
      return reflected[(row, col)]
    else:
      return reflected[(col, row)]
  return generate_matrix(size, size, diag_generator)

parser = OptionParser()
parser.set_defaults(extension=".txt",dim=5,num_mats=10,plot=False,
    error=10**-6,filename_base="jacobi_data",max=10000)
parser.add_option("-x", "--extension", dest="extension", help="Extension of data files")
parser.add_option("-d", "--dim", dest="dim", help="(int) The dimension of the matrices to diagonalize...Be careful. Bigger than 75 is intensive work for the computer.", type="int")
parser.add_option("-n", "--nummats", dest="num_mats", help="(int) The number of nxn matrices to diagonalize", type="int")
parser.add_option("-p", "--plot", dest="plot", help="Indicates whether or not to plot the data", action="store_true")
parser.add_option("-e", "--error", dest="error", help="The offset at which to stop running the iterations", type="float")
parser.add_option("-f", "--filenamebase", dest="filename_base", help="Prefix to attatch to the output files.")
parser.add_option("-m", "--max", dest="max", help="The maximum element size of the matrix...Elements of the matrix will range from +/- this.",type="int")
(options, args) = parser.parse_args()
filename_base = options.filename_base
filename_end = options.extension
num_mats = options.num_mats
show_plot = options.plot
dim = options.dim
max_mat_elem = options.max
max_offset = options.error

def file_of(i):
  return filename_base + str(i) + filename_end
for i in range(num_mats):
  print "-------JACOBI MATRIX DIAGONALIZATION-------------"
  print "Diagonalizing " + str(num_mats) + " randomly generated" +str(dim) + "x"+ str(dim) +" symmetric matrices..."
  filename = file_of(i) 
  jrec = jplot.Recorder(filename)
  jmath.jacobi_diagonalize(random_diagonal_matrix(dim, max_mat_elem), max_offset, jrec.record, jrec.start, jrec.stop)

if show_plot:
  filenames = map(file_of, range(num_mats)) 
  jplotter = jplot.MultiPlotter(filenames)
  jplotter.plot()
  jplotter.show()
