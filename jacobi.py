import random as rand
from scipy import mat
def g_matrix(num_rows, num_cols, generating):
	rows = []
	for r in range(num_rows):
		row = []
		for c in range(num_cols):
			row.append(generating(r, c))
		rows.append(row)
	return rows

def random_matrix_square(size, max_element):
	return g_matrix(size, size, 
		lambda row, col: rand.random() * max_element)

def random_diagonal_matrix(size, max_element, use_ints=False):
	reflected = {}
	def diag_generator(row, col):
		if row <= col:
			val = rand.random() * max_element
			reflected[(row, col)] = int(val + 1) if use_ints else val
			return reflected[(row, col)]
		else:
			return reflected[(col, row)]

	return g_matrix(size, size, diag_generator)

def(list):
	res = ""
	for l in list:
		res += "[" + (" ".join(map(str, l))) + "]\n"
	return res

def jacobi(A, b, guess_x, valid):
	new_x = calc_new_x(A, b, guess_x)
	while valid(new_x):
		print "new x:" + " ".join(map(str, new_x))
		new_x = calc_new_x(A, b, guess_x)
	return new_x

def calc_new_x(A, b, guess_x):
	new_x = []
	for i in range(len(A)):
		sum = 0
		for j in range(len(A[i])):
			sum += A[i][j] * guess_x[j] if i != j else 0
		new_x.append((b[i] - sum) / A[i][i])
	return new_x

num_executions = [20]
def times(unused):
	num_executions[0] = num_executions[0] - 1
	return num_executions[0] > 0
matrix = [[2.0,2.0],[2.0,2.0]]
b = [1.0,2.0]
x_0 = [0.0,0.0]
print "solving Ax = b where \nA=" + stringify(matrix) + "\nb=" + (" ".join(map(str, b)))
print "Solved: " + " ".join(map(str, jacobi(matrix, b, x_0, times)))
