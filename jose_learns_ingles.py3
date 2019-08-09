num = int(input())
word = input()
word = word.split(' ')

for _ in range(num):
	for i in range(num-1):
		if word[i].lower() > word[i+1].lower():
			word[i], word[i+1] = word[i+1], word[i]
			
print(" ".join(word))
	