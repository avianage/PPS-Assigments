
# To accept list of N integers and partition list into two sub lists even and odd numbers

num = int(input("\nEnter number of elements in the list: "))
num_list = []

print("\n")

for i in range(num):
    num = int(input(f"Number {i+1} element in the list: "))

    num_list.append(num)

print("\nNumbers: ",num_list)

def partition(num):
    even = []
    odd = []

    for ele in num:
        if (ele % 2 ==0 ):
            even.append(ele)
        else:
            odd.append(ele)

    return even, odd

even_list, odd_list = partition(num_list)

print("\nEven Numbers: ", even_list)
print("Odd Numbers: ", odd_list)

print("\n")