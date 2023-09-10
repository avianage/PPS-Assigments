
# To accept two numbers from user and compute smallest divisor and 
# Greatest Common Divisor of these two numbers.

import math

def smallest_divisor(num):
    for i in range(2, num + 1):
        if num % i == 0:
            return i

def gcd(a, b):
    return math.gcd(a, b)

num1 = int(input("\nEnter the first number: "))
num2 = int(input("Enter the second number: "))

divisor1 = smallest_divisor(num1)
divisor2 = smallest_divisor(num2)

gcd_result = gcd(num1, num2)

print(f"\nThe smallest divisor of {num1} is: {divisor1}")
print(f"The smallest divisor of {num2} is: {divisor2}")
print(f"The GCD of {num1} and {num2} is: {gcd_result}")