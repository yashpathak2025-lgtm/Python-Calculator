print("=" * 50)
print(f"{' ' * 20}Calculator")
print("=" * 50)

while True:

    # Choose Operation
    print("\nChoose an Operation")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Percentage(%)")
    print("6. Modulus (%)")
    print("7. Power (x^y)")
    print("8. Square (x²)")
    print("9. Cube (x³)")
    print("10. Exit")

    choice = input("Enter the Operation (1 to 10): ")

    # Exit
    if (choice == "10"):
        print("Thank you for using the Calculator.")
        break

    # Check valid choice
    if choice not in ("1", "2", "3", "4","5","6","7","8","9"):
        print("Invalid Choice! Please enter a number between 1 and 10.")
        continue
    # for Percentage
    
    if(choice=="5"):
        try:
            obtained = float(input("\nEnter Obtained Value: "))
            total = float(input("Enter Total Value: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if(total!=0 and obtained<=total):
            percentage=(obtained / total) * 100
            print(f"\nPercentage = {percentage:.2f}%")
        elif(total==0):
            print("Total cannot be zero.")
        else:
            print("Obtained value cannot be greater than total value.")


    # for Square
    elif(choice=="8"):
        try:
            number= float(input("Enter the number: "))
            print(f"Result: {number} ^ 2 = {number ** 2}")
        except ValueError:
            print("Invalid input! Please enter numbers only.")


    # for Cube 
    elif(choice=="9"):
        try:
            number= float(input("Enter the number: "))
            print(f"Result: {number} ^ 3 = {number ** 3}")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    elif(choice=="1" or choice=="2" or choice=="3" or choice=="4" or choice=="6" or choice =="7"):
    # Take Numbers
        try:
            a = float(input("\nEnter First Number: "))
            b = float(input("Enter Second Number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue
    # for Addition
        if (choice == "1"):
            print(f"\nResult: {a} + {b} = {a + b:.2f}")


    # for Subtraction
        elif (choice == "2"):
            print(f"\nResult: {a} - {b} = {a - b:.2f}")


    # for Multiplication
        elif (choice == "3"):
            print(f"\nResult: {a} X {b} = {a * b:.2f}")


    # for Division
        elif (choice == "4"):
            if b != 0:
                print(f"\nResult: {a} / {b} = {a / b:.2f}")
            else:
                print("\nError! Division by zero is not allowed.")


    # for Modulus
        elif(choice=="6"):
            print(f"\nResult: {a} % {b} = {a % b:.2f}")


    # for Power 
        elif (choice == "7"):
            print(f"\nResult: {a} ^ {b} = {a ** b}")


    continue_choice=input("Do you want to continue? (y/n)  ").lower()
    if(continue_choice!="y"):
        print("Thank you for using the Calculator.")
        break


