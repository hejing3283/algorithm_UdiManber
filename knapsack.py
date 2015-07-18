def knapsack(S, K) :
  '''
  dynamic programming to solve knapsack problem
  input: S, an array of size n storing sizes of the items
         K, the size of the knapsack
  output: P ( a 2-d array such that
  P[i, k].exist = True if there exist a solution to the problem with the first i elements  ## a knapsack of size k, 
  and P[i,k].belong = true if the ith element belongs to that solution
  '''
  K = K + 1 ## hand python index problem
  n = len(S)  
  ### init
  Pexist = [ [ 0 for _ in range(K) ]  for _ in range(n + 1)]
  Pbelong = [ [0 for _ in range(K) ]  for _ in range(n + 1)]
  Pexist[0][0] = True
  for ik in range(1,K) :
    Pexist[0][ik] = False

  for isize in range(1,n + 1):
    for ik in range(K):
      Pexist[ isize ][ ik ] = False
      if Pexist[ isize-1 ][ ik ]:
	Pexist [ isize ][ ik ] = True
	Pbelong[ isize ][ ik ] = False
      elif ik - S[isize - 1] >= 0:
	if Pexist[ isize-1][ ik -S[isize - 1]]:
	  Pexist[isize][ik] = True
	  Pbelong[isize][ik] = True
    
  return Pexist, Pbelong


S = [2,3,5,6]
K = 16
pe, pb =  knapsack(S, K)
print "Size", " ".join(map(str,range(K+1) ))
for isize in range(1, len(S)+1):
  print("k=" + str(S[isize -1])),
  temp1 = map(lambda x:int(x), pe[isize] )
  temp2 = map(lambda x:int(x)*2, pb[isize])
  for ik in range(K + 1):
    print( temp1[ik] + temp2[ik]),
  print 

