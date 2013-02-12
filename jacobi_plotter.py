import matplotlib.pyplot as plt
import numpy as np

def to_wolfram_alpha_string(arr):
  return "{" +" ".join(map(str, arr)).replace("  ", ",").replace(" ", "").replace("[","{").replace("]", "}").replace(".","").replace("}{","},{")+"}"

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
    print  wolfram_base_query + to_wolfram_alpha_string(self.matrix)+'"'
    self.file.close()

  def record(self, offset, diagonal, step):
    self.file.write(str(self.i) + "," + str(offset)+ "\n")
    if self.i % 100 == 0:
      print "computing..."

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
    plt.plot(range(len(points)), points, 'r--')

class MultiPlotter:
  def __init__(self, locations):
    self.plotters = []
    for file_location in locations:
      self.plotters.append(Plotter(file_location))

  def plot(self):
    plt.figure(1)
    rows = 5
    cols = 2
    i = 1
    for plotter in self.plotters:
      plt.subplot(rows, cols, i)
      plotter.plot()
      i += 1
    plt.show()
