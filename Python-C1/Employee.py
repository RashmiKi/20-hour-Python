name = input("Enter your name: ")
sales = int(input("Enter your sales: "))
base_salary = float(input("Enter your base salary: "))
target_salary=  int(input("Enter your target sales: "))
bonus = float(input("Enter your bonus: "))
new_salary = 0

if sales >= target_salary:
    new_salary = base_salary + bonus
    print("Salary:", new_salary)

print("Name:", name)
print("Salary:", new_salary)
