def quicksort( A ):
  """
  input: an array
  output: sorted array
  thought: why? another stratgy when compare to mergesort, which spends 
  lots effort on merging, quicksort spend many effort on dividing. 
  both used divided and conquer strategy. 
  TODO: consider improvement for base cases
  """
  def partition( A, left, right):
    '''
    input: an array, and the boundarys btw which a partition will be done
    output: array, and the middle element which seperates larger and small partitions
    '''
    plo = left
    pup = right
    pivot = A[left] ## can use random
    while plo < pup:
      while A[plo] < pivot and plo <= pup:
	plo += 1
      while A[pup] > pivot and pup >= plo:
	pup -= 1
      if plo < pup :
	temp = A[pup]; A[pup] = A[plo]; A[plo] = temp
    mid  = pup
    # temp = A[left]; A[left] = A[mid]; A[mid] = temp
    return A, mid
  def _qsort(A, left, right):
    if left < right:
      A, mid =  partition(A, left, right) 
      _qsort(A, left, mid - 1)
      _qsort(A, mid + 1, right)
    return A
  return _qsort(A, 0, 6 )

A = [8,5, 7,9,10,2,3]
print quicksort(A)
