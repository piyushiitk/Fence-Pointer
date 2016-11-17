input = 'wah'
fc = open('/home/piyushcs/Desktop/CS698F/' + input +'.txt')
fp = open('/home/piyushcs/Desktop/CS698F/' + input + '_fp.txt')

num = raw_input('Enter number\n')
num = int(num)

n = int(num/7)
r = int(num%7)
if(r != 0 ):
	n = n + 1

print n, r

prev = 1
res = 1

p = 1
offset = 1
count = 0 

for line in fp:
	next1, res1 = line[:-1].split(' ')
	next1 = int(next1)
	res1 = int(res1)
	if (n == next1):
		p = next1
		offset = res1
		break
	elif (n < next1):
		p = prev
		offset = res
		break
	else:
		prev = next1
		res = res1
		count += 1


if (count == 2):
	p = next1
	offset = res1

print 'offset', p, offset, count

for line in fc:
	temp = n - p

	data = line.split(' ')[offset-1:]
	data[-1] = data[-1][:-1]

	print 'temp is ', temp
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


# with contextlib.closing(mmap.mmap(fc.fileno(), 0, access=mmap.ACCESS_READ)) as m:
# 	temp = n - p

# 	m.seek(9*(offset-1))
# 	block = m.read(9)[:-1]

# 	if (temp == 0):
# 		i = 1
# 		fc = int(block[0][0])
# 		bit = int(block[0][1])
# 	else:
# 		i = 0
# 		fc = 0
# 		bit = 0

# 		while (temp > 0):
# 			block = m.read(9)[:-1]
# 			if(int(block[i][0]) == 1):
# 				fc = 1
# 				temp = temp - 1
# 			else:
# 				fc = 0
# 				bit = int(block[i][1])
# 				temp = temp - int(data[i][2:], 2)
# 			i += 1





if(fc == 0):
	print 'fillword is ', bit
else:
	print 'litral word is ', data[i-1], data[i-1][r]

# if(fc == 0):
# 	print 'fill ', bit
# else:
# 	m.seek((offset+i-1)*9)
# 	block = m.read(9)[:-1]
# 	print 'litral ', block, block[r]
