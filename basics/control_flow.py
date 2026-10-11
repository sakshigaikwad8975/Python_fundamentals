#Q1 Positive, negative, or zero
# Classify a number as positive, negative, or zero.
num1 = int(input("Enter a number: "))
if num1 > 0:
    print("The number is positive.")
elif num1 < 0 :
    print("The number is negative.")
else:
    print("The number is zero.")


#Q2 Grade calculator
# Assign a grade based on marks using a predefined grading scale.


marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks > 50:
    print("Grade D")
else:
    print("Pass")



#Q3 Voting eligibility
# Check whether a person meets the minimum voting age.

age = int(input("Enter you age: "))
if age >= 18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting.")

#Q4 Login simulation
# Compare a stored username and password against entered values. Print appropriate messages for correct and incorrect credentials.

username = "gaikwadsakshi"
password = "sakshi2005"
entered_username = input("Enter the username: ")
entered_password = input("Enter the password: ")
if username == entered_username and password == entered_password:
    print("Successful Login!!!")
elif username == entered_username and password != entered_password:
    print("Wrong Password")
elif username != entered_username and password == entered_password:
    print("Wrong username")
else:
    print("Wrong info!!!")

#Q5 Triangle classifier
# Given three side lengths, first check if they form a valid triangle, then classify it as equilateral, isosceles, or scalene.

a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("It's a triangle")
    if a == b and b == c:
        print("It's an equilateral triangle")
    elif a == b or b == c or a == c:
        print("It's an isosceles triangle")
    elif a != b or b != c or a != c:
        print("It's a scalene triangle")
else:
    print("It's not an triangle") 

#Q6 Ticket pricing
# Calculate ticket prices based on age, student status, and whether the visit is on a weekend.

age = int(input("Enter your age: "))
status = input("Are you a student: ")
visit = input("Are you visiting on a weekdend: ")
if age <= 12:
    print("Your ticket price is 100 USD")
    if status == "yes" or status == "Yes":
        print("You have 50 USD discount")
    if visit == "yes" or visit == "Yes":
        print("You have to pay 30 USD extra for weekend visit.")
    if age <= 12 and (status == "yes" or status == "Yes") and (visit == "yes" or visit == "Yes"):
        print("Your total charge is: ", 100-50+30)
    if age <= 12 and (status == "yes" or status == "Yes"):
            print("Your total charge is: ", 100-50)
    if age <= 12 and (visit == "yes" or visit == "Yes"):
            print("Your total charge is: ", 100+30)
elif age > 12:
    print("Your ticket price is 200 USD.")
    if status == "yes" or status == "Yes":
        print("You have 50 USD discount")
    if visit == "yes" or visit == "Yes":
        print("You have to pay 30 USD extra for weekend visit.")
    if age > 12 and (status == "yes" or status == "Yes") and (visit == "yes" or visit == "Yes"):
            print("Your total charge is: ", 200-50+30)
    if age > 12 and (status == "yes" or status == "Yes"):
            print("Your total charge is: ", 100-50)
    if age > 12 and (visit == "yes" or visit == "Yes"):
            print("Your total charge is: ", 100+30)

#Q7 BMI category
# Calculate BMI using weight and height, then classify the result using standard BMI ranges.

# weight = int(input("Enter weight in kg: "))
# height = int(input("Entner height is meters: "))
# bmi = weight / height
# if bmi <= 18.2:
#     print("Underweight")
# elif 18.5 <= bmi <= 24.9:
#     print("Healthy weight")
# elif 25.0 <= bmi <= 29.9:
#     print("Overweight")
# else:
#     print("Obesity")

#Q8 ATM withdrawal
# Simulate an ATM transaction. Check PIN, account balance, withdrawal amount, and whether the amount satisfies withdrawal constraints.

entered_pin = int(input("Enter PIN: "))


#Q9 Rock-paper-scissors
# Build a single-round game using nested conditionals. Compare the user's choice with a predefined computer choice.



# Q10 Smart admission system
# Determine admission eligibility using marks, entrance exam scores, and category-specific criteria. Clearly handle overlapping conditions.