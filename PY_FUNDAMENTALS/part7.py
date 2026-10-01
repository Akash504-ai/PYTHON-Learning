# String
text = "  Hello Python  "
print(text.strip())

# Exception handling
try:
    num = int(input("Enter a number: "))
    result = 100 // num
except ValueError:
    print("INVALID")

except ZeroDivisionError:
    print("Can't")

else:
    print(result)

finally:
    print("Successfull")