import sys
from datetime import datetime

class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

def addLeaf(node, data):
  if node is not None:
    if line < node.data:
      if node.left is None:
        node.left = Node(line)
      else:
         addLeaf (node.left, data)
    else:
      if node.right is None:
        node.right = Node(line)
      else:
        addLeaf(node.right, data)


def writeTree(node, file):
  if node is not None:
    writeTree(node.left, file)
    file.write(node.data)
    writeTree(node.right, file)

root = None
for line in sys.stdin:
  if line == "write\n":
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    with open(str(ts), 'w') as f:
      writeTree(root, f)
      root = None
  elif line == "exit\n":
    break
  else:
    if root is None:
      root = Node(line)
    else :
      addLeaf(root, line)
