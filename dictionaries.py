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


if "name" in student:
    print("Has name")

