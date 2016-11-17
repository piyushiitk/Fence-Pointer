import random

numbers = [10, 20, 30, 40, 50, 60, 70, 80] * 100000



fw = open('project.txt', 'w')


for i in range(5):
	
	data = random.sample(numbers, 10000)

	data.extend([10] * 63)
	
	data = random.sample(numbers, 10000)
	
	data.extend([10] * 63)
	
	data = random.sample(numbers, 10000)
	
	data.extend([10] * 63)
	
	data = random.sample(numbers, 10000)
	
	data.extend([10] * 63)
	
	data = random.sample(numbers, 60000)

	fw.write('[C'+ str(i) + '] ')
	
	for item in data:
		fw.write('%s ' % item)
	
	fw.write('\n')
	
fw.close()
