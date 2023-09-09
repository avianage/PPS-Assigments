
# To check whether input number is Armstrong number or not. An Armstrong number is an
# integer with three digits such that the sum of the cubes of its digits is equal to the number
# itself.

# A number is thought of as an Armstrong number if 
# the sum of its own digits raised to the power number of digits gives the number itself
# Eg: 153 = (1^3) + (5^3) + (3^3) = 153; 1634 = (1^4) + (6^4) + (3^4) + (4^4)

num = int(input("\nEnter the number to check: "))

sum = 0   # initializing variables for calculation purpose

temp = num
temp1 = num

count = 0
while temp1 != 0:
    temp1 = temp1 // 10
    count += 1

while temp > 0 :
    digit = temp % 10    
    sum += digit ** count

    temp = temp // 10

if sum == num:
    print ("Number {} is a armstrong number\n".format(num))
else:
    print ("Number {} isn't a armstrong number\n".format(num))

