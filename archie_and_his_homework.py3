# collect str input and place in list
myfraction = input()
myfraction = myfraction.split(' ')
myfraction = list(map(int, myfraction))

'''
myfraction[0] = numerator
myfraction[1] = denominator
'''

# check highest number divisble by numerator and denominator
for i in range(myfraction[0], 1, -1):
	if (myfraction[0] % i == 0) and (myfraction[1] % i == 0):
		myfraction[0] = myfraction[0] // i
		myfraction[1] = myfraction[1] // i

# change list to str
myfraction = list(map(str, myfraction))
myfraction = ' '.join(myfraction)
print(myfraction)
	
