#Q1 List operations
# Create a list of 10 numbers. Print the first, last, and middle elements. Add, remove, and update elements.

num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("First element of list is: ", num[0])
print("Last element of list is: ", num[9])
num.append(110)
print("Updated num is: ", num)
num.remove(30)
print("Updated list is: ", num)


#Q2 Shopping list
# Create a shopping list. Allow the user to add an item, remove an item, and view the updated list.

shopping_list = ["apple", "honey", "butter", "potato", "yogurt", "pineapple", "pastry"]
add_items = input("Do you want to add items?")
if add_items == "yes" or add_items == "Yes":
    updated_list = input("Enter items: ")
    shopping_list.append(updated_list)
else:
    print("No item to add")
remove_items = input("Do you want to remove items?")
if remove_items == "yes" or remove_items == "Yes":
    updated_list = input("Enter items: ")
    shopping_list.remove(updated_list)
print("Here's the final list: ", shopping_list)

#Q3 Find maximum and minimum
# Find the largest and smallest elements of a list without using max() or min().

num_list = [12, 69, 4, 7, 8, 10]
num_list.sort()
print("The largest element is list is ", num_list[0], " and smallest element is ", num_list[5])

#Q4 Remove duplicates
# Create a new list with duplicate values removed while preserving the original order.
# org_list = [1, 2, 2, 3, 4, 4, 1]
# new_list = []
# for num in org_list:
#     if num

#Q5 Separate even and odd
# Given a list of integers, create two separate lists for even and odd numbers.
int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
odd_list = []
for idx in int_list:
    if idx % 2 == 0:
        even_list.append(idx)
    else:
        odd_list.append(idx)
print("Even numbers list: ", even_list)
print("Odd numbers list: ", odd_list)

#Q6 Second largest
# Find the second-largest distinct number in a list without sorting it.



#Q7 List rotation
# Rotate a list to the right by k positions. Try a solution using slicing and another using loops.



#Q8 Matrix addition
# Represent two matrices as nested lists and calculate their element-wise sum.



#Q9 Flatten a nested list
# Convert a list of lists, such as [[1, 2], [3, 4], [5]], into a single flat list.



#Q10 Leaderboard
# Given a list of student names and a corresponding list of scores, produce a sorted leaderboard with rankings. Handle tied scores.