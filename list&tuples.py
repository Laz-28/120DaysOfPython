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

##Removing items
fruits.remove("banana")        # remove by value (first match)
last = fruits.pop()            # remove and return the last item

print(fruits)
second = fruits.pop(1)         # remove and return item at index 1

print(fruits)
del fruits[0]                  # delete by index
fruits.clear()                 # empty the list

print(fruits)