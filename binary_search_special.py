def special_binary_search(A, left, right, n):
  '''
  input: X, a sorted array, length n  
  output: position of which ai = i
  desp.: recursion
  '''
  ### boundary handling 
  if right - left <= 1 and (right == n-1 or left == 0):
    if A[right ] == n-1  :
      return n-1 
    elif A[left ] == 0 :
      return 0
  else:
    mid  = (right + left) / 2
    if A[mid] > mid :
      return special_binary_search(A, left, mid, n) 
    elif A[mid] < mid :
      return special_binary_search(A, mid, right, n) 
    else:
      return mid

if __name__ == "__main__":
 
  A = range(-5,16,2); n =len(A) 
  print A,n, special_binary_search(A,0, n-1, n)
  A = range(0,16,2)
  n = len(A) 
  print A, n, special_binary_search(A,0, n-1, n)
  A = range(0,7,2)
  n = len(A) 
  print A,n, special_binary_search(A,0,n-1,n)
  A = range(-3,15,2); n = len(A) 
  print A,n, special_binary_search(A,0, n-1, n)
