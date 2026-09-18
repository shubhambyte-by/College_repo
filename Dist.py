# Dictionaries:

student = {
    "name": "Rahul",
    "age": 20,
    "course": "B.Tech IT"
}

print(student["name"])

student["age"] = 21
student["city"] = "Chennai"

print(student.get("email", "Not available")) # 

for key, value in student.items():
    print(key, ":", value)

# del student["city"]
# print(student["city"])

