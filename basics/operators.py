#Q1 Even or odd
#Use the modulo operator to determine whether a given integer is even or odd.

number = 10
if number % 2 == 0:
    print(number, "is a even number.")
else:
    print(number, "is a odd number.")

#Q2 Number comparison
#Given three numbers, use comparison operators to identify the largest without using max().

num1 = 5
num2 = 7
num3 = 4
if num1 >= num2 and num1 >= num3:
    print(num1, "is greatest")
elif num2 >= num1 and num2 >= num1:
    print(num2, "is greatest")
else:
    print(num3, "is greatest")

#Q3 Discount calculator
# Calculate the final price of a product after a discount percentage using arithmetic operators.

price = 1000
discount = 9.8
final_price = 1000((100-9.8)/100)
print("Final price of item after", discount, "percent discount is", final_price, "USD.")

#Q4 Divisilbility checker
#  Check whether a number is divisible by both 3 and 5, either one, or neither.

nums = 15
if nums % 3 and nums % 5 ==0:
    print("Given number", nums, "is divisible by 5 and 3.")
elif nums % 3 or nums % 5 == 0:
    print("Given number", nums, "is divisible by 5 or 3.")
else: 
    print("Given number", nums, "is not divisible by 5 nor 3.")

#Q5 Age eligibility
# Check whether a person is eligible for a driving license based on age and whether they have a learner's permit.

#Q6 Range validation 
# Check whether a number lies between 10 and 100 inclusive using chained comparisons.

#Q7 Bitwise exploration
# Given two integers, display their bitwise AND, OR, XOR, left shift, and right shift results.

#Q8 Password conditions
# Check whether a password meets a minimum length requirement and whether it contains a specific required character.

#Q9 Leap year logic
# Determine whether a year is a leap year using logical and comparison operators.

#Q10 Electricity bill
# Calculate electricity charges using slab rates, such as one rate for the first 100 units, another for the next 100, and a third rate for units beyond 200.