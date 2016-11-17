import mmap
import contextlib
import os

input = 'wah'
f = open('/home/piyushcs/Desktop/CS698F/' + input +'.txt')

size = os.stat('/home/piyushcs/Desktop/CS698F/' + input +'.txt').st_size

fw = open(input + '_' + 'fp1.txt', 'w')

fence = []
temp = 0
n = 5
fp = n

prev = 0
next = 0

with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
	i = 0
	while (m.tell() < size):
		block = m.read(9)[:-1]
		if (int(block[0]) == 1):
			temp += 1
			if (fp == temp):
				fw.write(str(fp) + ' ' + str(i+1) + '\n')
				fp += n


		else:
			temp += int(block[2:], 2)
			if (fp < temp):
				if((temp%5) != 0):
					fp = (int(temp/5) + 1) * 5
				else:
					fp = temp
					fw.write(str(fp) + ' ' + str(i+1) + '\n')
					fp += n
		i += 1

fw.close()

fence = []
temp = 0
n = 5
fp = n

prev = 0
next = 0


fw = open(input + '_' + 'fp.txt', 'w')

data = []
for line in f:
	data = line.split(' ')

for i in range(len(data)):
	
	if (int(data[i][0]) == 1):
		temp += 1
		if (fp == temp):
			fw.write(str(fp) + ' ' + str(i+1) + '\n')
			fp += n


	else:
		temp += int(data[i][2:], 2)
		if (fp < temp):
			if((temp%n) != 0):
				fp = (int(temp/n) + 1) * n
			else:
				fp = temp
				fw.write(str(fp) + ' ' + str(i+1) + '\n')
				fp += n

fw.close()
