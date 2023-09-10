
# To accept a number from user and print digits of number in a reverse order.

num = int(input("\nEnter number to be reversed: "))
numrev = 0

temp = num

while temp > 0:
    digit = (temp %10)

    numrev = numrev*10 + digit

    temp = temp // 10

print("\nThe Reversed number is ", numrev)

print("\n")
