import sys
import os
import shutil

partitions = 3

def getKey(line):
  return line.split(":")[0]

def getPartitionByKey(key):
  return int(key) % partitions

def getPartition(p, key): # called for rebalancing
  return int(key) % p

def write(line):
  with open("partitions/"+str(getPartitionByKey(getKey(line))), 'a') as f: #todo select partition based on key
    f.write(line)

def read(key):
  with open('partitions/'+str(getPartitionByKey(key)), 'r') as f:
    lines = f.readlines()
    i = 0
    result = None
    while(i<len(lines)):
      if(getKey(lines[i])==key):
        result = lines[i].replace(key+':', '> ')
      i+=1
    return result

def rebalance(partitions2):
  global partitions
  print(str(partitions)+" -> "+str(partitions2))
  for p1 in range(partitions):
    path = 'partitions/'+str(p1)
    if os.path.isfile(path):
      with open(path, 'r') as f:
        lines = f.readlines()
        i = 0
        while(i<len(lines)):
          with open("partitions/"+str(getPartition(partitions2, getKey(lines[i])))+"_tmp", 'a') as tmp:
            tmp.write(lines[i])
          i+=1
      os.remove(path)
  for p2 in range(partitions2):
    if os.path.isfile('partitions/'+str(p2)+'_tmp'):
      shutil.move('partitions/'+str(p2)+'_tmp', 'partitions/'+str(p2))
  partitions = partitions2

for line in sys.stdin:
  if line == "exit\n":
    break
  elif line.startswith("p="):
    partitions2 = int(line.replace("p=", "").replace("\n", "")) #todo max(1, ...)
    if partitions2 < 1:
      partitions2 = 1
    if partitions2 != partitions:
      rebalance(partitions2)
  elif line.startswith("read "):
    key = line.replace('read ', '').replace("\n", "")
    result = read(key)
    print (result)
  else:
    write(line)
