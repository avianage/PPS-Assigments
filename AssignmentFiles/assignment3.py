
# To accept N numbers from user. Compute and display maximum in list, minimum in list,
# sum and average of numbers.

n = int(input("\nEnter number of elements in the list: "))  # take input as integer value n
num_list = []   # creating a empty list

print("\n")

for ele in range(n):
    temp = 0
    temp = int(input(f"Enter value of number {ele + 1}: "))   # store the values entered by users into a list

    num_list.append(temp)   # Appending / Adding elements in the list.

sum_inbuilt = sum(num_list)     # In-built function to calculate sum
avg_inbuilt = sum_inbuilt/len(num_list)
max_element = max(num_list)     # In-built function to calculate maximum element in a list
min_element = min(num_list)     # In-built function to calculate minimum element in a list

print("\nThe maximum element in the list is", max_element,".")
print("The minimum element in the list is", min_element,".")
print("The sum of all elements in the list is", sum_inbuilt,".")
print("The average of all elements in the list is", avg_inbuilt,".\n")


# If in-built function are not allowed, then use the following:

# sum = 0

# for i in range(n):
#     sum = sum + num_list[i]

# average = (sum)/n    # Calculating Average using formula

# max = num_list[0]
# min = num_list[0]

# for i in range(n):
#     if num_list[i] >= max:
#         max=num_list[i]
#     else:
#         continue

#     if num_list[i] <= min:
#         min=num_list[i]
#     else:
#         continue

# print(max, min, sum, average)

