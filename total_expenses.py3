num = int(input())
prices = []

# collect price
for _ in range(num):
	x = input()
	prices.append(x)

prices = list(map(int, prices))

# determine payment
for i in prices:
	if i > 1000:
		i = i - (i*0.1)

	# print payment in 2dp
	print("{:.2f}".format(i))