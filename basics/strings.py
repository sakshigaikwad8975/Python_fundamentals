#Q1 Name formatter
# Take a full name and print it in uppercase, lowercase, title case, and with leading/trailing spaces removed.

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

#Q5 Personal introduction 
# Take your first name and last name as input. Print your full name, then print its length.

first_name = input("Enter you first name: ")
last_name = input("Enter you last name: ")
full_name = first_name + " " + last_name
print("Your full name is ", full_name, "with the length of", len(full_name),"characters.")

#Q6 First and last character
# Take a word as input. Print its first character, last character, and length.

word = input("Enter a word: ")
first_char = word[0]
last_char = word[len(word)-1]
word_len = len(word)
print("First character is", first_char, ", last character is", last_char, "and length of", word, "is", word_len )


#Q7 String repetition
# Take a word as input and print it five times on the same line using the repetition operator.

word_1 = input("Enter a word: ")
repeated_word = word_1 * 5
print(repeated_word)
#Q8 Username creator 
# Take a first name and birth year as input. Combine them to create a username, such as sakshi2005. Assume the birth year is entered as a string.

firstName = input("Enter your first name: ")
birth_yr = input("Enter your birth year: ")
username = firstName + birth_yr
print("Your username is: ", username)


#Q9 Reverse a word
# Take a word as input and print it backward using slicing.

word_3 = input("Enter a word: ")
reverse_word = word[0, len(word_3), -1]
print("Reversed word of", word_3, "is", reverse_word)

#Q10 Extract the middle
# Take a word with an odd number of characters and print only its middle character. For example, python should produce t.

#Q11 Initials generator
# Take a first name and a last name as separate inputs. Print their initials. For example, Sakshi and Gaikwad should produce S.G.

#Q12 Slice a secret code
# Take a string of exactly eight characters. Print the first three characters, the last three characters, and the four characters in the middle.

#Q13 Palindrome checker
# Take a word and determine whether it reads the same forward and backward. Print whether it is a palindrome. Assume the input contains lowercase letters only.

#Q14 Character-by-character display
# Take a word as input and print each character on a separate line using a for loop and indexing.