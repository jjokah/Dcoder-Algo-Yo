testcase = int(input())

def largenum():
	num = input()
	digits = input() # collect digits
	digits = digits.split(' ') # place in list
	
	digits.sort(reverse=True) # sort list in reverse
	digits = "".join(digits) # join list items
	digits = int(digits) # change str to int
	
	print(digits)

for i in range(testcase):
	largenum()
