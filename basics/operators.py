#Q1 Even or odd
#Use the modulo operator to determine whether a given integer is even or odd.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")

#Q2 Number comparison
#Given three numbers, use comparison operators to identify the largest without using max().

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
if num1 >= num2 and num1 >= num3:
    print(num1, "is greatest")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is greatest")
else:
    print(num3, "is greatest")

#Q3 Discount calculator
# Calculate the final price of a product after a discount percentage using arithmetic operators.

price = 1000
discount = 9
final_price = price * ((100- discount )/100)
print("Final price of item after", discount, "percent discount is", final_price, "USD.")

#Q4 Divisilbility checker
#  Check whether a number is divisible by both 3 and 5, either one, or neither.

nums =int(input("Enter a number: "))
if nums % 3== 0 and nums % 5 ==0:
    print("Given number", nums, "is divisible by 5 and 3.")
elif nums % 3 == 0 or nums % 5 == 0:
    print("Given number", nums, "is divisible by 5 or 3.")
else: 
    print("Given number", nums, "is not divisible by 5 nor 3.")

#Q5 Age eligibility
# Check whether a person is eligible for a driving license based on age and whether they have a learner's permit.

age = int(input("Enter your age: "))
permit = input("Do you have learners perimit: ")
if age >= 18 and (permit == "Yes" or permit == "yes"):
    print("Eligible for learner's permit.")
    print("Eligible for driving license.")
else:
    print("Not eligible for driving liscense and learner's permit.")

#Q6 Range validation 
# Check whether a number lies between 10 and 100 inclusive using chained comparisons.

value = int(input("Enter a number: "))
if 10 <= value <= 100:
    print("Given number lies between 10 to 100.")
else:
    print("Given number is not in range 10 to 100.")
#Q7 Bitwise exploration
# Given two integers, display their bitwise AND, OR, XOR, left shift, and right shift results.

#Q8 Password conditions
# Check whether a password meets a minimum length requirement and whether it contains a specific required character.

min_len = 10
req_char = "@"
password = input("Enter a password: ")

if len(password) < min_len:
    print(("Your password must contain at least 10 characters."))
elif req_char not in password:
    print(req_char, "is missing.")
else:
    print("Correct password!!!")
#Q9 Leap year logic
# Determine whether a year is a leap year using logical and comparison operators.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year!!!")
else:
    print(year, "is not a leap year.")
#Q10 Electricity bill
# Calculate electricity charges using slab rates, such as one rate for the first 100 units, another for the next 100, and a third rate for units beyond 200.

# used_units = int(input("Enter used units: "))
# first_unit = 2
# sec_unit = 4
# third_unit = 5
# if used_units <= 100:
#     first_price = used_units * first_unit
#     print("Price of 1st slab is ", first_price)
# elif 100 < used_units < 200:
#     second_unit = used_units - 100
#     sec_price = second_unit * sec_unit
#     final_sec_price = first_price + sec_price
    