from Graph import Graph  

def celebrity( Know ) :
  '''
  Given a adjacency matrix indicating the know relationship 
  btw n persons, identify the celebrity in this graph, 
  or return None
  '''
  ## step 1, get all nodes, put into a stack
  ## step 2, eliminate non-candidate
  i = 0
  j = 1
  nextNode = 2
  n = len(Know)
  while (nextNode  <= n) : 
    if Know[i][j]:
      i = nextNode 
    else:
      j = nextNode
    nextNode += 1
    continue 

  if i == n + 1:
    candidate = j
  else:
    candidate = i
  print candidate
  wrong = False
  k = 0
  Know[candidate][candidate] = False
  while not wrong and k < n:
    if Know[candidate][k] :
      wrong = True
    if not Know[k][candidate]:
      if candidate != k:
	wrong = True
    k += 1
  if not wrong:
    celeb = candidate
  else :
    celeb = None
  return celeb

def prepG( type = 'class' ) :
  if type == 'dict':
    G = {1: [2,3,4,5],
         2: [1,3,4,5],
         3: [1,2,4],
         4: [1,2,3,5,6,7],
         5: [2,4],
         6: [4],
         7: [4, 5]
         }
  if type == 'class':
    G = Graph()
    for i in range(1,8):
      G.addVertex(i) 
    G.addEdge(1, 2, 1) 
    G.addEdge(1, 3, 1) 
    G.addEdge(2, 3, 1) 
    for i in range(1,4) + range(5,8):
      G.addEdge(4, i, 1) 
    G.addEdge(5, 2, 1) 
    G.addEdge(7, 5, 1) 
  if type == 'matrix':
     G = [[0,1,1,1,0,0,0],
	  [1,0,1,1,1,0,0],
	  [1,1,0,1,0,0,0],
	  [1,1,1,0,1,1,1],
	  [0,1,0,1,0,0,0],
	  [0,0,0,4,0,0,0],
	  [0,0,0,1,1,0,0]]

  return G 

G = prepG( type = 'matrix') 
print(G)
print celebrity(G)

