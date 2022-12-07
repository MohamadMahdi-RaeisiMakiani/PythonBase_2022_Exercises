from math import radians
from math import pi

# We have many datatypes in Python, such as:
# - String (str) ---> "Hello, world!"
# - Integer Numbers(int) -n, 0, n
# - Float Numbers (float) -n.m, 0, n.m
# - Complex [1j, 2j, ...] (complex) -nj, 0, nj
# - | [n = 1, 2, 3, 4, 5, 6, 7, 8, 9] - [m = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# - Boolean (bool)
# - Byte (bytes)
# - Arrays (list, tuple, dict, set) | Group1_DataTypes : all data types above
# - list: [Group1_DataTypes1, Group1_DataTypes2, Group1_DataTypes3, ...]
# - tuple: (Group1_DataTypes1, Group1_DataTypes2, Group1_DataTypes3, ...)
# - set: {Numeric_DataTypes1, Numeric_DataTypes2, Numeric_DataTypes3, ...}
# - dict: {key1 : value1, key2 : value2, key3 : value3, ...} | Dictionary | key, value: include Group1_DataTypes
# -----------------------------------------------------
# We have many built-in functions for each data type in Python such as:
# - user_name = "Jack" ---> type(user_name), user_name.upper()

if radians(60) == pi/3:
    print("radians : pi/3 = {}".format(round(pi/3, 2)))

# string variables
name_of_customer = "Sarah"
name_of_customer_2 = "alex"
other_name_1 = "Jack"
other_name_2 = "Jason Lee is 32"
other_name_3 = "Mark+Manson+is+a+Good+Writer"
other_name_4 = "Mark\nJason\nSarah\nAlex\nJack"
other_name_5 = "          Arnold Brown            "
other_name_6 = "++/*Sam Whitexxx,,,,..."
other_name_7 = "mIchELLE tWiNn"
numeric_string_1 = "123"
alphanumeric_string_1 = "Mona25"
sentense_string_1 = "hi im the first person in this room."


# this string built-in function changes the first alphabet character of string to capital
print(name_of_customer_2.capitalize())

# Make a string with 16 characters and place the 'alex' at the center
print(name_of_customer_2.center(16))

# count a character in the string
print(name_of_customer.count("a"))

# encode(encoding="ascii",errors="backslashreplace")
# errors : [backslashreplace - ignore - namereplace - strict - replace - xmlcharrefreplace]
print(name_of_customer.encode())

# Check a string end character and first character
print(name_of_customer.endswith("h"))
print(name_of_customer.startswith("h"))

# make tabs free spaces bigger or smaller
print(f"\t{name_of_customer}".expandtabs(16))

# find the character placement
print(name_of_customer_2.find("e"))

# make the string uppercase
print(name_of_customer_2.upper())

# it's like find but if we don't have the character it returns value error
# print(name_of_customer_2.index("b")) ---> Value Error
print(name_of_customer_2.index("l"))

# check the string if it is alphanumeric
print(alphanumeric_string_1.isalnum())

# check the string if it is alphabet [just words]
print(other_name_1.isalpha())
print(numeric_string_1.isalpha())
print(alphanumeric_string_1.isalpha())

# check the string if it is special type | isascii, isdecimal, isdigit, islower, isupper,
#   isnumeric, isprintable, isspace, istitle | ascii, decimal, integer numbers, small alphabet, capital alphabet
#       float numbers, able to print, just free space, title such as Book Store Library
print(numeric_string_1.isdigit())
print(alphanumeric_string_1.isdigit())

# add free space at left side of the string
print(f"{other_name_1.ljust(8)}finish.")

# add free space at right side of the string
print(f"{other_name_1.rjust(8)}finish.")

# make the string lowercase all
print(other_name_1.lower())

# delete choosed characters at begginig of the string
print(other_name_1.lstrip("Ja"))

# delete choosed characters from end of the string
print(other_name_1.rstrip("ck"))

# The strip() method removes any leading (spaces at the beginning)
#   and trailing (spaces at the end) characters (space is the default leading character to remove)
print(other_name_5.strip())
print(other_name_6.strip("+/*x,."))

# take a part the string
print(other_name_1.partition("Ja"))

# Replace the characters
print(name_of_customer.replace("a", "+"))

# We have also rfind(), rindex(), rpartition(), translate(), zfill(), ...

# take part the string with the choosen character and gives a list
print(other_name_2.rsplit(" "))
print(other_name_3.rsplit("+"))
print(other_name_3.split("+"))

# delete the break lines from the string
print(other_name_4.splitlines())

# swap capital and small alphabets
print(other_name_7.swapcase())

# makes the first letters after free space capital letter
print(sentense_string_1.title())
