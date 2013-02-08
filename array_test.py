from numpy import *

a = arange(6)
print a
reflected = {}
def diag_generator(row, col):
	if row <= col:
		val = rand.random() * max_element
		reflected[(row, col)] = val
		return reflected[(row, col)]
	else:
		return reflected[(col, row)]


