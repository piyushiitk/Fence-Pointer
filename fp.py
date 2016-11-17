import mmap
import contextlib
import os
import sys

def fencep(file_name, n):
	f = open('/home/piyushcs/Desktop/CS698F/output/' + file_name +'.txt')

	size = os.stat('/home/piyushcs/Desktop/CS698F/output/' + file_name +'.txt').st_size
	fw = open('/home/piyushcs/Desktop/CS698F/output/' + file_name + '_' + 'fp.txt', 'w')

	r = size%9

	fence = []
	temp = 0
	fp = n

	with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
		i = 0
		while (m.tell() < (size-r)):
			block = m.read(9)[:-1]
			if (int(block[0]) == 1):
				temp += 1
				if (fp == temp):
					fw.write(str(fp) + ' ' + str(i+1) + '\n')
					fp += n


			else:
				temp += int(block[2:], 2)
				if (fp < temp):
					if((temp%n) != 0):
						fp = (int(temp/n) + 1) * n
					else:
						fp = temp
						fw.write(str(fp) + ' ' + str(i+1) + '\n')
						fp += n
			i += 1

	fw.close()


if __name__ == "__main__":
	fencep(sys.argv[1], int(sys.argv[2]))
