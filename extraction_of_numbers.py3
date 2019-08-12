num = input()
sentence = input()
output = []

for i in sentence:
	if i.isdigit():
		output.append(i)

output = " ".join(output)
print(output)