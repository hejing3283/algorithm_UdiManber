def mapping( A, f, n ) :
  '''
  given a set of integers f , which is a mapping from 1 to n 
  identify a subset of S in which all the elements in S, 
  are mapping to all the elements in S
  input: a set of integers f, maximum integer n  
  output: new set S
  thougth:
  elimination of elements that not belongs to S
  -- implementation in non-recursive
  -- implementation in recursive
  '''
  A = map(lambda x:x-1,A)
  f = map(lambda f:f-1,f)
  S = A[:]
  counter = [0 for _ in range(n ) ] 
  for i in range(n) : 
    counter[ f[i] ] +=  1 
  queue = [ j for j in range(n ) if counter[j] == 0 ] 

  while len(queue) > 0 :
    i = queue.pop(0)
    print i, S
    S.remove(i) ### index retains the mapping information
    temp = f[i]
    counter[ temp ] = counter[ temp ] - 1
    if counter[temp] == 0 :
      queue.extend( [f[i] ] ) 
  return map(lambda x:x+1,S )

A = [1,2,3,4,5,6,7]
f = [3,1,1,5,5,4,6]
print mapping(A, f, 7) ### do not pass the name of the function, pass the function 
A = [1,2,3,4,5,6,7,8,9,10,11]
f = [9,5,6,3,3,3,1,4,1,7,8]
print mapping(A, f, 11)

