
# To simulate simple calculator that performs basic tasks such as addition, subtraction, 
# multiplication and division with special operations like computing x^y and x!.

print("\n------- Calculator -------")

while True:
    print("\n1. Addition.\n2. Subtraction.\n3. Multiplication.\n4. Division.\n5. Power of X.\n6. Factorial.\n7. Quit.\n")
    
    choice = int(input("\nWhat do you want to do: "))

    if choice == 1:
        num1 = int(input("\nEnter Number 1: "))
        num2 = int(input("Enter Number 2 to be added to Number 1: "))

        sum = num1 + num2

        print("\nThe Sum is ", sum)

    if choice == 2:
        num3 = int(input("\nEnter Number 1: "))
        num4 = int(input("Enter Number 2 to be subtracted from Number 1: "))

        diff = num3 - num4

        print("\nThe Difference is ", diff)

    if choice == 3:
        num5 = int(input("\nEnter Number 1: "))
        num6 = int(input("Enter Number 2 for multiplying with Number 1: "))

        mult = num5 * num6

        print("\nThe Product is ", mult)

    if choice == 4:
        num7 = float(input("\nEnter Number 1: "))
        num8 = float(input("Enter Number 2 to be divided with Number 1: "))

        div = num7 / num8

        print("\nThe Quotient is ", div)

    if choice == 5:
        num9 = int(input("\nEnter Number 1: "))
        num10 = int(input("Enter Power for Number 1: "))

        power = num9 ** num10

        print(f"\n{num9} to the power of {num10} is {power}.")

    if choice == 6:
        num11 = int(input("\nEnter Number to find Factorial: "))

        fact = 1

        for i in range(1, num11+1):
            fact = fact * i
        
        print("\nThe Factorial is ", fact)

    if choice == 7:
        break

    else:
        print("\nEnter Correct Choice.")
        break