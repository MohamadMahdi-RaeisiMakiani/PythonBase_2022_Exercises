from math import sqrt

print(f"\nThis is 64 Square Root: {int(sqrt(64))}\n")

# key value data type in python is Dicionary
city_country = {"London": "England", "New York": "United States",
                "France": "Paris", "Germany": "Berlin"}
print(city_country["France"])


# a list of data types can be added to list
foods_list = ["Pizza", "Burger", "Spageti",
              "Chicken", "French Fries", "Fish and Chips"]
print(foods_list[2])
print(foods_list[-1])
# tuple like a list but we can't make changes add, or remove values
fruits_to_buy = ("Apple", "Banana", "Orange",
                 "Cucumber", "Water Melon", "grapes")
print(fruits_to_buy[3:6])

# a set denied repetitive values
numbers_set = {5, 5, 5, 5, 5, 7, 9, 11, 13, 13, "fifteen", "seventeen"}
print(numbers_set)

# Add an item at the end of the list
foods_list.append("Sushi")
print(foods_list)

# copy a list to another list, dictionary
copied_food_list = foods_list.copy()
copied_city_country = city_country.copy()
print(f"\nThis is copied {copied_food_list}\n")
print(f"\nThis is copied {copied_city_country}\n")

# count an item in the list, tuple
print(copied_food_list.count("Sushi"))
print(fruits_to_buy.count("Apple"))

# find the index of the item in the list, tuple
print(copied_food_list.index("Sushi"))
print(fruits_to_buy.index("Orange"))

# add an item to a special index of the list
copied_food_list.insert(3, "Hot Dog")
print(copied_food_list)

# Delete the last item, list
copied_food_list.pop()
print(copied_food_list)

# Delete the item 2, list, dictionary
copied_food_list.pop(2)
city_country.pop("France")
print(copied_food_list)
print(city_country)

# like pop remove an item but get item value not the index
copied_food_list.remove("Fish and Chips")
print(copied_food_list)

# reverse the list
copied_food_list.reverse()
print(copied_food_list)

# copied_food_list.sort()

# Delete the last item, dictionary
city_country.popitem()
print(city_country)

# a dictionary keys and values => keys : values
print(city_country.keys())
print(city_country.values())

# update and add another dictionary to a dictionary
second_dict_items = {"China": "Pekan", "Russia": "Moscow", "Japan": "Tokyo"}
city_country.update(second_dict_items)
print(city_country)

# dictionary items [key,value]
print(city_country.items())

# get a value of a key
print(city_country.get("Japan"))

# clear the list and get an empty list, dictionary
foods_list.clear()
city_country.clear()
print(foods_list)
print(city_country)
