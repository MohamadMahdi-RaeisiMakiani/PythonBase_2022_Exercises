# This is a loop and it runs untill we stop it
# while True is a infinite loop
while True:
    # Getting user input
    temperature = input("\nEnter the temperature here\n >")
    # We can use try except in python to avoid any errors in the script when it runs
    try:
        # convert a variable value to the float numbers, like 2.2, 5.44
        float(temperature)
        # convert to integer numbers like, 1, 2, 3
        temp_to_number = int(float(temperature))
        # conditional statements in the python
        if temp_to_number >= 0 and temp_to_number <= 10:
            print("\nWeather is Good\n")
        elif temp_to_number >= 10:
            print("\nWeather is going to be Hot, Sunrise!\n")
        else:
            print("\nNow it's Cold, Sunset.\n")
        # we can use break to exit the loop
        break
    except:
        print("\nWrong command! Enter just a number")
