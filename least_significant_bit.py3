testcase = int(input())
numbers = []

for _ in range(testcase):
	x = input()
	numbers.append(x)

for i in numbers:
	if int(i) % 2 == 0:
		print('No')
	else:
		print('Yes')