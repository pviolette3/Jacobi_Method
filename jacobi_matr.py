from numpy import *
## Orthogonally diagonalize symmetric 2x2 arrrix
def eig_calc(arr):
  a = arr[0][0]
  b = arr[0][1]
  c = arr[1][1]
  eigvals = calc_eigvals(a, b, c)
  eigvects = calc_eigvects(a, b, c, eigvals)
  return [eigvals, eigvects]

def calc_eigvals(a, b, c):
  if b == 0:##it is already diagonalized!
    return [a,c]
  eigvals = []
  base = (a + c)/2
  radius = sqrt(a**2 - 2*a*c + 4*b**2 + c**2)/2
  eigvals.append(base + radius)
  eigvals.append(base - radius)
  return eigvals

def calc_eigvects(a, b, c, eigvals):
  if b == 0:##already diagonal...return I
    if eigvals[0] == a:
       return [array([1.0,0.0]), array([0.0, 1.0])]
    elif eigvals[0] == b:
      return  [array([0.0,1.0]), array([1.0, 0.0])]
    else:
      raise err
  def eigvect_of(l):
    v1 = 1
    v2 = (l - a) / b
    mag = sqrt(v1**2 + v2**2)
    return array([v1 / mag, v2 / mag]) 
  return map(eigvect_of, eigvals)

## A = D + R
## x_k+1 = D^(-1) (b - Rx_k)
def diagonalize_2by2(arr):
  eigs = eig_calc(arr)
  vals = eigs[0]
  vects = eigs[1]
  g = array([vects[0], vects[1]])
  d= array([[vals[0], 0], [0, vals[1]]])
  return [g, d, transpose(g)]

