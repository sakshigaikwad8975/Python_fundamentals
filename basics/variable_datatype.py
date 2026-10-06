#Q1 Personal profile
# Create variables for your name, age, height, and whether you're a student. Print a formatted profile with each variable's value and data type.

name = "Sakshi Gaikwad"
age = 21
height = 1.62
profession = "student"
print("Name: ", name)
print(type(name))
print("Age: ", age)
print(type(age))
print("Height: ", height, "m")
print(type(height))
print("Profession: ", profession)
print(type(profession))

#Q2 Simple calculator
#Store two numbers in variables. Calculate and print their sum, difference, product, quotient, and remainder.

val_1 = 10
val_2 = 5
sum = val_1 + val_2
difference = val_1 - val_2
product = val_1 * val_2
division = val_1 / val_2
remainder = val_1 % val_2
quotient = val_1 // val_2

print("Sum: ", sum)
print("Difference: ", difference)
print("Product: ", product)
print("Division: ", division)
print("Remainder: ", remainder)
print("Quotient: ", quotient)

#Q3 Temperature converter
# Store a temperature in Celsius and convert it to Fahrenheit and Kelvin.

temp = 100
fahrenheit = (temp * 1.8) +32
kelvin = temp +273.15
print("Conversion of ", temp, "degree Celsius to Fahrenheit is", fahrenheit, "degree Fahrenheit and Kelvin is", kelvin, "degree Kelvin." )

#Q4 Swapping values
# Swap the values of two variables without using a third variable. Then solve it again using a temporary variable.

num1 = 6
num2 = 7
temp = num1
num1 = num2
num2 = temp
print (num1, " ", num2)

#Q5 Shopping Bill
# Store the prices and quantities of three products. Calculate each subtotal, the total bill, and the average item price.

price1 = 150 
price2 = 500
price3 = 750

quantity1 = 3
quantity2 = 4
quantity3 = 2

subtotal1 = price1 * quantity1
subtotal2 = price2 * quantity2
subtotal3 = price3 * quantity3

total_bill = subtotal1 + subtotal2 + subtotal3

avg_bill = (price1 + price2 + price3) /9

print("Subtotal of 1st item: ", subtotal1, "USD")
print("Subtotal of 2nd item: ", subtotal2, "USD")
print("Subtotal of 3rd item: ", subtotal3, "USD")
print("Total bill of 3 items is: ", total_bill, "USD")
print("Average item price is: ", avg_bill, "USD")

#Q6 Time converter
# Store a number of seconds and convert it into hours, minutes, and remaining seconds.
total_seconds = 5600
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds //60
seconds = remaining_seconds % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Remaining seconds:", seconds)

#Q7 Type conversion
# Take a numeric string and convert it into a integer and a float. Perform calculations with both.

num_string = input("Enter a number: ")
int_val = int(num_string)
float_val = float(num_string)

#integer calculations
print("Addition: ", int_val + 20)
print("Substraction: ", int_val - 12)
print("Multiplication: ", int_val *10)
print("Division: ", int_val / 10)
print("Floor division: ", int_val // 5)
print("Remainder: ", int_val % 15)

#float calculations
print("Addition: ", float_val + 20)
print("Substraction: ", float_val - 12)
print("Multiplication: ", float_val *10)
print("Division: ", float_val / 10)
print("Floor division: ", float_val // 5)
print("Remainder: ", float_val % 15)

#Q8 Salary breakdown
# Store a monthly salary. Calculate annual salary, a 10% bonus, and the final annual income.


monthly_salary = 20000
annual_salary = monthly_salary * 12
bonus = annual_salary  * 0.10
final_salary = annual_salary + bonus

print("Monthly Salary: ", monthly_salary)
print("Annual Salary: ", annual_salary)
print("Bonus: ", bonus)
print("Final Salary: ", final_salary)

#Q9 Data Summary
# Given variables representing a student's name, marks in three subjects, and attendance percentage, generate a formatted summary with total marks, average, and eligibility status based on attendance.

name = "Sakshi"
python = 89
java = 93
c = 87
attendance_percent = 98

total_marks = python + java + c
avg_marks = total_marks /3
percent =  (total_marks/300) * 100
print("Name - ", name)
print("Total marks - ", total_marks)
print("Percentage- ", percent)
print("Average- ", avg_marks)

if attendance_percent >= 75:
    print("Eligible")
else:
    print("Not eligible")

#Q10 Mini financial tracker
#Store income and expenses in separate variables. Calculate savings, savings rate, and projected annual savings. Handle a zero-income case.

income = 50000
spend = 20000
if income == 0:
    print("No saving")
else:
    savings = income - spend
    saving_rate = (savings/income)*100
    annual_saving = savings * 12

    print("Monthly income- ", income, "USD")
    print("Monthly expenses- ", spend, "USD")
    print("Savings- ", savings, "USD")
    print("Saving Rates- ", saving_rate)
    print("Auunal Saving- ", annual_saving, "USD")