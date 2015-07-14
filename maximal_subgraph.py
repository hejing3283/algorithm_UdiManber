def maximal_induced_subgraph( G, k ):
  '''
  Given a graph G = (V, E), find a subgraph S, in which, 
  all vertices in S have degree >=k, or return None if no S identified 
  Sol1: identify those not belongs to S
  input: adjcency list G, and degree cutoff k
  output: subgraph S 
  '''
  S = G.copy()
  nodes = set( S.keys() )
  
  for key, neig in S.items():
    neig = set(neig).intersection(nodes)
    if len(neig) < k :
      S.pop(key, None)
      nodes.remove( key ) 
  ### update final k-cores subgraph 
  for key, neig in S.items():
    S[ key ] = list(set(neig).intersection(nodes))
  return S
  
def prepG( ) :
  G = {1: [2,3,4,5],
       2: [1,3,4,5],
       3: [1,2,4],
       4: [1,2,3,5,6,7],
       5: [2,4],
       6: [4],
       7: [4, 5]
       }
  return G 

G = prepG()
print "orignal nodes", G.keys(), G.values()
for k in range(2,6):
  S = maximal_induced_subgraph(G, k)
  print k, "-core with nodes ", S.keys(), S.values()



