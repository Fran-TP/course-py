"""
operators in python
"""

# Arithmetic operators
a = 10
b = 20

print(a + b)  # 30

print(a - b)  # -10

print(a * b)  # 200

print(a / b)  # 0.5

print(a % b)  # 10

print(a ** b)  # 100000000000000000000

print(a // b)  # 0

# Comparison operators
a = 10
b = 20

print(a == b)  # False

print(a != b)  # True

print(a > b)  # False

print(a < b)  # True

print(a >= b)  # False

print(a <= b)  # True

# Logical operators

a = True
b = False

print(a and b)  # False

print(a or b)  # True

print(not a)  # False

# Bitwise operators
a = 10
b = 20

print(a & b)  # 0

print(a | b)  # 30

print(a ^ b)  # 30

print(~a)  # -11

print(a << 2)  # 40

print(a >> 2)  # 2

# Assignment operators
a = 10
b = 20

a += b
print(a)  # 30

a -= b
print(a)  # 10

a *= b
print(a)  # 200

a /= b
print(a)  # 10.0

a %= b
print(a)  # 10.0

a **= b
print(a)  # 100000000000000000000

a //= b
print(a)  # 5000000000000000000

# Identity operators
a = 10
b = 20

print(a is b)  # False

print(a is not b)  # True

# Membership operators
a = [1, 2, 3, 4, 5]

print(1 in a)  # True

print(6 not in a)  # True

# Ternary operator
a = 10
b = 20

min = a if a < b else b

print(min)  # 10

# Operator precedence

a = 10
b = 20
c = 30
d = 40

print(a + b * c / d)  # 25

print((a + b) * c / d)  # 15.0

print(((a + b) * c) / d)  # 15.0


