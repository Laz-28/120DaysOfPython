# What is a module?
#A module is simply a Python file containing code (functions, variables, classes) that you can reuse in other files.

#Importing
import math

print(math.sqrt(16))      # 4.0
print(math.pi)            # 3.141592653589793

#Different ways to import
import math                       # use as math.sqrt()
import math as m                  # alias: m.sqrt()
from math import sqrt, pi         # import specific names: sqrt()
from math import *                # imports everything (avoid: causes name clashes)

#Useful standard library modules
##math
import math

math.sqrt(25)       # 5.0
math.ceil(4.1)      # 5 (round up)
math.floor(4.9)     # 4 (round down)
math.factorial(5)   # 120
math.pow(2, 3)      # 8.0
math.gcd(12, 18)    # 6
math.pi             # 3.14159...

##random
import random

my_list = [3,4,1,7,6]

print(random.randint(1, 10))              # random int from 1 to 10 (inclusive)
print(random.random())                    # random float from 0 to 1
print(random.choice(["a", "b", "c"]))     # pick one item
print(random.sample(range(1, 50), 6))    # pick 6 unique items
random.shuffle(my_list)                  # shuffle a list in place
print(random.uniform(1.5, 5.5))          # random float in a range

print(my_list)



#Date time
from datetime import datetime, date, timedelta

now = datetime.now()
print(now)                                  # 2026-10-28 14:30:12.123456
print(now.strftime("%d/%m/%Y %H:%M"))       # 28/10/2026 14:30
print(now.year, now.month, now.day)

today = date.today()
next_week = today + timedelta(days=7)

birthday = datetime.strptime("2000-05-14", "%Y-%m-%d")   # string → datetime
age_days = (now - birthday).days