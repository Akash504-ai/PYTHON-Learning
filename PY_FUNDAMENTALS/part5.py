# ===== Python Dictionaries ===== #
student = {
    "name" : "Akash",
    "age" : 21,
    "cpga" : 7.07,
    "branch" : "CSBS"
}
print(student)
print(type(student))
print(student["name"])
print(student["age"])

# get() is useful when a key might not exist.
# print(student["height"]) # KeyError
print(student.get("height","N/A"))
print(student.get("city","N/A"))

# adding a new key
student["city"] = "Belda"
print(student)
# Update an existing key
student["age"] = 25
print(student)

# Remove a specific key
del student["cpga"]
print(student)

# Remove the last inserted key-value pair
# student.popitem()

# Remove all entries
# student.clear()

student = {
    "name": "Akash",
    "age": 21,
    "cgpa": 7.07
}

print(student.keys())
print(student.values())
print(student.items())

