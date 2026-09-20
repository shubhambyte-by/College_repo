# Dictionaries:

# student = {
#     "name": "Rahul",
#     "age": 20,
#     "course": "B.Tech IT"
# }

# print(student["name"])

# student["age"] = 21
# student["city"] = "Chennai"

# print(student.get("email", "Not available")) # 

# for key, value in student.items():
#     print(key, ":", value)

# # del student["city"]
# # print(student["city"])


# no name 


numbers = [2, 5, 2, 8, 2, 5]
targets = [2, 5, 8]

for target in targets:
    count = 0
    for value in numbers:
        if value == target:
            count += 1
    print(target, count)
