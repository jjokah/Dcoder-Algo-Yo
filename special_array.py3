import math

num = input()
myarray = input()

myarray = myarray.split(' ')
myarray = list(map(int, myarray))

def isNatural(myarr):
	for i in myarr:
		if i <= 0 or (i != math.trunc(i)):
			return False
	return True

print('Yes') if isNatural(myarray) else print('No')
