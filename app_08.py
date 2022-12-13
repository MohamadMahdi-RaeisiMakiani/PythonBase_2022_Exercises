
# * for loop is a counting loop in the python

def main():

    # an empty list
    numbers_list = []

    # range built-in function and for loop
    for number_2 in range(11):
        print(f"for loop and range: {number_2}")

    # using range built-in function in another way
    for number_3 in range(1, 11):
        numbers_list.append(number_3)

    # print the list
    print(f"\nnumbers list is here: {numbers_list}\n")

    # len() is a built-in function to see length of the list or any data type.
    print(f"\nnumbers list length is here: {len(numbers_list)}\n")

    # Totall list items method 1
    totall_numbers_list = 0
    for i in range(len(numbers_list)):
        # print(f"list check: {numbers_list[i]}")
        totall_numbers_list += numbers_list[i]
    print(f"\nTotall is: {totall_numbers_list}\n")

    # Totall list items in other way
    list_all_numbers_sum = sum(numbers_list)
    print(f"\nTotal is(Using sum built-in function): {list_all_numbers_sum}\n")

    # The Average of the list sum
    print(f"\nThe average is: {totall_numbers_list/len(numbers_list)}\n")

    # getting user numbers to calculate sum of the numbers
    user_get_sum = 0
    for user_input_times in range(10):
        # try except to check if user enter a string instead of integer type and handle it
        try:
            user_get_number = int(
                input("Enter the number to calculate sum:\n >"))
            user_get_sum += user_get_number
        except:
            print("Error! Please Enter Just Numbers in Integer Type.")
            break
    print(f"\n\nSum of user numbers is: {user_get_sum}")

    # A variable with an empty value to giving it some values
    empty_variable_to_value = None
    print(empty_variable_to_value)
    empty_variable_to_value = 1
    print(empty_variable_to_value)

    # again check user input to be sure that is integer type (it's number)
    try:
        user_get_factorial = int(
            input("Enter the number to calculate factorial:\n >"))
    except:
        print("Error! Please Enter Just Numbers in Integer Type.")

    # calculate the factorial of a number
    for user_get_factorial_calc in range(1, user_get_factorial+1):
        # print(user_get_factorial_calc)
        empty_variable_to_value *= user_get_factorial_calc
    print(
        f"The factorial of {user_get_factorial} is: {empty_variable_to_value}")


if __name__ == "__main__":
    main()
