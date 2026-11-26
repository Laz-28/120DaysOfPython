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
from pathlib import Path

# Linux: uncomment this and comment out the next line when running on Linux.
# path = Path("/home/otieno-lazaro/words.txt")
path = Path(__file__).with_name("words.txt")

if path.exists():
    print("Found it")

else:
    print("file not found")
    

##Modern alternative

print(path.exists())
path.write_text("Hello", encoding="utf-8")
print(path.read_text(encoding="utf-8"))

##File paths

# open("notes.txt")                       # same folder as where you RUN the program
# open("data/notes.txt")                  # subfolder
# open(r"C:\Users\Amina\notes.txt")       # absolute path (r"" avoids backslash trouble)


##Encoding
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Habari ya asubuhi ☀️")

##CSV files
import csv

rows = [
    ["name", "age", "city"],
    ["Amina", 25, "Nairobi"],
    ["Brian", 30, "Mombasa"],
]

with open("people.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# with open("people.csv", newline="", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)                  # ['Amina', '25', 'Nairobi']

with open("people2.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    person = {"name": "Cate", "age": 22}
    writer.writerow(person)
    print(person["name"], person["age"])


with open("people.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["city"])      # values are always strings!

