#CTI-110
#P4HW1-Score List
#Sarah Houssein
#11/28/2023
#Use loop to get user input

from statistics import mean


#Get number of grades from user
num_grades = int(input("How many grades will you enter? "))

#Create a list to store the grades entered
grades_list = []

#Get grades from user
for i in range(num_grades):
    grade = float(input(f"Enter grade for Module {i + 1}: "))
    while grade < 0 or grade > 100:
        print("You entered an invalid grade: ")
        grade = float(input(f"Enter grade for Module {i + 1}: "))
    grades_list.append(grade)

print(grades_list)


                 



#Call methods on the list to get results
list_sum = sum(grades_list)
list_avg = mean(grades_list)
lowest_grade = min(grades_list)
highest_grade = max(grades_list)

#Create a value for spacing
x = " "

#Output to user with f-string
print("\n")
print("------------Results------------")
print("Lowest Grade:", '    ', lowest_grade)
print("Highest Grade:", '   ', highest_grade)
print("Sum of Grades:", '   ', f"{list_sum:.2f}")
print("Average:", '         ', f"{list_avg:.2f}")
print("-------------------------------")

