def Remove_Max_from_Heap( A, n ) :
  # input: a array representation oa heap A, with n elements
  # output: the maximum root, new heap A', number of elements in A'
  maxA = A[0]
  A[0] = A[n-1]
  A = A[:(n-1)]
  parent = 0
  child = 1
  n = n - 1 
  while child < n - 1 - 1:
    if A[ child ] < A[ child + 1 ] :
      child = child + 1
    if A[ parent ] < A[ child ] :
      temp = A[ parent ] 
      A[ parent ] = A[ child ] 
      A[ child ] = temp
      parent = child 
      child = 2 * child
  return maxA, A, n

A = [10, 8, 9, 6, 7, 3, 5 ] 
n = 7 
print A      
print Remove_Max_from_Heap(A, n ) 


