# Initialize a variable to store the total grades
total_grades = 0

# Ask the user for 6 grades and add them to the total
for i in range(6):
  grade = int(input("Enter a grade out of 10: "))
  total_grades += grade

# Calculate the average by dividing the total by 6
average = total_grades / 6

# Print the average
print("The average grade is:", average)