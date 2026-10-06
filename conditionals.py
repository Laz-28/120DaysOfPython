# Grade calculator
name = input("Enter your name: ")
math = float(input("Enter math score: "))
english = float(input("Enter english score: "))
science = float(input("Enter science score: "))

average = (math+english+science)/3

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print(f"{name}'s average is {round(average, 1)}")
print(f"Grade: {grade}")

if grade == "F":
    print("See your teacher immediately")
else:
    print("Well done!")

##Leap year

year = int(input("Enter a year: "))

if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")

