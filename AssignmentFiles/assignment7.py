
# To accept the number and Compute a) square root of number, b) Square of number, 
# c) Cube of number d) check for prime, d) factorial of number e) prime factors

import math

num = int(input("\nEnter Number to be Computed: "))

root = math.sqrt(num)   # function in math library

cube = num ** 3

fact = math.factorial(num)

def largest_prime_factorial(n):
    i = 2
    while i*i <= n:
        if n % i:
            i += 1
        else:
            n //= i

    return n

lpf = largest_prime_factorial(num)

print("\nThe root of the given number is ", root)
print("The Cube of the given number is ", cube)
print("The Factorial of the given number is ", fact)
print("The Largest Prime Factor is ", lpf)