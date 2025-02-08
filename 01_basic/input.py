"""
inputs
"""

name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height: ")
is_adult = input("Are you an adult? ")

print(f"Name: {name} Age: {age} Height: {height} Adult: {is_adult}")

# multiple inputs
country, city = input("Enter your country and city: ").split()

print(f"Country: {country} City: {city}")