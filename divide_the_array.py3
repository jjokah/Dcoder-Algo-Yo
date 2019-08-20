numsize = input()

# collect numbers and place in list
numbers = input()
numbers = numbers.split(' ')
numbers = list(map(int, numbers))

evenlist = []

for i in range(1, len(numbers)+1): # 1-indexed list
	if i % 2 == 0: # check if index is even
		if numbers[i-1] % 2 == 0: # check if actual index element is even (0-indexed)
			evenlist.append(numbers[i-1]) # add element to evenlist

# change numbers in list to str and then join
evenlist = list(map(str, evenlist))
evenlist = " ".join(evenlist)

print(evenlist)