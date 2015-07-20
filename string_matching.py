def string_match(A, n, B, m):
  '''
  input: A, a string of size n, 
	B , a string a size m
  output: Start, as the fisrt index such taht B is a subtring of A starting at A[Start]
  '''
  return start

A = "xyxxyxyxyyxyxyxyyxyxyxx"
B = "xyxyyxyxyxx"
# nextB = [-1,0,0,1,2,0,1,2,3,4,3] 

def compute_nextB(B, m):
  '''
  preprocess the talbe for next 
  induction proof
  input: B, m as the lenght of B
  output: nextB as the index for sequence B 
  '''
  nextB = [ -1 for _ in B]
  nextB[:2] = [-2,-1]
  for ile in range(2,m+1):
    irt = nextB[ ile - 1 ] + 1
    while B[ile -1] != B[irt] and irt > -1 :
      irt = nextB[irt] + 1 
    nextB[ ile ] = irt
  return B, nextB
# map(lambda x:x+1,nextB )

B, nextB =  compute_nextB(B, 10)
print B, nextB
