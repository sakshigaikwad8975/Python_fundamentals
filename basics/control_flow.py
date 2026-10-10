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



#Q5 Triangle classifier
# Given three side lengths, first check if they form a valid triangle, then classify it as equilateral, isosceles, or scalene.



#Q6 Ticket pricing
# Calculate ticket prices based on age, student status, and whether the visit is on a weekend.



#Q7 BMI category
# Calculate BMI using weight and height, then classify the result using standard BMI ranges.



#Q8 ATM withdrawal
# Simulate an ATM transaction. Check PIN, account balance, withdrawal amount, and whether the amount satisfies withdrawal constraints.



#Q9 Rock-paper-scissors
# Build a single-round game using nested conditionals. Compare the user's choice with a predefined computer choice.



# Q10 Smart admission system
# Determine admission eligibility using marks, entrance exam scores, and category-specific criteria. Clearly handle overlapping conditions.