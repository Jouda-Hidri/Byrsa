import sys
from datetime import datetime

root = None
segments = []

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

def write():
  global root
  global segments
  path = str(datetime.timestamp(datetime.now())) # todo current segment also should be global
  segments.append(path) # todo create new segment only when current is too big
  print("> segments size="+str(len(segments)))
  with open(path, 'w') as f:
    writeTree(root, f)
    root = None

def merge():
  global segments
  with open(segments[0], 'r') as segment1, open(segments[1], 'r') as segment2, open('sstable', 'w') as sstable:
    lines1 = segment1.readlines()
    lines2 = segment2.readlines()
    i = 0
    j = 0
    while ( i < len(lines1) and j < len(lines2)):
      line1IsDuplicate = i+1 < len(lines1) and lines1[i] == lines1 [i+1]
      line2IsDuplicate = j+1 < len(lines2) and lines2[j] == lines2 [j+1]
      if(line1IsDuplicate or line2IsDuplicate):
        if(line1IsDuplicate):
          i+=1
        if(line2IsDuplicate):
          j+=1
      elif (lines1[i] <= lines2[j]):
        sstable.write(lines1[i])
        i+=1
      else:
        sstable.write(lines2[j])
        j+=1
    while ( i < len(lines1) ):
      sstable.write(lines1[i])
      i+=1
    while ( j < len(lines2) ):
      sstable.write(lines2[j])
      j+=1
  print("----------")
  with open('sstable', 'r') as f:
      print(f.read())
  print("----------")

for line in sys.stdin:
  if line == "write\n":
    write()
  elif line == "merge\n":
    merge()
  elif line == "exit\n":
    break
  else:
    if root is None:
      root = Node(line)
    else :
      addLeaf(root, line)
      # todo auto write files, auto merge files
      # todo implement read
