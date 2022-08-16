import sys
from datetime import datetime

tree = None
segments = []

class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

def getKey(line):
  #lets make ':' the separator
  return line.split(":")[0]

def addLeaf(node, data):
  if node is not None:
    if getKey(line) < getKey(node.data):
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
  global tree
  global segments
   # todo rename to sstable
  path = "sst/"+str(datetime.timestamp(datetime.now())) # todo current segment also should be global
  segments.append(path) # todo create new segment only when current is too big
  print("> segments size="+str(len(segments)))
  with open(path, 'w') as f:
    writeTree(tree, f)
    tree = None

def read(key):
  with open('sstable', 'r') as sstable:
    lines = sstable.readlines()
    i = 0
    result = None
    while(i<len(lines)):
      if(getKey(lines[i])==key):
        result = lines[i]
      i+=1
    return result

def merge():
  global segments
  with open(segments[0], 'r') as segment1, open(segments[1], 'r') as segment2, open('sstable', 'w') as sstable:
    lines1 = segment1.readlines()
    lines2 = segment2.readlines()
    i = 0
    j = 0
    while ( i < len(lines1) and j < len(lines2)):
      line1IsDuplicate = i+1 < len(lines1) and getKey(lines1[i]) == getKey(lines1 [i+1])
      line2IsDuplicate = j+1 < len(lines2) and getKey(lines2[j]) == getKey(lines2 [j+1])
      if(line1IsDuplicate or line2IsDuplicate):
        if(line1IsDuplicate):
          i+=1
        if(line2IsDuplicate):
          j+=1
      elif(getKey(lines1[i]) == getKey(lines2[j])):
        print(lines1[i]+"=="+lines2[j])
        sstable.write(lines2[j]) #lines2 later than lines1
        i+=1
        j+=1
      elif (getKey(lines1[i]) < getKey(lines2[j])):
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
  elif line.startswith("read "):
    key = line.replace('read ', '').replace("\n", "")
    result = read(key)
    print (result)
  else:
    print("key="+getKey(line))
    if tree is None:
      tree = Node(line)
    else :
      addLeaf(tree, line)
      # todo auto write files, auto merge files
      # todo implement key: comma separated
