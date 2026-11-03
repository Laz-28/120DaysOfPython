# mytools.py
def square(n):
    return n * n

def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

# mytools.py
def square(n):
    return n * n

if __name__ == "__main__":
    print(square(4))      # runs only when you run mytools.py itself

import math
print(dir(math))        # list everything inside
help(math.sqrt)         # read the documentation
