def longest_increasing_subsequencing( A , m ) :
  ''' 
  input: a sequence of integers
  output : the longest increasing subsequence 
  '''
  BIS = [] 
  LIS = None
  def bsearch_last(BISlast, left, right, k, a ):
    '''
    given a set of BIS, the length of it, and an element, return the indices k1, k2 
    for which BIS[k1][-1] < a < BIS[k2][-1]
    or [-1,0] if it's minimum
    or k, k+1 if it's maximum
    use binary search
    '''
    med = (left + right) / 2
    if right - left == 1:
      if BISlast[ left ] > a :
        return -1, 0 
      elif BISlast[right] < a :
	return k-1, k
      else:
	return left, right
    else:
      if BISlast[ left ] > a :
        return -1, 0 
      else:
        if BISlast[med] > a:
          return bsearch_last(BISlast, left, med , k, a)
        elif BISlast[ med ] < a :
          if BISlast[right] > a :
            return bsearch_last(BISlast, med, right, k, a )
          else:
            return k-1, k  
        else: 
          return med, med 
  BIS = []
  BIS.append([A[0]])

  for ia in range(1,m) :
    kBIS = len(BIS)
    if kBIS == 1:
      if A[ia] > BIS[0][-1]:
	BIS[0].append(A[ia])
      else:
	BIS.insert(0,[A[ia]])
    else: 
      BISlast = map(lambda x:x[-1], BIS)
      ik1, ik2 = bsearch_last(BISlast, 0, kBIS-1, kBIS, A[ia])
      if ik1 < 0 or ik1 == ik2:
        ## start a new sequence
        BIS.insert(0,[A[ia]])
      elif ik1 == kBIS - 1:
	BIS[ik1].append( A[ia] )
      else:
        BIS[ik1].append( A[ia] )
  lenBIS = 0
  LIS = []
  for iBis in BIS:
    n  = len(iBis)
    if n > lenBIS:
      lenBIS = n
      LIS = iBis 
    elif n == lenBIS:
      LIS.append(iBis)
    else:
      continue
  return LIS 

if __name__ == "__main__" :
  A = [1,5,-1,9,2,7,3,4,10,6,7]
  m = len(A)
  print A 
  print longest_increasing_subsequencing(A, m)

