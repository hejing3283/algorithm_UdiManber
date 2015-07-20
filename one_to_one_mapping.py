def mapping( A , f ) :
  '''
  given a set of integers A, and a function f 
  identify a subset of S in which all the elements in S, 
  are mapping to all the elements in S
  input: a set of integers f, maximum integer n  
  output: new set S
  thougth:
  elimination of elements that not belongs to S
  '''
  n = len(A)
  fA = map(f, A)
  fA = [i for i in fA if i in A]

  S = A[:]
  counter = [0 for _ in range(n) ] 
  for i in range(len(fA)) : 
    counter[ fA[i] ] +=  1 
  queue = [ j for j in range(n) if counter[j] == 0 ] 
  print counter
  while len(queue) > 0 :
    print queue, 
    i = queue.pop(0)
    print i,
    S.pop(i)
    counter[ fA[i] ] = counter[ fA[i] ] - 1
    print counter
    if counter[ fA[i] ] == 0:
      queue.extend( [fA[i]] ) 

  return S

A = [1,5,2,3,7,8,10]

def mapf_1(x):
  return 2 * x -1

fun = mapf_1
print mapping(A, fun) ### do not pass the name of the function, pass the function 

