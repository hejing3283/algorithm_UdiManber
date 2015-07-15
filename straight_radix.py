def straight_radix( X, n, k):
  '''
  input: X, an array of integers, each with k digits, in the range of 1 to n
  output: X, the array in sorted order
  '''
  dnum = 10 ## 0-9
  GQ = X[:]
  Q =  [ [] for _  in range(dnum + 1) ]
  for ik in range(k-1,-1, -1):
    while len(GQ) :
      x = GQ.pop()
      d = int(str(x)[ik])
      Q[d].insert(0,x)
    for t in range(dnum + 1) :
      GQ.extend( Q[t] ) 
    Q =  [ [] for _  in range(dnum + 1) ]
  return GQ

X = [410,153,792,400,123,503]
k = 3
n = 9
print X
print straight_radix( X, n , k)
