"""
Range in py
"""

# range(stop)
# range(start, stop)
# range(start, stop, step)

# range(stop)
# The range(stop) function generates a sequence of numbers from 0 to stop - 1.
# The default value of start is 0 and step is 1.
# The stop value is mandatory.

# Example
# Generate a sequence of numbers from 0 to 4
for i in range(5):
    print(i)

# range(start, stop)
# The range(start, stop) function generates a sequence of numbers from start to stop - 1.

# Example
# Generate a sequence of numbers from 2 to 4
for i in range(2, 5):
    print(i)

# range(start, stop, step)
# The range(start, stop, step) function generates a sequence of numbers from start to stop - 1 with a step value.
# The step value is optional and the default value is 1.

# Example
# Generate a sequence of numbers from 2 to 10 with a step value of 2
for i in range(2, 11, 2):
    print(i)

# The range() function is commonly used in for loops to iterate over a sequence of numbers.

# Example
# Print the square of numbers from 1 to 5
for i in range(1, 6):
    print(i**2)

# The range() function is also used to generate a sequence of numbers and convert it into a list.

# Example
# Convert the range object to a list
numbers = list(range(5))
print(numbers)  # [0, 1, 2, 3, 4]

# Example
# Convert the range object to a list
numbers = list(range(2, 5))
print(numbers)  # [2, 3, 4]