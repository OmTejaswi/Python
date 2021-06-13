# split duplicate from array
numbers = [5,4,1,5,7,6,5,2,1,3,4,5,7,8,6,5,3,8,6]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print(numbers)
print(unique)