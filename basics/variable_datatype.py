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
print("Conversion of ", temp, "degree Celcius to Fahrenheit is", fahrenheit, "degree Fahrenheit." )

#Q4 Swapping values
# Swap the values of two variables without using a third variable. Then solve it again using a temporary variable.

num1 = 6
num2 = 7
num1, num2 = 7, 6
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

avg_bill = price1 + price2 + price3 /3

print("Subtotal of 1st item: ", subtotal1, "USD")
print("Subtotal of 2nd item: ", subtotal2, "USD")
print("Subtotal of 3rd item: ", subtotal3, "USD")
print("Total bill of 3 items is: ", total_bill, "USD")
print("Average item price is: ", avg_bill, "USD")