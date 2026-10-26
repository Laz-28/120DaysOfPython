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