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
  brutal-force way
  '''
  nextB = [ -1 for _ in B]
  nextB[:2] = [-2,-1]
  for ile in range(2,m):
    irt = nextB[ ile - 1 ] + 1
    while B[ile -1] != B[irt] and irt > -1 :
      irt = nextB[irt] + 1 
    nextB[ ile ] = irt
  return map(lambda x:x+1,nextB )
# print nextB  
print B
print compute_nextB(B, 10)
