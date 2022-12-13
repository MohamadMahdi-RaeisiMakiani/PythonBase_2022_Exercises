
# to open a file in the Python we have to do these steps:
#   - define a variable with a custome name
#   - use open method
#   - first parameter of this method is the file address and the file name
#   - second parameter of this method is the open method opearations
#   - operations include : read (r) - write (w) - append (a) - create (x)
#   - also we can choose the file opens in binary mode or text mode (optional)
#   - to open the file in text mode add t end of the operation and in binary mode add b
#   - for example read a file in binary mode we have to use "rb" as the operation
#   - another example write a text file we have to use "wt" as the operation
#   - we have some other methods for the open() function such as:
#   - read(), readlines(), readlines(), write(), writelines(), seek(), truncate(), close(), tell()
# close()	    | Closes the file
# detach()	    | Returns the separated raw stream from the buffer
# fileno()	    | Returns a number that represents the stream, from the operating system's perspective
# flush()	    | Flushes the internal buffer
# isatty()	    | Returns whether the file stream is interactive or not
# read()	    | Returns the file content
# readable()	| Returns whether the file stream can be read or not
# readline()	| Returns one line from the file
# readlines()	| Returns a list of lines from the file
# seek()	    | Change the file position
# seekable()	| Returns whether the file allows us to change the file position
# tell()	    | Returns the current file position
# truncate()	| Resizes the file to a specified size
# writable()	| Returns whether the file can be written to or not
# write()	    | Writes the specified string to the file
# writelines()	| Writes a list of strings to the file

# open a file to write in a string in it    |   "wt" means write operation in text mode
# if file exist, it clean the file then write datas
# if file doesn't exist, it create the file then write datas
file_1 = open("test_file_1.txt", "wt")
# write the string in the file
file_1.write("Here is the Text file to test the open method in the Python\n")
# close the file to finish our work with the file
file_1.close()

buy_list = ["Tomato", "Potato", "Meat", "Bread", "Cheese", "Egg"]

# open the file in append mode to add some string to the text file
file_2 = open("test_file_1.txt", "a")
for buy_list_items in buy_list:
    # writelines write string or datas in each line of the file
    file_2.writelines(f"\nBuy Item > {buy_list_items}")
# tell method show the character length written in the file
print(f"\nThis is your file characters > {file_2.tell()}\n")
file_2.close()

# also we can use "r" operation to just read the file
file_3 = open("test_file_1.txt", "r")
# with readlines method we can read every line of the file step by step
for each_line in file_3.readlines():
    print(
        f"\nYou want to read this text file in redlines mode> {each_line}")
file_3.close()


print("\n-----------------------------")

# again we have read method to read all the file text
file_4 = open("test_file_1.txt", "r+")
print(f"\nYou want to read this text file in read mode> {file_4.read()}\n")
file_4.close()

# with seek method we can start reading file from each section we selected
# according to read or readline or readlines methods -> next line
# we can specify using of seek method to character sections or line sections
file_5 = open("test_file_1.txt", "rt")
file_5.seek(70)
print(
    f"I read this file from character 70 to end of the line> {file_5.readline()}")
print(
    f"I read this file from character 70 to end of the file> {file_5.read()}")
file_5.close()
