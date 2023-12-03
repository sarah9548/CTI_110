#CTI-110
#P4HW2-Salary Calculator
#Sarah Houssein
#11/30/2023
#Use if/else to determine an employeees pay


#Create variables to hold totals paid to employees
total_overtime_pay = 0
total_regular_hours_pay = 0
total_gross_pay = 0
total_employees = 0

#Get user input
while True:
    name = input("Enter employee's name or 'Done' to terminate: ")
    
    #Calculations
    if name.lower() == 'done':
        break
    
    hours_worked = float(input(f"How many hours did {name} work? "))
    pay_rate = float(input(f"What is {name}'s pay rate? "))
    
    overtime_pay = 0
    regular_hours_pay = 0
    overtime_hours = 0
    
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (1.5 * pay_rate)
        regular_hours_pay = 40 * pay_rate
        
    #This represents if regular_hours_pay is 40 or less     
    else:
        regular_hours_pay = hours_worked * pay_rate
        
    gross_pay = regular_hours_pay + overtime_pay
    
    #Calculate pay
    total_overtime_pay += overtime_pay
    total_regular_hours_pay += regular_hours_pay
    total_gross_pay += gross_pay
    total_employees += 1
    
    #Display
    print("\nEmployee Details:")
    print(f"Name: {name}")
    print(f"Pay Rate: ${pay_rate}/hr")
    print(f"Hours Worked: {hours_worked} hrs")
    print(f"Overtime Hours: {overtime_hours} hrs")
    print(f"Overtime Pay: ${overtime_pay:.2f}")
    print(f"Pay for Regular Hours: ${regular_hours_pay:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    

#This code executes after loop breaks
print("Done adding employees")
print()    
print(f"Total number of employees: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_hours_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
