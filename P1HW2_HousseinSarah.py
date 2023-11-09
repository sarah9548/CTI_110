# A Travel Expense calculator
# Date: 11/9/2023
# CTI-110 P1HW2 - Travel Expense
# Sarah Houssein


# This will Prompt the user to enter their budget
budget = float(input("Enter Budget: "))

# This will Ask the user to enter the travel destination
destination = input("Enter your travel destination: ")

# This will Ask the user for the amount they will spend on gas
gas_expense = float(input("How much do you think you will spend on gas? "))

# This will ask the user for the amount they will spend on accommodation
accommodation_expense = float(input("Approximately, how much will you need for accommodation/hotel? "))

# This will Ask the user for the amount they will spend on food
food_expense = float(input("Last, how much do you need for food? "))

# This will Calculate the total expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Calculate the remaining budget
remaining_budget = budget - total_expenses

# Display the travel expenses 
print("\n****************************************")
print("             Travel Expenses             ")
print("****************************************")
print("Location:                ", destination)
print("Initial Budget:          $", format(budget, '.2f'))
print("Fuel:                    $", format(gas_expense, '.2f'))
print("Accommodation:           $", format(accommodation_expense, '.2f'))
print("Food:                    $", format(food_expense, '.2f'))
print("Remaining Balance:       $", format(remaining_budget, '.2f'))
print("****************************************")

