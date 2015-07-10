def Insert_Heap( A, n, x) :
  ## this version didn't maitein the property in the new leave node
  A = A + [x]
  n = n + 1
  child = n  
  parent = n / 2
  while parent >= 1 :
    if A[ child - 1 ]  > A[ parent - 1 ] :
      ## swap and exchange
      temp = A[parent - 1] 
      A[parent - 1 ] = A[child - 1]
      A[child - 1 ] = temp 
      ## TODO to make it maitain the property in new leaf
      child = parent 
      parent = child / 2  
    else :
      break

  return A, n 
A = [10, 9, 7, 3, 8, 6, 4 ] 
n = 7 
x = 5
print A
print Insert_Heap(A, n, x )
A = [10, 7, 9, 3, 5, 1, 6 ] 
n = 7 
x = 8

print A
print Insert_Heap(A, n, x )


