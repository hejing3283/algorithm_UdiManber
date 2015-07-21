def special_binary_search(A, n):
  '''
  input: X, a sorted array, length n  
  output: position of which ai = i
  desp.: recursion
  '''
  def _bsearch( A, left, right):
    mid  = (right + left) / 2
    if mid == A[mid]:
      return mid
    elif A[mid] > mid and mid > 0:
      _bsearch(A, left, mid) 
    elif A[mid] < mid  and mid < n-1:
      _bsearch(A, med, right) 
    else:
      if A[right ] == n-1 :
	return n-1 
      elif A[left ] == 0:
	return 0
      else:
	return None
  return _bsearch(A, 0, n-1)

if __name__ == "__main__":
 
  A = range(-5,16,2)
  n = 11
  print A, special_binary_search(A,n)

  A = range(0,16,2)
  n = len(A) 
  print A, special_binary_search(A,n)
  A = range(0,7,2)
  n = len(A) 
  print A, special_binary_search(A,n)
