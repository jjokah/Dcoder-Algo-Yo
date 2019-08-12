num = input()
sentence = input()

sentence = sentence.split(" ")
for i in sentence:
	if i == 'Nemo':
		print(sentence.index(i) + 1)