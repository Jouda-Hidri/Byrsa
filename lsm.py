import sys

class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

def addLeaf(node, data):
  print("check if node is none")
  if node is not None:
    print("node.data="+node.data)
    if line < node.data:
      if node.left is None:
        node.left = Node(line)
        print("left added")
      else:
         addLeaf (node.left, data)
    else:
      if node.right is None:
        node.right = Node(line)
        print("right added")
      else:
        addLeaf(node.right, data)


def writeTree(node, file):
    if node is not None:
      print("left")
      writeTree(node.left, file)
      print("root")
      file.write(node.data)
      print("right")
      writeTree(node.right, file)

with open('sstable', 'w') as f:
    root = None
    for line in sys.stdin:
        if line == "exit\n":
            writeTree(root, f)
            break
        else:
            print("adding <"+ line+">")
            if root is None:
                root = Node(line)
            else :
                addLeaf(root, line)
            print("root.data="+root.data)
