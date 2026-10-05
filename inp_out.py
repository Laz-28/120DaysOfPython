print("Hello")
print("Name:", "Amina", "Age:", 25)      # multiple values, separated by spaces
print("a", "b", sep="-")                 # a-b  (custom separator)
print("Loading", end="...")             # no new line at the end
print("Done")                            # Loading...Done
print("Line 1\nLine 2")                  # \n = new line
print("Col1\tCol2")                      # \t = tab

age = int(input("Enter your age: "))
price = float(input("Enter price: "))
print(f"Next year you will be {age + 1}")
print(f"The bag costs ksh{price}")


if age > 30:
    if price < 1000:
        print("Too big for that little cash")
    else:
        print("Yeah boy, you are a G")
elif age > 20:
    print("You are in kido")
else:
    print("Invalid")

##Bilt in functions
print(round(3.14159, 3))    # 3.14
print(abs(-7))       # 7
print(min(4, 9, 2))       # 2
print(max(4, 9, 2))       # 9


#Simple interest principle

principal = float(input("Enter the principal amount: "))
rate =  float(input("Enter the rate: "))
time = float(input("Enter the time in years: "))

interest = (principal*rate*time)/100

total = principal + interest

print(f"Interest is {interest}")
print(f"Total amount is {total}")
print(f"Monthly interset is {(interest/(time * 12))}")

#BMI calculator
name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight/(height**2)

print(f"\n{name}, your bmi is {round(bmi, 1)}")
print("Healthy range:", 18.5 <= bmi <= 24.9)