class Vertex:
  def __init__(self, key):
    self.id = key
    self.connectedTo = {} ## a hash  
    
  def addNeighbor(self, nbr, weight = 0) :
    self.connectedTo[nbr] = weight 

  def getConnections(self) :
    return self.connectedTo.keys()

  def getId( self ) :
    return self.id

  def getWeight( self, nbr ) :
    return self.connectedTo[nbr]

class Graph:
  def __init__(self):
    self.vList = {}
    self.numVertices = 0 
  
  def addVertex( self, key ):
    self.numVertices = self.numVertices + 1
    newV = Vertex( key ) 
    self.vList[ key ] = newV 
    return newV 

  def getVertex(self, key):
    if key in self.vList():
      return self.vList[key]
    else:
      return None
  
  def __contains__(self, key):
    if key in self.vList():
      return True
    else :
      return False

  def addEdge(self, fromKey, toKey, cost = 0 ):
    if not fromKey in self.vList:
      vf = self.addVertex( fromKey ) 
    if not toKey in self.vList:
      vt = self.addVertex( toKey )  
    ### not sure why not use the vf, vt generaged before ??? 
    self.vList[ fromKey ].addNeighbor( self.vList[toKey] , cost) 

  def getVertices( self ): 
      return self.vList.keys()
 
