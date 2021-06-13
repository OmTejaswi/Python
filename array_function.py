numbers = [5,1,3,4,3,6,7]
print(numbers)

# add a number to last of array
numbers.append(20)
print(numbers)

# insert number of specific index
numbers.insert(5,80)
print(numbers)

# to remove specific number from array
numbers.remove(3)
print(numbers)

# remove last item
numbers.pop()
print(numbers)

# get index of item
print(numbers.index(80))

# arrange array in ascending order
numbers.sort()
print(numbers)

# arrange array in descending order
numbers.reverse()
print(numbers)

# make copy of array
numbers2 = numbers.copy()
print(numbers2)

# clear whole array
numbers.clear()
print(numbers)