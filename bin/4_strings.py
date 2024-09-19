"""
 Strings:
        -- We have option to store collection of characters like name, email-id etc
        -- Automatically index number will be assigned to each char
"""

print("Strings PART-1")
print("How to store values")
print("-"*20)
# ------------

a = 'WEL COME'
# Internally it will create object of 'str' class and store the values

# OR
b = str('WEL COME')

print(a, b)

print("#"*40, end="\n\n")
#################################


print("Strings PART-2")
print("How to store values")
print("-"*20)
# ------------

a = 'PERSON'
b = 'PERSON\'S'
c = "PERSON'S"
d = """PERSON'S HEIGHT IS XYZ" ( " represents inches)"""
e = '''PERSON'S HEIGHT IS XYZ" ( " represents inches)'''

print(a, b, c, d, e, end="\n\n")

print(a, b, c, d, e, sep="\n")


print("#"*40, end="\n\n")
#################################

print("Strings PART-3")
print("How to store values")
print("-"*20)
# ------------

a = "C:\newfolder\test.py"
# Bydefault: few chars with \ will be special meaning ex: \n -> replaced with newlinfe

print("Value of 'a' = ", a, end="\n\n")

b = r"C:\newfolder\test.py"
# r - > raw string,
print("Raw string 'b' = ", b, end="\n\n")

print("Converting a to raw string:", repr(a))

print("#"*40, end="\n\n")
#################################

print("Strings PART-4")
print("How to store values")
print("-"*20)
# ------------

x = 10
y = 20
z = x + y

my_string = f"add of {x} and {y} is {z}"
# f - > format
# f -> it will replace {variable name} with value
print("my_string:", my_string)

print("#"*40, end="\n\n")
#################################

print("Strings PART-5")
print("Indexes: Access each character using index number")
print("-"*20)
# ------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 5_strings.xlsx Section-1

print("0th character using +ve index number:", my_string[0])
print("0th character using -ve index number:", my_string[-8])

# print("100th character using +ve index number:", my_string[100]) # ERROR

print("#"*40, end="\n\n")
#################################

print("Strings PART-6")
print("Slicing: Pull substring")
print("-"*20)
# ------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 5_strings.xlsx Section-2

print("substring from index-1 to index-6 using +ve index number:", my_string[1:6])
print("substring from index-1 to index-6 using -ve index number:", my_string[-7:-2], end="\n\n")
# Default behavior, character at last index will not come

print("substring from index-1 to END using +ve index number:", my_string[1:])
print("substring from index-1 to END using -ve index number:", my_string[-7:], end="\n\n")

print("substring from BEGINNING to index-6 using +ve index number:", my_string[:6])
print("substring from BEGINNING to index-6 using -ve index number:", my_string[:-2], end="\n\n")


print("#"*40, end="\n\n")
#################################

print("Strings PART-7")
print("Step Value: We can skip values")
print("-"*20)
# ------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 5_strings.xlsx Section-3

print("substring from index-1 to index-6 using +ve index number:", my_string[1:6:2])
print("substring from index-1 to index-6 using -ve index number:", my_string[-7:-2:2], end="\n\n")


print("#"*40, end="\n\n")
#################################


print("Strings PART-8")
print("-ve Step Value: We can traverse in reverse direction")
print("-"*20)
# ------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 5_strings.xlsx Section-4

# Steps
# Example: index- 6 to 1 in reverse direction
# start index should be : 6
# end index should be: 1
# step value should be -ve value

print("sub string from index 6 to 1 using +ve index number:step by -1", my_string[6:1:-1])
print("sub string from index 6 to 1 using -ve index number:step by -1", my_string[-2:-7:-1], end="\n\n")

print("sub string from index 6 to 1 using +ve index number:step by -2", my_string[6:1:-2])
print("sub string from index 6 to 1 using -ve index number:step by -2", my_string[-2:-7:-2], end="\n\n")

print("#"*40, end="\n\n")
#################################

print("Strings PART-9")
print("Methods/Variables present inside 'str' class")
print("-"*20)
# ------------

# my_string = "WEL COME"
# print(dir(my_string))

# OR

print(dir(str))

print("#"*40, end="\n\n")
#################################

print("Strings PART-10")
print("Special Names which is starting with __ & ends with __")
print("-"*20)
# ------------

s1 = "Hello"
s2 = "python"
concat_result = s1 + s2 # internally + mapped-to/calls __add__ defined inside str class
length_of_s1 = len(s1) # Internally len() function calls __len__ defined inside str class

print("concat_result:", concat_result)
print("length_of_s1:", length_of_s1)

print("#"*40, end="\n\n")
#################################

print("Strings PART-11")
print("'startswith()' method")
print("-"*20)
# ------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

startswith_result = my_string.startswith("WEL") # True/False
print("startswith_result:", startswith_result)

print("#"*40, end="\n\n")
#################################
