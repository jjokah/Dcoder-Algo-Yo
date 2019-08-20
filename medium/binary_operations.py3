# collect binary numbers
x, y = input().split()

# convert to python binary format
x = '0b' + x
y = '0b' + y

# convert binary to decimal
x = int(x, 2)
y = int(y, 2)

# calculate
mysum = x + y
myproduct = x * y

# convert decimal to binary
mysum = bin(mysum)
myproduct = bin(myproduct)

# convert to readable format
mysum = mysum[2:len(mysum)]
myproduct = myproduct[2:len(myproduct)]

print(mysum)
print(myproduct)