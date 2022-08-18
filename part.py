import sys

def getKey(line):
  return line.split(":")[0]

def write(line):
  with open("partitions/1", 'a') as f:
    f.write(line)

def read(key):
  with open('partitions/1', 'r') as f:
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
  elif line.startswith("read "):
    key = line.replace('read ', '').replace("\n", "")
    result = read(key)
    print (result)
  else:
    write(line)
