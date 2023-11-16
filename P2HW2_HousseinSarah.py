#CTI-110
#P2HW2-List
#Sarah Houssein
#11/14/2023
#Enter grades for module tests

#Get input from user
module_1 = float(input("Enter grade for module_1: "))
module_2 = float(input("Enter grade for module_2: "))
module_3 = float(input("Enter grade for module_3: "))
module_4 = float(input("Enter grade for module_4: "))
module_5 = float(input("Enter grade for module_5: "))
module_6 = float(input("Enter grade for module_6: "))

#Create an empty list
grades = []

#Add values to the list
grades.append(module_1)
grades.append(module_2)
grades.append(module_3)
grades.append(module_4)
grades.append(module_5)
grades.append(module_6)


#Calculation methods
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

#Display Summary
print("\n----------Results--------------")
print(f"Lowest Grade: {lowest:.2f}")
print(f"Highest Grade: {highest:.2f}")
print(f"Sum of Grades: {total:.2f}")
print(f"Average: {average:.2f}")
print("\n-------------------------------")
