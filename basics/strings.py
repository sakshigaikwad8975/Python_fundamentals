#Q1 Name formatter
# Take a full name and print it in uppercase, lowercase, title case, and with leading/trailing spaces removed.

#Q2
name = input("Enter your full name: ")
print("Full name in upper case: ", name.upper())
print("Full name in lower case: ", name.lower())
print("Full name in title case: ", name.title())
print("Full name without leading/trailing spaces: ", name.strip())


#Q2 Character counter 
# Count the number of vowels, consonants, digits, and spaces in a given string.
text = "sakshi was born in 2005"
vowels = 0
consonants = 0
digits = 0
spaces = 0
vowel_ref = "AEIOUaeiou"
for char in text:
    if char in vowel_ref:
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)

#Q3 Reverse a string 
# Reverse a string using slicing, then solve it again without slicing.
word = input("Enter a string: ")
sliced = word[0::-1]
reversed_str = word.__reversed__
print("Reversed string using slicing: ", sliced)


#Q4 Personal introduction 
# Take your first name and last name as input. Print your full name, then print its length.

#Q5 First and last character
# Take a word as input. Print its first character, last character, and length.

#Q6 String repetition
# Take a word as input and print it five times on the same line using the repetition operator.

#Q7 Username creator 
# Take a first name and birth year as input. Combine them to create a username, such as sakshi2005. Assume the birth year is entered as a string.

#Q8 Reverse a word
# Take a word as input and print it backward using slicing.

#Q9 Extract the middle
# Take a word with an odd number of characters and print only its middle character. For example, python should produce t.

#Q10 Initials generator
# Take a first name and a last name as separate inputs. Print their initials. For example, Sakshi and Gaikwad should produce S.G.

#Q11 Slice a secret code
# Take a string of exactly eight characters. Print the first three characters, the last three characters, and the four characters in the middle.

#Q12 Palindrome checker
# Take a word and determine whether it reads the same forward and backward. Print whether it is a palindrome. Assume the input contains lowercase letters only.

#Q13 Character-by-character display
# Take a word as input and print each character on a separate line using a for loop and indexing.