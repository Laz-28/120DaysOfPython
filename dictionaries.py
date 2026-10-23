##What is a dictionary : A dictionary stores values in keys and pairs, stores data as key:value pairs, you look up things by meaningful key rather than position
student = {
    "name" : "Amina",
    "age":20,
    "course":"python",
    "is_active": True
}

print(student["name"])
print(student.get("age"))
print(student.get("phone","N/A")) ##N/A is used as a default

##Adding and removing

student["city"] = "Nairobi"
student["age"] = 21
student.update({"age":22, "grade":"A"})

print(student)



print(student)
age = student.pop("age")
print(student)

print(len(student))


##Looping through dictionaries
if "name" in student:
    print("Has name")

for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(f"{key} : {value}")

##Dictionary methods summary

prices = {"apple": 50, "banana": 20, "mango": 80}
prices.keys()      # dict_keys(['apple', 'banana', 'mango'])
prices.values()    # dict_values([50, 20, 80])
prices.items()     # dict_items([('apple', 50), ...])
list(prices.keys())            # convert to a normal list
sorted(prices)                 # sorted keys
sorted(prices.items(), key=lambda item: item[1])   # sort by value (lambda is Lesson 12)

##Nested dictionaries and lists in dictionaries

students = {
    "amina":{"age":20,"scores": [85,90,78]},
    "brian":{"age":22,"scores":[70,65,88]}
}

print(students["amina"]["age"])
print(students["brian"]["scores"][0])

students["cate"] = {"age":21, "scores":[]}
students["cate"]["scores"].append(95)

##Counting pattern
text = "banana"
counts = {}

for ch in text:
    if ch in counts:
        counts[ch] += 1
    else:
        counts[ch] = 1

print(counts)

##Sets  - removing duplicates
numbers = {1, 2, 3, 3, 2}
print(numbers)                   # {1, 2, 3} (duplicates gone)

empty_set = set()                # NOT {} (that makes an empty dictionary)
letters = set("hello")           # {'h', 'e', 'l', 'o'}


