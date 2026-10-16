##Slicing and indexing
fruits = ["apple", "banana", "mango", "orange"]

print(fruits[0])       # apple
print(fruits[-1])      # orange
print(fruits[1:3])     # ['banana', 'mango']
print(fruits[::-1])    # reversed list
print(len(fruits))     # 4

##Adding items
fruits.append("grape")         # add to the end
fruits.insert(1, "kiwi")       # insert at index 1
fruits.extend(["pear", "plum"])  # add several items

print(fruits)
