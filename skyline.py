def skyline(coord, left, right):
  '''
  input a series of locations for rectangeles, 
  output the locations for the skylines eliminating the inner lines
  input: 
  (1,11,5), (2,6,7), (3,13,9), (12,7,16),(14,3,25), 
  (19,18,22), (23,13,29), (24,4,28)
  output :
  (1,11,3,13,9,0,12,7,16,3,19,18,22,3,23,13,29,0)
  thought: induction method
  n-1, Nth

  '''
  if right - left == 1:
    A = coord[left]
    B = coord[right]
    lenA = len(A) 
    lenB = len(B)
    ## identify new x, y intersection
    C = []
    iA = A.pop(0); 
    iB = B.pop(0)
    iiA = A[-1]
    if iB > iiA: 
      C.extend([iA] + A + [0] + [iB] + B)
    else:
      while len(A) > 0 and len(B) > 0  :
        if iA < iB :
          C.extend([iA, A.pop(0)] )
          iA = A.pop(0)
        else  : 
          C.extend([iB, B.pop(0)] )
          iB = B.pop(0)
      if len(A) >0 :
	C.extend([iA] + A)
      if len(B) > 0:
	C.extend([iB] + B)
    return C
  elif left == right:
    return coord[left]
  else: 
    mid = (right + left ) / 2
    bleft = skyline(coord, left, mid - 1)
    bright = skyline(coord, mid, right)
    C = skyline([bleft, bright], 0, 1) 
    return C

coord = [[1,11,5], [2,6,7],[3,13,9], [12,7, 16],\
    [14,3,25], [19,18,22], [23,13,29], [24,4,28] ] 
print coord
print skyline(coord, 0, 7) 
