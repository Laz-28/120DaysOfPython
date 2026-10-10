#Range

for i in range(5):
    print(i)

for x in range(0,10,2):#start,stop,step
    print(x)

for letter in "Python":
    print(letter)

fruits = ["Banana","Apple","Oranges","Coconuts"]

for fruit in fruits:
    print(f"I like {fruit}")

#While loops

count = 1
while count <= 5:
    print(count)
    count += 1

#password checker

password = ""
while password != "#Miniminter22$":
    password = input("Enter password: ")
print("Access Granted")


#Break and continue

for num in range(1,7):
    if num == 5:
        continue#break
    print(num)

#While true

while True:
    answer = input("Enter 'quit' to exit: ")
    if answer == "quit":
        break
    print(f"You have entered {answer}")

#Accumulator patterns

total = 0
for i in range(1,11):
    total += i

print(total)

##Multiplicatioin table
    
number = int(input("Which table do you want? "))

print(f"\nMultiplication table of {number}")
print("-" * 25)

for i in range(1, 13):
    print(f"{number} x {i:2} = {number * i:3}")

##Numbers guessing game
import random

secret = random.randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You got it in {attempts} attempts.")
        break