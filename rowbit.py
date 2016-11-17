import sys
import mmap
import contextlib
import os
import time

def fencep(file_name, num):
	fc = open('examples/' + file_name +'.txt')
	fp = open('examples/' + file_name + '_fp.txt')

	if(num%7 == 0):
		n = num/7
		r = 7
	else:
		n = num/7 + 1
		r = num%7

	prev = 1
	res = 1
	# p, offset variables are the mapping from real block no to compressed block no in compressed file.
	p = 1
	offset = 1
	count = 0

	check = 0

	for line in fp:
		next1, res1 = line[:-1].split(' ')
		next1 = int(next1)
		res1 = int(res1)
		if (n == next1):
			p = next1
			offset = res1
			check += 1
			break
		elif (n < next1):
			p = prev
			offset = res
			check += 1
			break
		else:
			prev = next1
			res = res1
			count += 1


	if (check == 0):
		p = prev
		offset = res

	#print 'offset', p, offset, count

	for line in fc:
		temp = n - p

		data = line.split(' ')[offset-1:]
		data[-1] = data[-1][:-1]

		# print 'temp is ', temp
		if (temp == 0):
			i = 1
			fc = int(data[0][0])
			bit = int(data[0][1])

		else:
			data = data[1:]
			i = 0
			fc = 0
			bit = 0
			while(temp > 0):
				if(int(data[i][0]) == 1):
					fc = 1
					temp = temp - 1
				else:
					fc = 0
					bit = int(data[i][1])
					temp = temp - int(data[i][2:], 2)
				i += 1
	
	# if(fc == 0):
	# 	print 'fillword ', bit
	# else:
	# 	print 'literal ', data[i-1], data[i-1][r]

def nicefencep(file_name, num):
	fc = open('examples/' + file_name +'.txt')
	fp = open('examples/' + file_name + '_fp.txt')

	if(num%7 == 0):
		n = num/7
		r = 7
	else:
		n = num/7 + 1
		r = num%7


	prev = 1
	res = 1

	p = 1
	offset = 1
	count = 0
	# checking if the we went through the while fencepointer file without finding and any match, so we will use last block as reference.
	check = 0

	for line in fp:
		next1, res1 = line[:-1].split(' ')
		next1 = int(next1)
		res1 = int(res1)
		if (n == next1):
			p = next1
			offset = res1
			check += 1
			break
		elif (n < next1):
			p = prev
			offset = res
			check += 1
			break
		else:
			prev = next1
			res = res1
			count += 1

	if (check == 0):
		p = prev
		offset = res

	#print 'offset', p, offset, count

	with contextlib.closing(mmap.mmap(fc.fileno(), 0, access=mmap.ACCESS_READ)) as m:
		temp = n - p

		m.seek(9*(offset-1))
		block = m.read(9)[:-1]

		if (temp == 0):
			i = 1
			fc = int(block[0])
			bit = int(block[1])
		else:
			i = 1
			fc = 0
			bit = 0

			while (temp > 0):
				block = m.read(9)[:-1]
				if(int(block[0]) == 1):
					fc = 1
					temp = temp - 1
				else:
					fc = 0
					bit = int(block[1])
					temp = temp - int(block[2:], 2)
				i += 1

		# Uncomment this to get results
		if(fc == 0):
			print 'fill ', bit
		else:
		 	m.seek((offset+i-2)*9)
		 	block = m.read(9)[:-1]
		 	print 'literal ', block, block[r]

def getbit(file_name, num):
	fc = open('/home/piyushcs/Desktop/CS698F/output/' + file_name +'.txt')

	if(num%7 == 0):
		n = num/7
		r = 7
	else:
		n = num/7 + 1
		r = num%7

	with contextlib.closing(mmap.mmap(fc.fileno(), 0, access=mmap.ACCESS_READ)) as m:
		temp = n - 1

		block = m.read(9)[:-1]

		if (temp == 0):
			i = 1
			fc = int(block[0])
			bit = int(block[1])
		else:
			i = 1
			fc = 0
			bit = 0

			while (temp > 0):
				block = m.read(9)[:-1]
				if(int(block[0]) == 1):
					fc = 1
					temp = temp - 1
				else:
					fc = 0
					bit = int(block[1])
					temp = temp - int(block[2:], 2)
				i += 1

		# Uncomment this to get results
		# if(fc == 0):
		# 	print 'fill ', bit
		# else:
		# 	m.seek((i-1)*9)
		# 	block = m.read(9)[:-1]
		# 	print 'literal ', block, block[r]


if __name__ == "__main__":
	# comparing getbit and nicefencp
	# start = time.time()
	# n = 40000
	# for i in range(1, 5000):
	# 	getbit(sys.argv[1], int(n+i))

	# print time.time() - start

	# start = time.time()

	# for i in range(1, 5000):	
	# 	nicefencep(sys.argv[1], int(n+i))

	# print time.time() - start
	
	nicefencep(sys.argv[1], sys.argv[2])

	
