import mmap
import contextlib

with open('../wah.txt', 'r') as f:
	with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
		print m.read(10)
		print m[:10]
		print m.read(10) 