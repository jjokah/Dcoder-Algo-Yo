num = input()

numbers = input().split()
numbers = list(map(int, numbers))

no_of_prime = 0

for i in numbers:
	isprime = True
	
	if i == 1: # 1 is not a prime
		isprime = False
		
	for j in range(2, i):
		if i % j == 0:
			isprime = False
			break
			
	if isprime:
		no_of_prime = no_of_prime + 1
		
print(no_of_prime)