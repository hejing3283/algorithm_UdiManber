def binary_search(A, n, z) :
  '''
  input: sorted array A in the range of 1 to n, search key z
  output: index of z in A, or None if not in A
  desp: recursive version 
  thought: induction, n/2 each time  
  '''
  def _bsearch(A, lo, up, z): 
    med = (lo+up)/2 
    if z == A[med]:
      return med 
    elif z < A[med] and med > 0:
      return _bsearch(A, 0, med, z)
    elif z > A[med] and med < n-1: 
      return _bsearch(A, med, n, z)
    else:
      return None
  return  _bsearch(A, 0, n, z)


n = 9
A = range(2,n+2)
print A
# print binary_search(A, n, 5)
# print binary_search(A, n, 8)
print binary_search(A, n, 10)
print binary_search(A, n, 9)
print binary_search(A, n, 2)
print binary_search(A, n, 1)
print binary_search(A, n, 14)
