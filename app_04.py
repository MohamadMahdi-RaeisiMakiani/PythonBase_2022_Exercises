from math import pi
# import pi number from math library/module

# main function


def main():
    # Getting user input
    circle_radius = input("\nEnter the circle radius (r)\n >")
    try:
        # to round the numbers with 2 decimal places
        rounded_radius = round(float(circle_radius), 2)
        # calculate area of the circle
        circle_area = rounded_radius*pi
        # using f strings to add variables to for print a string
        print(f"\nYour circle area is: {round(circle_area, 2)}\n")
    except:
        print("\nWrong command, Enter just numers!\n")
        # to clean exit from app when user gives a string, not numers(float or int types)
        quit()

    # to define a function we have to use -def- before the function name
    # at this function we have one parameter or argument with a default value(rounded_radius)
    # but we can give another argument when we call or use the function /Refer to x1/
    def calculate_volume(sphere_radius=rounded_radius):
        # calculate the sphere volume
        sphere_volume = 4/3*pi*sphere_radius**3
        # in every function we may have a final result or export a special data from the function
        # to do that we have to return that variable or value
        return round(sphere_volume, 2)

    print(f"\nYour sphere volume is: {calculate_volume()}\n")
    # x1
    print(calculate_volume(5))


# using it to recognize that our code is a independent script or it's a module
if __name__ == "__main__":
    main()
