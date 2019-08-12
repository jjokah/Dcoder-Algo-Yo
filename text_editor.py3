num = int(input())
wordlist = []

# collect words and place in list
for i in range(num):
	word = input()
	wordlist.append(word) 

# capitalize each item
for i in range(len(wordlist)):
	wordlist[i] = wordlist[i].upper()

# print each item
for i in wordlist:
	print(i)