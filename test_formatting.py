import numpy as np

arr = np.array([1,2,3,-1,-2,-3,-1,-2,3]).astype(float).reshape(3,3)
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
    print res
  return res
print wolfram_str(arr)

