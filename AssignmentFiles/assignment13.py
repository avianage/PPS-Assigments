
# To accept the number of terms a finds the sum of sine series.

# sin(x) = x - (x^3 / 3!) + (x^5 / 5!) - (x^7 / 7!) + ...
# sine series

import math

x = float(input("\nEnter the value of x (in radians): "))
N = int(input("Enter the number of terms (N): "))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def sine_series(x, n):
    result = 0.0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        result += term
    return result

sum_sine_series = sine_series(x, N)

print(f"\nThe sum of the sine series for x = {x} and N = {N} is: {sum_sine_series}")

print("\n")