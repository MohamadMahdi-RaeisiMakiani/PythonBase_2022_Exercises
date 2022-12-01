def main():
    get_user_Nama = input("Enter your Name\n >")
    get_user_Age = input("How old are you?\n >")
    get_user_Height = input("Enter your height\n >")
    get_user_Weight = input("Enter your weight\n >")
    user_all_Info = f"\nHey {get_user_Nama}! You are {get_user_Age}, your height is {get_user_Height}cm and your weight is {get_user_Weight}Kg."
    print(user_all_Info)

    check_more = input("\nDo you want more info?\n (yes/no) >")

    def inch_converter(height=get_user_Height, weight=get_user_Weight):
        height_to_Inch = round(float(height)/2.54, 2)
        weight_to_Pond = round(float(weight)*2.20462262, 2)
        print(
            f"\nAgin your weight is {weight_to_Pond}pond and your height is {height_to_Inch}inch.")
    if check_more == "yes":
        inch_converter()
    elif check_more == "no":
        print("\nOK, Thank you! Bye.\n")
    else:
        print("\nWrong command!\n")


if __name__ == "__main__":
    main()
