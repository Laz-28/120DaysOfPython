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