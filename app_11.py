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


if __name__ == "__main__":
    main()
