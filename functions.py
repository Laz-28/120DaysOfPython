##A function is a named block of code that you can reuse
def greet(name):
    print(f"Hello {name}")

greet("Lazaro")

##Default parameters

def greet2(name, greeting = "Hello"):
    return f"{greeting} {name}"

print(greet2("Otieno", "Hi"))
print(greet2("Amina"))

##Keyword arguments
def describe(name, age, city):
    return f"{name}, {age}, from {city}"

print(describe(city="Thika", name="Amina", age=25))

##*args and *kwargs
def total(*numbers):
    return sum(numbers)

print(total(1,2,3,4,5,6))

def show(**info):
    for key, value in info.items():
        print(f"{key} : {value}")

show(name="Farhiya", age = 21)

##Docstrings

def area(length, width):
    """Return the area of a rectangle."""
    return length * width

help(area)             # shows the docstring

##Functions calling functions
def square(n):
    return n*n

def sum_of_squares(a,b):
    return square(a)+square(b)

print(sum_of_squares(23,24))

##Passing lists
def add_item(items):
    items.append("new")        # changes the ORIGINAL list

my_list = ["a"]
add_item(my_list)
print(my_list)                 # ['a', 'new']

