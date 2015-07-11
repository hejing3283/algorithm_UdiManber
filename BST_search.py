class Node:
  """
  BST tress, explicit representation, each node has key, 
  pointer to left code, ponter to right node 
  """
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

  def insert(self, key):
    ## insert new node
    ### TODO : need more work to make it a balanced tree
    if self.key:
      if key < self.key:
	if self.left is None:
	  self.left  = Node( key )
	else:
	  self.left.insert( key )
      elif key > self.key:
	if self.right is None:
	  self.right = Node( key )
	else:
	  self.right.insert( key )
      else :
	pass
    else:
      self.key = key

  def delete(self, key) :
    ## delete a key
    node, parent = self.lookup(key)
    if node == None or parent == None:
      print key, "not in the tree or root node"
      return self 
    if node.left is None and node.right is None:
      ## case 1 no child
      if parent.left is node:
	parent.left = None
      else:
	parent.right = None
      del node
    
    elif (node.left is None) + (node.right is None) == 1:
      ## case 2 one child
      if node.left:
	_node = node.left
      else:
	_node = node.right
      
      if parent:
	if parent.left is node: 
	  parent.left = _node
	else:
	  parent.right = _node
	del node
      else:
	self.left = _node.left
	self.right = _node.right
	self.key = _node.key

    elif node.left and node.right:
      ## case 3 2 children
      ## find a successor
      parent = node
      successor = parent.right
      while successor.left:
	parent = successor
	sucessor = successor.left
      node.key = successor.key
      if parent.left is sucessor:
	parent.left = successor.right
      else:
	parent.right = successor.right

  def print_tree(self):
    ### print the tree
    if self.left :
      self.left.print_tree()
    print self.key
    if self.right:
      self.right.print_tree()

  def lookup(self, key, parent = None):
    ### recursively search BST
    ## output: node, and parent
    if key < self.key:
      if self.left is None:
	return None, None
      return self.left.lookup( key, self)
    elif key > self.key:
      if self.right is None:
	return None, None
      return self.right.lookup( key, self) 
    else: 
      return self, parent
      

root = Node(8)
root.insert(10)
root.insert(6)
root.insert(4)
root.insert(11)
root.insert(9)
root.insert(7)
x = 4
x = 7
x = 8
root.lookup(x)[0].print_tree()
print root.lookup(x)[0].left, "   ", root.lookup(x)[0].right  
print "-----------"
root.delete(x)
root.print_tree()

