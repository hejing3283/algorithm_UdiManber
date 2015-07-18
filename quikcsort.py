def quicksort( A ):
"""
input: an array
output: sorted array
thought: why? another stratgy when compare to mergesort, which spends 
lots effort on merging, quicksort spend many effort on dividing. 
both used divided and conquer strategy. 
"""
  def partition( A, left, right):
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
    temp = A[left]; A[left] = A[mid]; A[mid] = temp
    return A 
