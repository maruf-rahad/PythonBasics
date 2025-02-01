names = ["Tourist", "Peter", "John", "Doe"]
print(names)
# print 1st element of the list
print(names[0])
# print last element of the list
print(names[len(names)-1])
# - represent from the last
print(names[-1])
# print second last element of the list
print(names[-2])
# replace 1st element of the list
names[0] = "Maruf"
print(names)
# print 1 <= index < 3
print(names[1:3])

numbers = [1, 2, 3, 4, 5]
print(numbers)
# add new element at the last
numbers.append(6)
print(numbers)
# add new element in specific index
numbers.insert(2, 222)
print(numbers)
# add one string in the 4th index
numbers.insert(3, "abc")
print(numbers)
# remove 222
numbers.remove(222)
print(numbers)
# print the length of numbers
print(len(numbers))

