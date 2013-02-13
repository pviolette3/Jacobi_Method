from optparse import OptionParser
import scipy as sp
import numpy as np

def proportionize(vals):
  max = vals[0]
  def to_proportion(val):
    return val / max;
  return map(to_proportion, vals)

def min_index_lt(proportion, arr):
  for i in range(len(arr)):
    if arr[i] < proportion:
      return i
  return None

def iterations_to(proportion, arrs):
  proportions = map(proportionize, arrs)
  res = []
  for props in proportions:
    res.append(min_index_lt(proportion, props))
  return res

def dist_vals_for(arr):
  return [sp.mean(arr), sp.std(arr)]

def load_data_match(base_name, num_data, extension):
  all_data = []
  for i in range(num_data):
    filename = base_name + str(i) + extension
    f = open(filename, 'r')
    vals = []
    for line in f:
      vals.append(float(line.split(",")[1]))
    all_data.append(vals)
  return np.array(all_data)

def find_results(all_data):
  return dist_vals_for(iterations_to(max_prop, all_data))
parser = OptionParser()
parser.set_defaults(extension=".txt",num_mats=10,filename_base="jacobi_data",err=0.5)
parser.add_option("-x", "--extension", dest="extension", help="Extension of data files")
parser.add_option("-n", "--nummats", dest="num_mats", help="(int) The number of nxn matrices to diagonalize", type="int")
parser.add_option("-e", "--error", dest="err", help="The proportion of errors to find",type="float")
(options, args) = parser.parse_args()
num_mats = options.num_mats
base_name = options.filename_base
extension = options.extension
max_prop = options.err

results = find_results(load_data_match(base_name, num_mats, extension))

print "Of " + str(num_mats) + " matrices created, the...."
print "Average number of iterations to reach " + str(max_prop) + " of the error: " + str(results[0]) 
print "Std dev of iterations: " + str(results[1])
