num = input()

# collect numbers and place in a list
numbers = input()
numbers = numbers.split(' ')
numbers = list(map(int, numbers))

gaplist = []

# for each number
for i in numbers: 
	highest = 0
	# go through all numbers
	for j in numbers:
		# find the gap
		gap = abs(i-j) 
		# keep track of the highest gap
		if gap > highest: 
			highest = gap
	
	# store the highest gap for each number		
	gaplist.append(highest)

# sort the list in reverse
gaplist.sort(reverse=True)

# print the highest
print(gaplist[0])