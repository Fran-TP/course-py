"""
flow control
"""

# if
age = 18

if age >= 18:
    print("You are an adult")

# if else
name = "Fran"

if name == "John":
    print("You are John")
else:
    print("You are not John")

# if elif else
a = 10
b = 20

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

# nested if
age = 18
is_adult = True

if age >= 18:
    if is_adult:
        print("You are an adult")
    else:
        print("You are not an adult")
else:
    print("You are not an adult")

# ternary operator
result = "You are an adult" if age >= 18 else "You are not an adult"

# short circuit and or
age = 18
is_adult = True

if age >= 18 and is_adult:
    print("You are an adult")

if age >= 18 or is_adult:
    print("You are an adult")

# truthy and falsy conditions
# falsy values: 0, 0.0, '', "", [], {}, (), None, False
# truthy values: everything else not falsy
value = 0

if value:
    print("Truthy")
else:
    print("Falsy")


