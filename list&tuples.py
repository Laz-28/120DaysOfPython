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

#Searching and counting
nums = [5, 3, 8, 3, 1]

print(3 in nums)          # True
print(nums.index(8))      # 2 (position of first match)
print(nums.count(3))      # 2

#Sorting and reversing
nums = [5, 3, 8, 1]

nums.sort()                    # sorts in place: [1, 3, 5, 8]
nums.sort(reverse=True)        # [8, 5, 3, 1]
nums.reverse()                 # flips the order in place

sorted_nums = sorted(nums)     # returns a NEW sorted list, original unchanged


#Built ins
nums = [4, 9, 2, 7]

print(len(nums))     # 4
print(sum(nums))     # 22
print(min(nums))     # 2
print(max(nums))     # 9


##Looping through lists
colors = ["red", "green", "blue"]

for color in colors:
    print(color)

# Need the index too? Use enumerate()
for i, color in enumerate(colors):
    print(i, color)             # 0 red, 1 green, 2 blue

for i, color in enumerate(colors, start=1):
    print(f"{i}. {color}")      # 1. red, 2. green, 3. blue