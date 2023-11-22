#CTI_110
#P3HW2 - Salary
#Sarah Houssein
#11/21/2023
#Use if/else to determine an employees pay

#Get user input
name = input("Enter the name of the employee: ")
hours_worked = float(input("Enter the number of hours the employee worked this week: "))
pay_rate = float(input("Enter the employee's pay rate: "))
               
#Calculations
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (1.5 * pay_rate)
    regular_hours_pay = 40 * pay_rate          


#This represents if emp_hours is 40 or less
else:
    regular_hours_pay = hours_worked * pay_rate
    
#Calculate pay
gross_pay = regular_hours_pay + overtime_pay

#Display
print("\nEmployee Details:")
print(f"Name: {name}")
print(f"Pay Rate: ${pay_rate}/hr")
print(f"Hours Worked: {hours_worked} hrs")
print(f"Overtime Hours: {overtime_hours} hrs")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Pay for Regular Hours: ${regular_hours_pay:.2f}")
print(f"Gross Pay: ${gross_pay:.2f}")

