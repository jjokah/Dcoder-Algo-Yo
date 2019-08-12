no_of_string = input()
my_string = input()
my_list = []

for letter in my_string:
	for i in range(3):
		my_list.append(letter)

my_string2 = "".join(my_list)

# print(no_of_string)
print(my_string2)
