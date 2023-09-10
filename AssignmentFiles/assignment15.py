
# Write a python program that accepts a string from user and perform following string operations- 
# i. Calculate length of string ii. String reversal 
# iii. Equality check of two strings iii. Check palindrome ii. Check substring

string = input("\nEnter String: ")

while True:
    
    print("\n1. Calculater Length of String.\n2. Reverse the String." +
        "\n3. Check for Equality of String.\n4. Check Palindrome.\n5. Check Substring.\n6. Quit")

    choice = int(input("\nWhat do you want to do: "))

    print("\n")

    if choice == 1:
        length = len(string)

        print(f"\nThe Length of the string is {length} characters")

    if choice == 2:
        stringrev = string[::-1]

        print(f"The Reversed String is: '{stringrev}' .")

    if choice == 3:
        string2 = input("\nEnter another string for check: ")

        equal = string == string2

        print(f"\nEquality Check with another String: {equal}")

    if choice == 4:
        stringrev = string[::-1]

        palindrome = stringrev == string

        print(f"\nPalindrome Check: {palindrome}")

    if choice == 5:
        substring = input("\nEnter Substring: ")

        sub = substring in string

        print(f"\nSubstring Check: {sub}")

    if choice == 6:
        break



