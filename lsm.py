import sys

with open('sstable', 'w') as f:
    for line in sys.stdin:
        f.write(line)
