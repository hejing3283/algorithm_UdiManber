def maximum_consecutive_sequence( X ):
  '''
  Given an array of n intergers, not necessarily positive,
  find the largest sum of a consecutive seq, if sum = negative, assign it 0.
  input : An array of size n
  output: global_max( the sum the the maixumum subsequence), and the seq
  thought:
  induction: 
    n-1 no solution, the only new solution would be ni n_n-1 , nth, only if nth positive 
    n-1 has solution -- the solution is last k items, check nth item, return new solution
		     \ the solution is some k items in the middle, compare with new laster m items, return the max 
  points, keep track of the last k item, check nth item, set sum <0 to 0

  '''
  seq_gb = []; seq_sf = [] 
  max_gb = 0; max_sf = 0
  for ix in range( len(X) ) :
    if X[ix] + max_sf > max_gb:
       max_sf += X[ix]
       max_gb = max_sf
       seq_sf.append( X[ix] )
       seq_gb = seq_sf[:] ## hard copy is NECESSARY!!!
       continue
    else:
       if X[ix] + max_sf > 0 :
	 max_sf += X[ix]
	 seq_sf.extend([X[ix]])
       else:
	 max_sf = 0
	 seq_sf = []
       continue
	
  return max_gb, seq_gb

X = [1,3,0,-1,-5,2,-1,0,1,2,5,-3]

print X
print maximum_consecutive_sequence(X)

