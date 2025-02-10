"""
List in Python
"""
# List of integers
my_list = [1,2,3,4,5]

# list of strings
my_list_str = ['apple', 'banana', 'cherry']

# list of mixed data types
my_list_mixed = [1, 'apple', 2, 'banana']

# Empty list
empty_list = []

# Nested list
nested_list = [['apple', 'banana'], [1, 2, 3]]

# Matrix list
Matrix_list = [[1,2], [3,4], [5,6]]

# Accessing elements in a list
print(my_list[0])  # 1
print(my_list[1])  # 2
print(my_list[-1])  # 5

# Slicing a list
print(my_list[1:3])  # [2, 3]

# reverse a list
print(my_list[::-1])  # [5, 4, 3, 2, 1]

# methods in list
# append() - add an element to the end of the list
my_list.append(6)
print(my_list)  # [1, 2, 3, 4, 5, 6]

# insert() - add an element at a specific index
my_list.insert(2, 7)
print(my_list)  # [1, 2, 7, 3, 4, 5, 6]

# extend() - add elements of a list to another list
my_list.extend([8, 9])

print(my_list)  # [1, 2, 7, 3, 4, 5, 6, 8, 9]

# remove() - remove the first occurrence of an element
my_list.remove(7)

print(my_list)  # [1, 2, 3, 4, 5, 6, 8, 9]

# pop() - remove an element at a specific index

my_list.pop(2)

print(my_list)  # [1, 2, 4, 5, 6, 8, 9]

# clear() - remove all elements from the list
my_list.clear()

print(my_list)  # []

# index() - return the index of the first occurrence of an element

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(my_list.index(3))  # 2

# count() - return the number of occurrences of an element
print(my_list.count(3))  # 1

# sort() - sort the elements of a list
my_list.sort()
# sort in descending order
my_list.sort(reverse=True)

print(my_list)  # [9, 8, 7, 6, 5, 4, 3, 2, 1]

# reverse() - reverse the elements of a list
my_list.reverse()

print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# copy() - return a shallow copy of the list
new_list = my_list.copy()

print(new_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List comprehension
# create a list of squares of numbers from 1 to 5
squares = [i**2 for i in range(1, 6)]

print(squares)  # [1, 4, 9, 16, 25]

# create a list of square with map
squares = list(map(lambda x: x**2, range(1, 6)))

print(squares)  # [1, 4, 9, 16, 25]
