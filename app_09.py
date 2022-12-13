
# * while loops are the conditional loops in the Python

# this is a while loop and it runs till user enter an integer number
while True:
    try:
        user_number_input_1 = int(input("Please enter a numbe:\n >"))
        # break means exit the loop
        break
    except:
        print("Wrong command, Just integer numbers!")

# this is a while loop to display numbers between 0 and user input number if it is lower than 10
while user_number_input_1 < 10 and user_number_input_1 > 0:
    print(f"\nThis is number in loop > {user_number_input_1}\n")
    user_number_input_1 -= 1

# making a new list of numbers using loops
numbers_list_1 = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 30]
numbers_list_2 = []

for list_items_1 in numbers_list_1:
    while list_items_1 < 11:
        # print(list_items_1)
        numbers_list_2.append(list_items_1)
        list_items_1 += 1
print(f"\nThis is the second list: {numbers_list_2}\n")
