def main():
    numbers_to_do = []
    try:
        first_numer = int(input("Enter the num 1\n > "))
        second_numer = int(input("Enter the num 2\n > "))
        numbers_to_do.append(first_numer)
        numbers_to_do.append(second_numer)
    except:
        print("\nWrong command, Just Integer Numbers!\n")
        exit()
        # On many operating systems, a program can abort with exit(0)
        # exit(0) will be a good exit.
        # If you do exit(1) then it will be an error.
        # exit(0)

    calculater_operation = input(
        "Enter the operation you want (+ | - | * | / | power)\n > ")

    def calculator(operation, numbers):
        if operation == "+":
            sum_numbers = numbers[0] + numbers[1]
            print(
                f"\nYour operations is Total\n > {numbers[0]} + {numbers[1]} = {sum_numbers}\n")
        elif operation == "-":
            subtraction_numbers = numbers[0] - numbers[1]
            print(
                f"\nYour operations is Subtraction:\n > {numbers[0]} - {numbers[1]} = {subtraction_numbers}\n")
        elif operation == "*":
            multiplication_numbers = numbers[0] * numbers[1]
            print(
                f"\nYour operations is Multiplication:\n > {numbers[0]} * {numbers[1]} = {multiplication_numbers}\n")
        elif operation == "/":
            division_numbers = numbers[0] / numbers[1]
            print(
                f"\nYour operations is Division:\n > {numbers[0]} / {numbers[1]} = {division_numbers}\n")
        elif operation == "power":
            power_numbers = numbers[0] ** numbers[1]
            print(
                f"\nYour operations is Power:\n > {numbers[0]} ** {numbers[1]} = {power_numbers}\n")
        else:
            print("\nWrong command, we don't have this operation here!\n")

    calculator(calculater_operation, numbers_to_do)

    find_mine = input(
        "\nWhich mine you want to start Mining? (mine 1 - mine 2 - mine 3)\n > ")

    def find_the_gold(which_mine):
        mines = ["mine 1", "mine 2", "mine 3"]
        if which_mine == "mine 1":
            print("\nYou Find The Gold\n")
            try:
                jewelery_amount = int(input("\nHow much you want?\n > "))
                if jewelery_amount >= 10 and jewelery_amount < 20:
                    print(f"\nYou Win {jewelery_amount} Gold\n")
                elif jewelery_amount < 10:
                    print(f"\nSure, I'll give you {jewelery_amount} Gold\n")
                else:
                    print(f"\nF**k off, you greedy son of a ...\n")
            except:
                print("\nYou f**king kidding me! Just Number\n")
        elif which_mine == "mine 2":
            print("\nHey Man! You are so lucky, this is the Diamond Mine.")
            try:
                jewelery_amount = int(input("\nHow much you want?\n > "))
                if jewelery_amount >= 5 and jewelery_amount < 10:
                    print(f"\nYou lucky win {jewelery_amount} Diamond\n")
                elif jewelery_amount < 5:
                    print(f"\nGet your {jewelery_amount} Diamond\n")
                else:
                    print(f"\nF**k off, you greedy son of a ...\n")
            except:
                print("\nYou f**king kidding me! Just Number\n")
        elif which_mine == "mine 3":
            print("\nThis mine is Empty, Today is not your day, GoodBye!\n")
        else:
            print("What??? We don't have this shit.")
    find_the_gold(find_mine)

    number_adder_1 = 0
    while number_adder_1 < 21:
        print(f"\nYour Number is > {number_adder_1}\n")
        number_adder_1 += 1

    football_teams_goals = {"Spain": "2 Goals", "Brazil": "3 Goals",
                            "England": "4 Goals", "Argentina": "6 Goals"}

    print(f"\nThis is all team with goals > {football_teams_goals}\n")

    for all_football_teams in list(football_teams_goals.keys()):
        print(f"\nMatch Team > {all_football_teams}\n")

    match_total_goals = 0
    for all_goals_get in list(football_teams_goals.values()):
        for total_goals in all_goals_get:
            if total_goals.isdigit():
                match_total_goals += int(total_goals)

    print(f"\nThis Match Total Goals > {match_total_goals}\n")


if __name__ == "__main__":
    main()
