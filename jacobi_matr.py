from numpy import *
## Orthogonally diagonalize symmetric 2x2 arrrix
def eig_calc(arr):
  a = arr[0][0]
  b = arr[0][1]
  c = arr[1][1]
  eigvals = []
  base = (a + c)/2
  discrim = sqrt(a**2 - 2*a*c + 4*b**2 + c**2)
  eigvals.append(base + discrim/2)
  eigvals.append(base - discrim/2)

  eigvects = []
  for l in eigvals:
    v1 = b / (a - l)
    v2 = 1
    u1 = v1 / sqrt(v1**2 + 1)
    u2 = 1 / sqrt(v1**2 + 1)
    print 'u1, u2' + str(u1) + ' ' + str(u2) 
    eigvects.append(array([u1, u2]))
  return [eigvals, eigvects]

## A = D + R
## x_k+1 = D^(-1) (b - Rx_k)
def diagonalize_2by2(arr):
  eigs = eig_calc(arr)
  vals = eigs[0]
  vects = eigs[1]
  g = array([vects[0], vects[1]])
  d= array([[vals[0], 0], [0, vals[1]]])
  return [g, d, transpose(g)]

mats = diagonalize_2by2(array([[1.0,2.0],[2.0,8.0]]))
print mats
print (dot(dot(mats[0], mats[1]), mats[2]))
