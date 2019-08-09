pangram = input()
pangram = pangram.lower()
letters = "abcdefghijklmnopqrstuvwxyz"

def isPangram(pg):
	for i in letters:
		if i not in pg:
			return False
	return True

print('YES') if isPangram(pangram) else print('NO')