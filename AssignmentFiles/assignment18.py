
# Create class EMPLOYEE for storing details (Name, Designation, gender, Date of Joining and Salary). 
# Define function members to compute 
# a) total number of employees in an organization 
# b) count of male and female employee 
# c) Employee with salary more than 10,000 
# d) Employee with designation “Assistant Manager."

class Employee:
    
    def __init__ (self, name, designation, gender, joining_date, salary):
        self.name = name
        self.designation = designation
        self.gender = gender
        self.joining_date = joining_date
        self.salary = salary

employee_list = []

def no_of_employees(employee_lst):
    return len(employee_lst)

def gndr(employee_lst):
    male = 0
    female = 0

    for emp in employee_lst:
        if emp.gender.lower() == "female":
            female += 1
        
        if emp.gender.lower() == "male":
            male += 1
    
    return male, female

def high_salary(employee_lst, threshold=10000):
    return (emp for emp in employee_lst if emp.salary >= threshold)

def asst_manager(employee_lst):
    return (emp for emp in employee_lst if emp.designation.lower() == "assistant manager")

while True:
    choice = input("\nAdd Employee? (Y/ N): ")

    if choice.lower() == 'y':
        name = input("\nEnter Name of Employee: ")
        designation = input("Enter Designation of Employee: ")
        gender = input("Enter Gender of Employee: ")
        joining_date = input("Enter Joining Date of Employee: ")
        salary = float(input("Enter Salary of Employee: "))

        employ = Employee(name, designation, gender, joining_date, salary)
        employee_list.append(employ)

    if choice.lower() == 'n':
        break
        
employee_no = no_of_employees(employee_list)
male , female = gndr(employee_list)
highsal = high_salary(employee_list)
asst_mgnr = asst_manager(employee_list)

print(f"\nTotal Number of Employees: {employee_no}.")

print(f"\nFemale Employees: {female}")
print(f"Male Employees: {male}")

print("\nEmployee with salary more than 10,000: ")
for emp in highsal:
    print(f" - {emp.name}, Salary: {emp.salary}")

print("\nEmployee with designation of 'Assistant Manager': ")
for emp in asst_mgnr:
    print(f" - {emp.name}")