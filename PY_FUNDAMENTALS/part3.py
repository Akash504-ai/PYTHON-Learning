# --------------- PYTHON LISTS -------------- #
list = [10,20,30,40,50,60,70,80,90,100]
print (list, type(list))

# List can contain diff data types 
student = ["Akash", 21, 7.07, True]
print(student)

# indexing
print(list[0])
print(list[3])
print(list[7])
# Negative indexing starts from the end
print(list[-1])

# Slicing ---> list_name[start:stop:step]
print(list[0:5:2]) # [10, 30, 50]

# Modifying list elements is also possible

# Operations
num = [10,20,30,40,50]
num.append(60) # add one element at the end
print(num)
num.extend([70,80])
print(num) # add multiple elements
num.insert(0,5)
print(num) # add an element at a specific index
num.remove(5)
print(num) # remove by value
del num[1]
print(num)
del num[0:2]
print(num)
num.clear() # remove everything
print(num) # []

# Sorting and reversing
numbers = [50, 10, 40, 20, 30]
numbers.sort()
print(numbers)  # [10, 20, 30, 40, 50]
numbers.sort(reverse=True)
print(numbers)  # [50, 40, 30, 20, 10]

# reverse the existing order
numbers = [10, 20, 30, 40]
numbers.reverse()
print(numbers)  # [40, 30, 20, 10]
print(len(numbers))