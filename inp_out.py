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



