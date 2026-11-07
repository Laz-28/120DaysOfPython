file = open("notes.txt", "w")
file.write("Hello\n")
file.close()

##Safen way to use to avoid data lose
with open("notes.txt", "w") as file:
    file.write("Hello\n")

# file modes
# "r"	Read (default)
# "w"	Write
# "a"	Append
# "x"	Create only
# "r+"	Read and write

with open("notes.txt", "w") as f:
    f.write("line 1\n")
    f.write("line 2\n")
    f.writelines(["A\n", "B\n"])

with open("notes.txt", "a") as f:
    f.write("line 3\n")

with open("notes.txt", "a") as f:
    print("Line 4", file=f)


##Reading 
with open("notes.txt", "r") as f:
    content = f.read()              # whole file as one string

with open("notes.txt") as f:
    lines = f.readlines()           # list of lines (with \n)

with open("notes.txt") as f:
    first = f.readline()            # one line at a time


with open("notes.txt") as f:
    for line in f:
        print(line.strip())         # strip() removes the trailing \n

with open("notes.txt") as f:
    lines = f.read().splitlines()  ##Lines in a list

print(lines)


##Checking if a file exists
import os

if os.path.exists("/home/otieno-lazaro/words.txt"):
    print("Found it")

else:
    print("file not found")
    

##Modern alternative

from pathlib import Path

path = Path("/home/otieno-lazaro/words.txt")
print(path.exists())
print(path.read_text())
path.write_text("Hello")

##File paths

open("notes.txt")                       # same folder as where you RUN the program
open("data/notes.txt")                  # subfolder
open(r"C:\Users\Amina\notes.txt")       # absolute path (r"" avoids backslash trouble)


##Encoding
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Habari ya asubuhi ☀️")

