import sys

partitions = 3

def getKey(line):
  return line.split(":")[0]

def getPartition(key):
  partition = int(key) % partitions
  print(str(partitions)+" partitions: key="+key+" partition="+str(partition))
  return partition


def write(line):
  with open("partitions/"+str(getPartition(getKey(line))), 'a') as f: #todo select partition based on key
    f.write(line)

def read(key):
  with open('partitions/'+str(getPartition(key)), 'r') as f:
    lines = f.readlines()
    i = 0
    result = None
    while(i<len(lines)):
      if(getKey(lines[i])==key):
        result = lines[i].replace(key+':', '> ')
      i+=1
    return result

for line in sys.stdin:
  if line == "exit\n":
    break
  elif line.startswith("partitions "):
    partitions = int(line.replace("partitions ", "").replace("\n", ""))
    if partitions < 1:
      partitions = 1
  elif line.startswith("read "):
    key = line.replace('read ', '').replace("\n", "")
    result = read(key)
    print (result)
  else:
    write(line)
