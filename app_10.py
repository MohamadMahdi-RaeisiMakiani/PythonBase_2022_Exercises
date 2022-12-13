
# * functions in python made by this syntax:
#
#       + def function_name(parameter = default_value):
#       +   function inside block
#       + function_name(argument) | to call, use or run a function
#
#       / We are able to avoid using any parameters or arguments like this:
#       + def function_name():
#       +   ...
#       + function_name()
#
#       / And we can use *args and **kwargs when we don't know how
#           many parameters or arguments we should use. *args for variable = value
#           **kwargs for variable = { key : vale }
#       + def function_name(*any_custome_name):
#           ...
#         function_name("value 1", "value 2", 3, True, ["a", "b"])
#
#       + def function_name(**any_custome_name):
#           ...
#         function_name( key_1 = "value 1", key_2 = "value 2")
#
#       / We can return some value in every function in the Python
#           but it is better to return just one value in each function.

# define a function
def say_hello():
    return "Hello, world!"


# run, use or call the function
say_hello()

# print the value you returned in the function block
print(
    f"\nThis is the message was returned in the function:\n > {say_hello()}\n")


# define a function with a default value for it parameter
def say_hello_to_user(user_name="No Entered Name"):
    print(f"Hello Mr./Mrs. {user_name}, This is a Good day.\n")


# if we send an argument to call a function that runs without using parameter default value
say_hello_to_user("Mark Morby")

# but when we don't pass any argument to call the function it uses parameter default value to run it
say_hello_to_user()

# also we are able to ask the user to enter an input
#   and use it instead of function argument to call it | for Example enter "Linda"
input_user_name = input("Enter your name, please:\n >")
say_hello_to_user(input_user_name)


# We can use *args to access user give infinite arguments
def print_three(*args):
    # unpack the args
    arg1, arg2, arg3 = args
    print(f"\n > arg1: {arg1}, arg2: {arg2}, arg3: {arg3}\n")


print_three("Hi.", "How are you?", "GoodBye!")


# a function with using *args rule to send as many argument as we want
def company_members_list(*member):
    the_employee_list = []
    the_employee_list.append(member)
    return the_employee_list


# to use a variable that returned by a function we have to make a variable that calls the function
emp_list = company_members_list(
    "Mark", "Jason", "Mona", "Sarah", "Mike", "Jack")

# it gives us a list that the first index of that is a tuple which contains the names.
print(f"The company employee list is:\n > {emp_list}")
# it gives the names in a tuple
print(f"The company employee list is:\n > {emp_list[0]}")


def company_member_ages(**member_age):
    print(
        f"\n > Company head is {member_age['Boss']} with age {member_age['Boss_age']}\n")
    print(
        f"\n > Company designer is {member_age['Designer']} with age {member_age['Designer_age']}\n")
    print(
        f"\n > Company developer is {member_age['Developer']} with age {member_age['Developer_age']}\n")


company_member_ages(Boss="Jason", Boss_age=35, Designer="Mona",
                    Designer_age=20, Developer="Mark", Developer_age=25)


Food_Costs_list = {"Pizza": "7$", "HotDog": "2$",
                   "Burger": "4$", "Fish and Chips": "8$", "Fried Chicken": "6$",
                   "French Fries": "3$", "Steak": "10$"}

# to get a key value from the dictionary
print(f"\nThe cost of Pizza is > {Food_Costs_list['Pizza']}\n")

# it gives us an error cause we don't have
#   any 10$ keys (it's a value not key!) | Next line that was commented to avoid getting errors
# print(f"\nThe cost of Pizza is > {Food_Costs['10$']}\n")

# it's like above but it returns None, we don't get an error
print(f"The cost of Burger is > {Food_Costs_list.get('10$')}")

# another way to get a value of a dictionary key
print(f"The cost of Burger is > {Food_Costs_list.get('Burger')}")

# to get all dictionary items
print(f"\nDictionary items are here:\n >{Food_Costs_list.items()}\n")

# to make a list from all dictionary keys
all_foods = list(Food_Costs_list.keys())

# to make a list from all dictionary values
all_costs = list(Food_Costs_list.values())

# print the lists above
print(f"\nFoods List:\n > {all_foods}\n")
print(f"\nCosts List:\n > {all_costs}\n")

# to display each key with its value in the dictioanry
for each_food in all_foods:
    print(f"The food {each_food} is {all_costs[all_foods.index(each_food)]}")
