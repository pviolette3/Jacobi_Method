import matplotlib.pyplot as plt
import numpy as np
from sys import stdout

def wolfram_str(arr):
  res = "{"
  m = len(arr)
  for i in range(m):
    n = len(arr[i])
    row = "{"
    for j in range(n):
      if j == n-1:
        row += str(arr[i][j]) + "}"
      else:
        row += str(arr[i][j]) + ","
    res += row
    if i == m - 1:
      res += "}"
    else:
      res += ","
  return res

class Recorder:
 
  def __init__(self, location):
    self.i = 0
    self.points = []
    self.fileLocation = location
    self.file = open(location, 'w')

  def start(self, matrix):
    print "Writing data to file: " + self.fileLocation
    print "\nInput is the following matrix:"
    self.matrix = matrix
    print matrix
    print "\n\n"

  def stop(self, diagonalized):
    print "Finished!"
    n = len(diagonalized[1])
    eigenvals = []
    for i in range(n):
      for j in range(n):
        if i == j:
          eigenvals.append(diagonalized[1][i][j])
    print 'Eigenvalues: ' + ' '.join(map(str, eigenvals))
    print 'Eigenvectors are:'
    print diagonalized[0]
    print "\nCopy and paste into your browser to check solution:"
    wolfram_base_query = '"http://www.wolframalpha.com/input/?i=' 
    print  wolfram_base_query + wolfram_str(self.matrix)+'"'
    self.file.close()

  def record(self, offset, diagonal, step):
    self.file.write(str(self.i) + "," + str(offset)+ "\n")
    if(self.i == 0):
      print "Computing",
    if self.i % 10 == 0:
      stdout.write(".")
      stdout.flush()
    if self.i % 500 == 0:
      print
    self.i += 1

class Plotter:
  def __init__(self, location):
    self.fileLocation = location
    self.file = open(location, 'r')

  def plot(self):
    points = []
    for line in self.file:
      vals = line.split(",")
      points.append(float(vals[1]))
    iters = np.arange(len(points))
    def fit(x):
      return x * np.log(9.0/10.0) + np.log(points[0])
    plt.plot(iters, fit(iters))
    plt.plot(iters, np.log(points))

def show(self):
  plt.show()

class MultiPlotter:
  def __init__(self, locations):
    self.plotters = []
    for file_location in locations:
      self.plotters.append(Plotter(file_location))

  def fit_dim(self, dim):
    if dim % 2 == 1:
      return (dim, 1)
    else:
      return (dim/2, 2)

  def plot(self):
    plt.figure(1)
    rows, cols = self.fit_dim(len(self.plotters))
    i = 1
    plt.suptitle("Log(Offsets) v Iterations", fontsize=20)
    for plotter in self.plotters:
      plt.subplot(rows, cols, i)
      plotter.plot()
      i += 1
  
  def show(self):
    plt.show()
