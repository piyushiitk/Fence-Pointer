# Fence-Pointer

This is a project which implements fence pointer to reduce the time required to access perticular bit in the bitmap indexing, where all bits are compressed using the WAH algorithm. 'rowbit.py' contains the code required for the process.
We found out that using fence pointer we can can 30 times more performance than normal sequential access.

# MMAP
We used mmap to reduce the access time of accessing perticular block of the file. Which performs better than normal file operations(seek, read etc.). Because it maps file addresses to the virtual address in memory.

# Usage
For creating fence pointers for perticular compressed file.
```python
python fp.py wah
```
For using rowbit to get the bit of a perticular row.
```python
#python rowbit file_name rownumber
python rowbit.py wah 5
```
P.S. The default location for data is examples in this demo so change location in fp.py and rowbit.py to customize.
