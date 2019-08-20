num = int(input())
markslist = []

for i in range(num):
	marks = input()
	markslist.append(marks)

for i in markslist:
	x, y = i.split()
	x, y = int(x), int(y)
	if x > 70 and y > 50:
		print('Pass')
	else:
		print('Fail')