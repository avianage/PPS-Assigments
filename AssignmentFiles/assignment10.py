
# To input binary number from user and convert it into decimal number

binary_num = input("\nEnter a binary number: ")

if not all(bit in '01' for bit in binary_num):
    print("Invalid binary number. Please enter a valid binary number.")
else:
    decimal_num = int(binary_num, 2)
    print(f"The decimal equivalent of {binary_num} is: {decimal_num}")

print("\n")