
# To calculate salary of an employee given his basic pay (take as input from user).
# Calculate gross salary of employee. Let HRA be 10 % of basic pay and TA be 5% of
# basic pay. Let employee pay professional tax as 2% of total salary. Calculate net salary
# payable after deductions.

salary = float(input("\nEnter Basic Pay of Employee: "))

hra = (0.1 * salary)    # hra is 10% of basic pay
ta = (0.05 * salary)   # ta is 5% of basic pay
ptax = (0.02 * salary)     # ptax is 2% of basic pay

net_salary = salary - (hra + ta + ptax)

print("\nThe net-salary after deducing HA, TA and Professional Tax is: ", net_salary)