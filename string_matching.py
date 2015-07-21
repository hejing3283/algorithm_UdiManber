def string_match(A, n, B, m):
  '''
  input: A, a string of size n, 
	 B , a string a size m
  output: Start, as the fisrt index such taht B is a subtring of A starting at A[Start]
  '''
  B,nextB = compute_nextB(B, m)
  print "python index", nextB
  start = 0
  ia = 0; ib = 0
  while ia <= n and ib <= m :
    if A[ia] == B[ib] :
      ia += 1
      ib += 1
    else:
      ib = nextB[ib] + 1
      if ib < 0:
	ia += 1
	ib == 0 
    if ib == m + 1  :
      start = ia - (m+1) 
  return start

def compute_nextB(B, m):
  '''
  preprocess the talbe for next 
  induction proof
  input: B, m as the lenght of B
  output: nextB as the index for sequence B 
  '''
  nextB = [ 0 for _ in B]
  nextB[:2] = [-2,-1]
  for ile in range(2,m+1):
    irt = nextB[ ile - 1 ] + 1
    while B[ile -1] != B[irt] and irt > -1 :
      irt = nextB[irt] + 1 
    nextB[ ile ] = irt
  return B, nextB

A = "xyxxyxyxyyxyxyxyyxyxyxx"
B = "xyxyyxyxyxx"
n = len(A)
m = len(B)
print "golden starndar",[-1,0,0,1,2,0,1,2,3,4,3] 
startA =  string_match(A, n-1, B, m-1)
print A[startA:]
print B

