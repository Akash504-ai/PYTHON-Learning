# age = (input("Enter your age : ")) # type ---> str

# age = int(input("Enter your age : ")) # type ---> int

# print(age, type(age))

# string operations
name = "Akash"
print(name.upper())
print(name.lower())
print(name.find("ash")) # checks is the substring 
                        # exist and then return idx
                        # for this idx ---> 2
print(name.find("B"))   # for this idx ---> -1
print(name.replace("Akash", "Santra"))
# check presence
print("A" in name) # True ---> "A" is present in 
                   #           name string 
print("B" in name) # False


# OPERATOR PRECENDENCE [BODMAS]
# ans = (2 + 3) * 5
# print(ans)


# logical operators are written as ---> 
# or, and, not


# Loops
# n = int(input("Enter a no : "))

# i = 1

# while i <= 10:
#     print(n * i)
#     i = i + 1


# Non-primitive data types
# List - Mutable
marks = [98, 99, 97, 95, 93, "A", 69.69]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
marks.append(25)
marks.insert(0,50) # appending at 1st idx
print(marks)

# Tuple - immutable
marks = (98, 99, 97, 95, 93, 95, 95)
print(marks.count(95))
print(marks.index(95)) # ---> first idx

# Set => unique items collection
marks = {98, 97, 95, 96, 95, 96}
print(marks)
print(len(marks))


# Dictionary {key => val}
marks = {
    "Maths" : 99,
    "Physics" : 98,
    "English" : 89
}
print(marks)
print(type(marks))
print(marks["Physics"])


