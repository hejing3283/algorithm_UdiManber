def mergesort( A, n ):
  '''
  input: an array of distince numbers, in the range of (1,n)
  output: sorted array of input array
  thought: classical divide and conquer algorithm. ## based on selection sort 
  - divide into subproblems
  - sort subproblems
  - combine subproblems ( using the previously mentioned sort strategy

  '''
  def swap(A, a,b):
    temp = A[a];
    A[a] = A[b];
    A[b] = temp
    return A 

  def _msort(A, left, right): 
    if right - left == 1:
      if A[left] > A[right] :
  	A = swap(A, left, right)
    elif left != right :
      mid = (left + right) /2
      _msort(A, left, mid - 1)
      _msort(A, mid, right)
      ## merge
      i = left
      j = mid
      k = 0
      temp = []
      while (i <= mid - 1) and (j <= right) :
        k = k + 1
        if A[i] <= A[j]:
          temp.append( A[i])
          i += 1
        else:
          temp.append( A[j])
          j += 1
      if j > right:
        for ileft in range(mid-i):
          A[right - ileft] = A[mid - 1- ileft]
      for t in range(k) :
        A[left + t] = temp[t]
  _msort(A, 0, n-1)
  return A 

A = [1,5,7,6,2,3,9,8, 10]
print A
print mergesort(A,9)

A = [1,5,7,6,2,9,8, 10]
print A
print mergesort(A,8)
