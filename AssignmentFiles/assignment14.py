
# To accept from user the number of Fibonacci numbers to be generated and print the Fibonacci series.

num = int(input("\nEnter number of terms in the Fibonacci Series: "))

def fibonacci(num):
    a, b = 0 , 1

    fibonacci_series = []

    if num <= 0:
        print("\nEnter Positive Number.")
    
    elif num == 1:
        fibonacci_series.append(0)

    elif num == 2:
        fibonacci_series.append([0, 1])
    
    else:
        fibonacci_series.extend([0, 1])

        for i in range(2, num):
            next = fibonacci_series[-1] + fibonacci_series[-2]
            fibonacci_series.append(next)

    return fibonacci_series

fib_series = fibonacci(num)

print("\nFibonacci Series: ")
for ele in fib_series:
    print(ele, end=" ")
    
print("\n")

