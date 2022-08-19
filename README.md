# Byrsa

**LSM-Tree / SSTaable**

elements are added in order (ordered by key) in the SSTable; They are first added to an ordered binary tree (LSM-Tree) and then written in segments. Each time the current segment exceeds 25 Bytes, a new segment is created. When 2 segments exceeds the threshold, they are merged into the SSTable. During the merge the files are compacted, means duplicates are removed.

run:  
``python lsm.py``

add element, for example value "milk" for key "1"    
``1:milk``

read element, for example read value for key "1"    
``read 1``

When a new value is set to an existing key, the key would be updated. For example when running    
``1:milk``    
``1:coffee``    

``read 1`` would return ``coffee``

**Partitioning**    
run:  
``python part.py``

change partitions, for example set partitions to 3:    
``p=3``

add element     
``1:milk``

read element    
``read 1``
