def polynomial_evaluation( A,  x) :
  n = len(A)
  P = A[ n-1 ]
  for i in range(1, n):
    P = P * x + A[n-1 - i ]
  return P
A = [1, 2, 3] 
x = 4
print polynomial_evaluation(A, 4)
