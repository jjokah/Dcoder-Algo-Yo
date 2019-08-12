no_of_letters = input()
word = input()
index = input()

word = list(word) # change to list
index = index.split(" ") # change to list and remove space
index = list(map(int, index)) # change list values to integer

for i in index:
	i = int(i) # turn i from str to int
	word[i] = word[i].lower() if word[i].isupper() else word[i].upper()
	

word = "".join(word)

print(word)