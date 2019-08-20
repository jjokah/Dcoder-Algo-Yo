num = int(input())

digitslist = []

for i in range(num):
	digits = input()
	digitslist.append(digits)

for i in digitslist:
	ifirst = int(i[0])
	ilast = int(i[(len(i)-1)])
	firstandlast = ifirst + ilast
	print(firstandlast)
