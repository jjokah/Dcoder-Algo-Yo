# Check Examples

#python 3.7.1

no_of_integer = int(input())
integers = input()

int_list = integers.split(" ")
int_list = list(map(int, int_list))

int_list.sort()

highest_int = int_list[no_of_integer - 1]


print(sum(int_list) % highest_int)
