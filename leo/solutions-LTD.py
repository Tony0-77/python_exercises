#  Exercises 1 - 8  Strings (Level 1)

##exercise 1-8.2
# Write a Python program that prints the length of a string s.
s = "Leo"
print(len(s))

##exercise 1-8.4
"""Write a Python program that prints the character at index i in the string s.
    If the index is out of range, the program should print "i is out of range"
    If the string is empty, the program should print "Empty String\""""

s = "Leo"
i = 1

if len(s) == 0:
    print("Empty String")
elif i < 0 or i >= len(s):
    print(f"{i} is out of range")
else:
    print(s[i])

##exercise 1-8.6
"""Write a Python Program that prints the reversed version of a string.
    The program must preserve uppercase and lowercase letters.
    If the string is empty, print it intact."""

str_val = "Dellosa"
print(str_val[::-1])

##exercise 1-8.8
"""Write a Python program that prints the first and last three characters of the string s as a single string.
    If the string has less than six characters, print an empty string (blank output)."""

s = "Dellosa"
if len(s) < 6:
    print("") 
else:
    print(s[:3] + s[-3:]) 

##exercise 1-8.11
"""Write a Python program that prints the string s without the characters located at even indices.
    If the string is empty or only has one character, print it intact."""

s = "Pizza"
if len(s) <= 1:
    print(s)
else:
    print(s[1::2]) 

##exercise 1-8.13
"""Write a Python program that check if a string only contains numbers.
    If it does, print True. Else, print False."""

strOnly = "leodellosa85"
print(strOnly.isdecimal())

##exercise 1-8.15
"""Write a Python program that prints the string s without the character at index n.
    If the index n is out of range, print the string s intact.
    If the string s is empty, print the string s intact."""

strIdx = "leodellosa"
idx = 9
if(len(strIdx) == 0 or idx < 0 or idx >= len(strIdx)):
    print(strIdx)
else:
    print(strIdx[:idx] + strIdx[idx + 1:])

##exercise 1-8.17
"""Write a Python program that prints the string s with the character curr_char replaced by the character new_char.
    curr_char and new_char are variables that contain strings with a single character.
    You may assume that new_char will not be an empty string.
    The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).
    If no match is found, print the initial string."""

s = "Hello"
curr_char = "s"
new_char = "a"

print(s.replace(curr_char, new_char))

#  Exercises 9 - 16  Strings (Level 2)

##exercise 9-16.1
"""Write a Python program that prints a version of the string s with all commas 
    replaced by dots."""

s = "Leo,T,Dellosa"
COMMA = ","
DOT = "."
print(s.replace(COMMA, DOT))

##exercise 9-16.3
"""Write a Python program that checks if the string s contains all the letters in the alphabet (case-insensitive, so "A" should be equivalent to "a").
    If it does, print True. Else, print False.
    Before comparing the characters, you should convert the string to lowercase.
    If the string contains spaces, ignore them before finding the result.
    You may assume that the string doesn't contain any other symbols, only spaces (possibly).
    Consider these letters as part of the alphabet: 'abcdefghijklmnopqrstuvwxyz'"""

alphabet = set('abcdefghijklmnopqrstuvwxyz')
inputStr = "The quick brown fox jumps over the lazy dog"
s = inputStr.replace(" ", "").lower()
    
if alphabet.issubset(s):
    print(True)
else:
    print(False)

##exercise 9-16.5
"""Write a Python program that prints a copy of the string s without any spaces.
    Words should be connected in the final string.
    If the string doesn't contain spaces, print it intact."""

s = "Leo T. Dellosa"
print(s.replace(" ",""))

##exercise 9-16.7
"""Write a Python program that checks if the string s starts with the sequence of characters denoted by the variable prefix.
    If it does, print True. Else, print False.
    This test should be case sensitive. For example, "A" should not be equivalent to "a".
    If the length of the prefix is greater than the length of the string, print False."""

s = "Leo Dellosa"
prefix = "Leo"

print(s.startswith(prefix))

##exercise 9-16.9
"""Write a Python program that checks if the string s ends with a specific sequence of characters denoted by the variable suffix.
    If it does, print True. Else, print False.
    This test should be case sensitive. Therefore, "A" should not be equivalent to "a".
    If the length of the suffix is greater than the length of the string, print False."""

s = "Leo Dellosa"
suffix = "osa"

print(s.endswith(suffix))

##exercise 9-16.12
"""Write a Python program that reverses the individual words in the string s and changes their capitalization. Uppercase letters should be printed in lowercase and vice versa.
    Assume that the string only contains letters and spaces are used to separate words."""

s = "Leo T. Dellosa"
words = s.split()
result = []
for word in words:
    reversed_word = word[::-1]
    changed_case_word = reversed_word.swapcase() 
    result.append(changed_case_word)
    
print(" ".join(result))

##exercise 9-16.14
"""Write a Python program to count the number of repeated characters in the string s.
    The program must print the total number of repeated characters and a message on the next line displaying the repeated characters separated by a space and sorted alphabetically.
    If there are no repeated characters in the string, print 0 as the total count and None on the next line."""

s = "Leo Dellosa"
repeated_chars = []
for char in s:
	if (s.count(char) > 1) and (char not in repeated_chars):
		repeated_chars.append(char)
print(len(repeated_chars))

if repeated_chars:
	print(" ".join(sorted(repeated_chars)))
else:
	print(None)
     
##exercise 9-16.16
"""Write a Python program to convert a string s to lowercase, sort the characters of each word in alphabetical order, and print the resulting string.
    You may assume that the string only contains letters and spaces to separate the words.
    Spaces should be preserved in the final string."""

s = "Leo Dellosa"
new_str = ""
words_list = s.split(" ")
for word in words_list:
	new_str += "".join(sorted(word.lower())) + " "

print(new_str.rstrip())

#  Exercises 17 - 24  Lists and Tuples (Level 1)

##exercise 17-24.2

"""Write a Python program that multiplies all the items in a list by the value of the variable factor.
    The program must print the list as the output.
    The program should also allow multiplying the variable factor by a string in case the list contains strings.
    You may assume that the value of factor will be a positive integer."""

my_list = ["L", "e", "o"]
factor = 2
for i in range(len(my_list)):
	my_list[i] *= factor
print(my_list)

##exercise 17-24.4
"""Write a Python program that prints the elements of a list on the same line.
    The elements should be separated only by a space (not by a comma).
    The output should not include the opening and closing square brackets [ ]."""

my_list = ["L", "e", "o"]
print(" ".join(my_list))

##exercise 17-24.6
"""Write a Python program that prints the largest and smallest values in a list
    Print the two values on the same line, separated by a space.
    The largest value should appear first and the smallest value should appear second.
    You may assume that the list only contains numeric values.
    If the list is empty, print None."""

my_list = [0, 0, 0]
if my_list:
	print(max(my_list), min(my_list))
else:
	print(None)
      
##exercise 17-24.8
"""Write a Python program that checks if a list is empty or not.
    If the list is empty, print "Empty". Else, print "Not Empty"."""

my_list = []
if my_list:
	print("Not Empty")
else:
	print("Empty")
      
##exercise 17-24.11
"""Write a Python program that prints the elements of a list followed their corresponding indices.
    Each element and its index must be on the same line separated by a space.
    If the list is empty, print "Empty List"."""

my_list = ["L","e","o"]
if my_list:
	for idx, value in enumerate(my_list):
            print(value, idx)
else:
	print("Empty")
      
##exercise 17-24.13
"""Write a Python program that removes all occurrences of the element elem_to_remove from a list.
    The output of the program should be the new list with the element removed.
    If the element is not found in the list, print the message "Not Found".
    If the list is empty, print "Empty List"."""

my_list = ["D","e","l","l","o","s","a"]
elem_to_remove = "s"      
if len(my_list) == 0:
    print("Empty List")
elif elem_to_remove not in my_list:
    print("Not Found")
else:
    lst = [elem for elem in my_list if elem != elem_to_remove]
    print(lst) 

##exercise 17-24.15
"""Write a Python program that removes duplicate elements from a list, only keeping one occurrence of each element in the list.
    The original list should be mutated (modified).
    The program must print the final version of the list."""

my_list = [1, 1, 2, 3, 4, 4]
no_duplicates = list(set(my_list))
print(no_duplicates)

##exercise 17-24.17
"""Write a Python program that counts the number of elements in a list with value greater than 3.
    You may assume that the list only contains numbers.
    Print the final count."""

my_list = [1, -1, 0, 2, 2, 3, 4]
count = sum(1 for elem in my_list if elem > 3)
print(count)

# Exercises 25 -  32  Lists and Tuples (Level 2)

##exercise 25-32.1
"""Write a Python program that prints (as a list) the elements of listA that are not in listB as a list.
    If the lists have the same elements, print an empty list.
    If listA is an empty list, print an empty list."""

listA = [1, 2, 3, 4]
listB = [1, 2]
difference = []
for elem in listA:
	if elem not in listB:
		difference.append(elem)

print(difference)

##exercise 25-32.3
"""Write a Python program that calculates the distance between two 3D points.
    The points are represented by two lists with three elements. The first element is 
    the x-coordinate. The second element is the y-coordinate. The third element is the z-coordinate."""

pointA = [3, 4, 5]
pointB = [1, 3, 5]

distance = ((pointA[0] - pointB[0])**2
			+ (pointA[1] - pointB[1])**2
			+ (pointA[2] - pointB[2])**2)**(1/2)

print(distance)

##exercise 25-32.5
"""Write a Python program that prints a list with the elements that listA and listB have in common.
    If they don't have any elements in common, print an empty list.
    The program should not assume that the lists have the same length.
    You may assume that each element will only appear once in each list."""

listA = [1, 2, 3, 4]
listB = [1, 2, 3, 4]

common_elem = []

for elem in listA:
	if elem in listB:
		common_elem.append(elem)

print(common_elem)

##exercise 25-32.7
"""Write a Python program that prints the second largest value in a list.
    If the list is empty or only has one element, print None."""

my_list = [1, 2, 3, 4]

if len(my_list) > 1:
	no_duplicates = set(my_list)
	no_duplicates.remove(max(no_duplicates))
	print(max(no_duplicates)) 
else:
	print(None)
	
##exercise 25-32.10
"""Write a Python program that prints the second smallest value in a list.
    If the list is empty or only has one element, print None."""

my_list = [1, 2, 3, 4]

if len(my_list) > 1:
	no_duplicates = set(my_list)
	no_duplicates.remove(min(no_duplicates))
	print(min(no_duplicates)) 
else:
	print(None)
	
##exercise 25-32.12
"""Write a Python program that creates and print a dictionary that maps each element in a list to its corresponding frequency (how many times it occurs in the list).
    The test should be case-sensitive. Therefore, "A" should not be considered the same element as "a"."""

my_list = ["a", "a", "b", "c", "a", "b"]

freq_dict = {}

for elem in my_list:
	if elem not in freq_dict:
		freq_dict[elem] = 1
	else:
		freq_dict[elem] += 1

print(freq_dict)

##exercise 25-32.14
"""Write a Python program that prints a "flattened" version of a list that contains nested lists.
    "Flattened" means that all the elements in the nested lists should be added to a main list such that it doesn't contain any nested lists, just the individual.
    The list could contain other elements that are not lists or other sequences, so you must check the type of each element and act appropriately.
    If the list is empty, print an empty list."""

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = []

for elem in my_list:
	if isinstance(elem, list):
		for nested_elem in elem:
			flat_list.append(nested_elem)
	else:
		flat_list.append(elem)

print(flat_list)

##exercise 25-32.16
"""Write a Python program that generates and prints all the possible permutations of a list.
    A permutation is a possible arrangement of the elements of the list. For example, [2, 1, 3] is a permutation of [1, 2, 3].
    Print each permutation as a list on a separate line. You can print them as lists or tuples.
    Include the list itself as a permutation."""

import itertools

my_list = [1, 2, 3]
permutations = list(itertools.permutations(my_list))
for permutation in permutations:
	print(permutation)
	
#Exercises 33 - 38  Dictionaries (Level 1)

##exercise 33-38.2
"""Write a Python program that checks if a key exists in a dictionary or not.
    If the key exists in the dictionary, print True. Else, print False.
    The key should be stored in the variable key."""

my_dict = {"a": 1, "b": 2, "c": 3}
key = "d"
print(key in my_dict)

##exercise 33-38.4
"""Write a Python program that adds a new key-value pair to a dictionary only if the key doesn't exist already.
    If the key-value pair exists in the dictionary, do not update the existing value. The dictionary should not be modified in this case.
    Store the new key in the new_key variable and the new value in the new_value variable.
    Print the final value of the dictionary."""

my_dict = {"January": 45, "February": 56, "March": 67}

new_key = "May"
new_value = 1
if new_key not in my_dict:
	my_dict[new_key] = new_value

print(my_dict)

##exercise 33-38.6
"""Write a Python program that merges two dictionaries and prints the resulting dictionary.
    "Merging" the dictionaries involves making a new dictionary with the key-value pairs in both dictionaries."""

my_dict1 = {"a": 1, "b": 2, "c": 3}
my_dict2 = {"c": 4, "d": 6, "e": 8}
final_dict = my_dict1 | my_dict2
print(final_dict)

##exercise 33-38.9
"""Write a Python program that checks if all values in a dictionary are equal.
    If they are, print True. Else, print False.
    If the dictionary is empty, print "Empty"."""

my_dict = {"a": 4, "b": 4, "c": 4}
num_unique_values = len(set(my_dict.values()))
if num_unique_values == 0:
	print("Empty")
elif num_unique_values == 1:
	print(True)
else:
	print(False)
	
##exercise 33-38.11
"""Write a Python program that prints the largest value in a dictionary.
    If the dictionary is empty, print None.
    You may assume that the values are numeric."""

my_dict = {"a": 4, "b": 3, "c": 7}
if my_dict:
	max_value = max(set(my_dict.values()))
	print(max_value)
else:
	print(None)
	
##exercise 33-38.13
"""Write a Python program that prints the smallest value in a dictionary.
    If the dictionary is empty, print None.
    You may assume that the values are numeric."""

my_dict = {"a": 4, "b": 3, "c": 7}
if my_dict:
	max_value = min(set(my_dict.values()))
	print(max_value)
else:
	print(None)
	
# Exercises 39 - 44  Dictionaries (Level 2)

##exercise 39-44.1
"""Write a Python program that counts the frequency of each value in a dictionary.
    The program should create a new dictionary to map each value in the original dictionary to its frequency (how many times it occurs).
    If the dictionary is empty, print an empty dictionary."""

my_dict = {
	"a": 4,
	"b": 4,
	"c": 2,
	"d": 7,
	"e": 4,
	"f": 2,
	"g": 7,
	"h": 7
 }
freq_dict = {}
for value in my_dict.values():
	if value in freq_dict:
		freq_dict[value] += 1
	else:
		freq_dict[value] = 1

print(freq_dict)

##exercise 39-44.3
"""Write a Python program that creates a dictionary from the values contained in nested lists.
    Each nested list has this format [value1, value2].
    value1 should be the key in the dictionary and value2 should be its corresponding value.
    If there are no nested lists, print an empty dictionary."""

my_list = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]
new_dict = {}
for nested_list in my_list:
	key = nested_list[0] 
	value = nested_list[1]
	new_dict[key] = value

print(new_dict)

##exercise 39-44.5
"""Write a Python program that prints the largest of the values in a dictionary.
    You may assume that all the values in the dictionary are either lists or tuples."""

my_dict = {
	"a": [1, 2, 3],
	"b": [4, 0, -4],
	"c": [3, 5, 9],
	"d": [45, 12, 100]
}
max_sum = None
for list_value in my_dict.values():
	list_sum = sum(list_value)
	if max_sum is None:
		max_sum = list_sum
	elif max_sum < list_sum:
		max_sum = list_sum

print(max_sum)

##exercise 39-44.8
"""Write a Python program that creates and displays a dictionary that maps each letter in a string to how many times the character occurs in the string (its frequency).
    The dictionary should only include the characters in the string. 
    The test should be case-insensitive ("A" should be counted as "a").
    The keys in the dictionary should be lowercase letters.
    Only include letters in the dictionary."""

my_string = "Leo Dellosa"
freq_dict = {}
for char in my_string.lower():
	if char.isalpha():
		if char in freq_dict:
			freq_dict[char] += 1
		else:
			freq_dict[char] = 1

print(freq_dict)

##exercise 39-44.10
"""Write a Python program that sorts (in ascending order) the lists contained as values in a dictionary.
    The dictionary contains key-value pairs that match strings to lists. You need to sort these lists.
    The lists have to be mutated (changed)."""

my_dict = {
	"a": [4, 3, 2],
	"b": [5, 3, 7],
	"c": [1, 9, 10],
	"d": [3, 4, 1]
}
for list_value in my_dict.values():
	list_value.sort()

print(my_dict)

##exercise 39-44.12
"""Write a Python program that takes the content of a dictionary and converts it into a list of lists.
    Each nested list should contain a key as the first element and its corresponding value as the second element.
    Print the final list of lists."""

product_info = {
	"description": "shoe",
	"price": 4.56,
	"colors": ["green", "blue", "red"],
}
new_list = []
for key, value in product_info.items():
	new_list.append([key, value])

print(new_list)

# Exercises 45 - 50  Programs with Conditionals (Level 1)

##exercise 45-50.2
"""Write a Python program that prints if a number num is either
 "Positive", "Negative", or "Zero"."""

num = 5
if num == 0:
	print("Zero")
elif num > 0:
	print("Positive")
else:
	print("Negative")
	
##exercise 45-50.4
"""Write a Python program that prints a descriptive message indicating if each character in a string is a vowel or a consonant. For example: "<char> is a <consonant | vowel>"
    If the character is a special character, number, or symbol, print "<char> is not a letter".
    If the string is empty, print "Empty String"."""

text = "Leo: 36"
if not text:
	print("Empty String")
else:
	for char in text.lower():
		if char in ("a", "e", "i", "o", "u"):
			print(f"{char} is a vowel")
		elif not char.isalpha():
			print(f"{char} is not a letter")
		else:
			print(f"{char} is a consonant")
			
##exercise 45-50.6
"""Write a Python program that prints the maximum of three integers (a, b, c)."""

a = -5
b = -3
c = -4
print(max(a, b, c))

##exercise 45-50.9
"""Write a Python program that prints the smallest of three integers a, b, and c."""

a = -5
b = -3
c = -4
print(min(a, b, c))

##exercise 45-50.11
"""Write a Python program that prints the corresponding season based on the value of the variable season_num.
    The possible values of season_num are: 1 for Spring, 2 for Summer, 3 for Fall, 4 for Winter.
    If the value of season_num is neither one of these values, print "Please enter a valid number"."""

season_num = 22
if season_num == 1:
	print("Spring")
elif season_num == 2:
	print("Summer")
elif season_num == 3:
	print("Fall")
elif season_num == 4:
	print("Winter")
else:
	print("Please enter a valid number")
	
##exercise 45-50.13
"""Write a Python program that prints "Equal" if three numbers a, b, and c are equal.
    If at least one number if different, the program should print "Not Equal"."""

a = 1
b = 1
c = 1
if a == b == c:
	print("Equal")
else:
	print("Not Equal")
	
# Exercises 51 - 56  Programs with Conditionals (Level 2)

##exercise 51-56.1
"""Write a Python program that prints the number of days in a given month.
    The value of the variable month is the name of the month with the first letter capitalized.
    Do not consider leap years for the number of days in February.
    You can add a customized message. For example: "<month> has: <num_days> days."/"""

month = "July"
months_31_days = ("January", "March", "May", "July", 
					"August", "October", "December")
months_30_days = ("April", "June", "September", "November")
if month in months_31_days:
	print(f"{month} has: 31 days")
elif month in months_30_days:
	print(f"{month} has: 30 days")
else:
	print(f"{month} has: 28 days")
	
##exercise 51-56.3
"""Write a Python program that determines if three numbers (a, b, and c) are in increasing order, decreasing order, or none.
    If a > b > c, print "Decreasing Order".
    If a < b < c, print "Increasing Order".
    Else, print "None". """

a = 3
b = 2
c = 1
if a > b > c:
	print("Decreasing Order")
elif a < b < c:
	print("Increasing Order")
else:
	print("None")
	
##exercise 51-56.5
"""Write a Python program that prints the positive and negative solutions (roots) for a quadratic equation.
    If the equation only has one solution, print the solution as the output.
    If it has two solutions, print the negative one first and the positive one second on the same line.
    If the equation has no real solutions, print "Complex Roots".
    You can determine the number of solutions with the discriminant (the result of b^2 - 4ac in the formula below).
    - If it's negative, the equation has no real solutions (only complex roots).
    - If it's 0, there is only one solution.
    - If it's positive, there are two real solutions.
    A quadratic equation has this form:
        ax^2 + bx + c = 0
    For example:
        x^2 + 2x + 1 = 0
    To solve this equation, we use the quadratic formula:
    We find the result by replacing the values of a, b, and c in the formula."""

import math

a = 2
b = 5 
c = -3
discriminant = b**2 - 4*a*c
if discriminant < 0:
	print("Complex Roots")
elif discriminant == 0:
	r = (-b + math.sqrt(discriminant))/(2*a)
	print(r)
else:
	r1 = (-b - math.sqrt(discriminant))/(2*a)
	r2 = (-b + math.sqrt(discriminant))/(2*a)
	print(r1, r2)
	
##exercise 51-56.8
"""Write a Python program that prints if a given year was (or will) be a leap year.
    Tip: A leap year is "a year, occurring once every four years, that has 366 days including February 29 as an intercalary day." (Definition by Oxford Languages).
    This is how you can determine if a year is a leap year or not:
    if (year is not divisible by 4) then (it is a common year).
    else if (year is not divisible by 100) then (it is a leap year)
    else if (year is not divisible by 400) then (it is a common year)
    else (it is a leap year)"""

year = 1993
if year % 400 == 0:
	print(f"{year} is a leap year")
elif year % 100 == 0:
	print(f"{year} is not a leap year")
elif year % 4 == 0:
	print(f"{year} is a leap year")
else:
	print(f"{year} is not a leap year")
	
##exercise 51-56.10
"""Write a Python program that simulates an interactive calculator with the basic arithmetic operations in Python (addition, subtraction, multiplication, division, integer division, and modulo).
    The program must interact with the user by asking for the values and the type of operation that will be performed.
    The output should include the values, the operation, and the result (as shown below).
    The type of operation will be denoted by an integer.
        - 1 for addition
        - 2 for subtraction
        - 3 for multiplication
        - 4 for division
        - 5 for integer division
        - 6 for modulo
    The program should present an initial message to the user describing the types of operations and the integer that has to be entered to select each one of them.
    If the values entered by the user are invalid for the operation selected, a descriptive message should be displayed. For example, for a division operation the denominator cannot be 0.
    If the user enters an invalid integer to select the operation, print
    "Please choose a valid operation"/"""

ADDITION = 1
SUBTRACTION = 2
MULTIPLICATION = 3
DIVISION = 4
INTEGER_DIVISION = 5
MODULO = 6

print("=== Welcome to your Interactive Python Calculator ===")

a = int(input("Please enter the first value: "))
b = int(input("Please enter the second value: "))

print("Great! Now enter the operation.")
print("These are the available options:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Integer Division")
print("6 - Modulo")

operation = int(input("--> Enter the corresponding integer: "))

if operation == ADDITION:
	result = a + b
	print(f"The result of {a} + {b} is: {result}")
elif operation == SUBTRACTION:
	result = a - b
	print(f"The result of {a} - {b} is: {result}")
elif operation == MULTIPLICATION:
	result = a * b
	print(f"The result of {a} * {b} is: {result}")
elif operation == DIVISION:
	if b == 0:
		print("Division by Zero. Please enter another value for b.")
	else:
		result = a / b
		print(f"The result of {a} / {b} is: {result}")
elif operation == INTEGER_DIVISION:
	if b == 0:
		print("Division by Zero. Please enter another value for b.")
	else:
		result = a // b
		print(f"The result of {a} // {b} is: {result}")
elif operation == MODULO:
	result = a % b
	print(f"The result of {a} % {b} is: {result}")
else:
	print("Please choose a valid operation.")
	
##exercise 51-56.12
"""Write a Python program that simulates the "Rock, Paper, Scissors" game.
    The game should ask the user to enter an option (either "Rock", "Paper", or "Scissors").
    The player should play against the computer, which will select a random option.
    The computer's selection will be compared against the player's selection to determine who wins.
"""

import random

options = ("rock", "paper", "scissors")
computer = options[random.randint(0, 2)]

print("====== Welcome to the game ======")
player = input("Please enter Rock, Paper, or Scissors below:\n")

if player.lower() == computer:
    print("It's a tie! Try again.")
elif player.lower() == "rock":
    if computer == "paper":
        print("You lose! Your opponent chose 'Paper'")
    else:
        print("You win! Your opponent chose 'Scissors'") 
elif player.lower() == "paper":
    if computer == "scissors":
        print("You lose! Your opponent chose 'Scissors'")
    else:
        print("You win! Your opponent chose 'Rock'")
elif player.lower() == "scissors":
    if computer == "rock":
        print("You lose! Your opponent chose 'Rock'")
    else:
        print("You win! Your opponent chose 'Paper'")
else:
    print("Please enter a valid option.")
	
# Exercises 57 - 63  For Loops and While Loops (Level 1)

##exercise 57-63.2
"""Write a Python program that prints the first 15 positive integers (starting from 1).
    Print the numbers one per line using a loop and the range() function."""

for i in range(1, 16):
	print(i)
	
##exercise 57-63.4
"""Write a Python program that prints the integers between a given number n and 1 (in descending order, both inclusive).
    The value of n should be entered by the user and you may assume that it is an integer greater than or equal to 1.
    Use a loop to print each number on a separate line."""

inputted = int(input("Enter the value of 'n': "))
for i in range(inputted, 0, -1):
	print(i)
	
##exercise 57-63.6
"""Write a Python program that calculates and prints the sum of the first 100 non-negative integers (from 1 to 100).
    Use a loop to find this sum."""

total = 0
for i in range(1, 101):
	total += i

print(total)

##exercise 57-63.8
"""Write a Python program that prints the multiplication table for a positive integer n.
    The values displayed should go from n x 1 up to n x 10 with a descriptive format (as shown below).
    Use a loop to implement your solution."""

n = int(input("Enter the value of 'n': "))
print(f"===== Multiplication Table of {n} =====")

for i in range(1, 11):
	print(f"{n} x {i} = {n * i}")

##exercise 57-63.11
"""Write a Python program that prints all the letters in the alphabet using a loop (one letter per line).
    The program should print the letters in uppercase."""

for i in range(65, 91):
	print(chr(i))
	
##exercise 57-63.13
"""Write a Python program that prints the first 100 even numbers (from 2 to 200 inclusive)."""

for i in range(2, 201, 2):
    print(i)
	
##exercise 57-63.15
"""Write a Python program that calculates the factorial of a given number n.
    The value of n should be entered by the user.
    The program must print the result and use a loop to calculate it.
    The factorial of a number n is denoted as n! and it is the result of multiplying all the positive integers that are less than or equal to n.
    For example, 3! = 3 * 2 * 1.
    0! is equal to 1."""

n = int(input("Enter the value of 'n': "))
factorial = 1
for i in range(2, n+1):
	factorial *= i

print(factorial)

##exercise 57-63.17
"""Try to implement the previous exercises using While loops.
    While loops continue running while a given condition is True, 
	so you will have to adapt the solutions and write conditions to stop the loop at the appropriate moment."""

factorial = 1
i = 1
while i <= n:
    factorial *= i 
    i += 1 
print(factorial)

# Exercises 64 - 71  For Loops and While Loops (Level 2)

##exercise 64-71.1
"""Write a Python program that checks if a number is prime or not.
    If the number is prime, it should print "Prime".
    If the number is not prime, it should print "Not prime".
    A prime number is only divisible by 1 and by itself. It is not the product of two smaller natural numbers."""

num = int(input("Enter an integer: "))

if num == 0 or num == 1:
	print("Not Prime")
else:
	for i in range(2, num):
		if num % i == 0:
			print("Not Prime")
			break
	else:
		print("Prime")
		
##exercise 64-71.3
"""Write a Python program that prints a triangular pattern like the ones shown below in the examples.
    Each row must have its corresponding number of asterisks. The first row contains one asterisk. The second row contains two asterisks. The third row contains three asterisks and so on.
    The number of rows should be determined by the value of n, a value entered by the user."""

n = int(input("Enter an integer: "))
for i in range(1, n + 1):
	print("*" * i)

##exercise 64-71.5
"""Write a Python program that prints the digits of a number in reverse order on the same line.
    If the number only has one digit, print this digit."""

num = 123
number_str = str(num)
for digit in reversed(number_str):
    print(digit, end='')
	
##exercise 64-71.7
"""Write a Python program that prints a string reversed using a loop.
    All the characters must be on the same line in reverse order."""

print()
str_val = "Leo"
for digit in reversed(str_val):
    print(digit, end='')
	
##exercise 64-71.10
"""Write a Python program that prints a pyramid pattern made with asterisks.
    The number of rows should be determined by the value of the variable n. This value will be entered by the user.
    You may assume that the value of n is a positive integer."""
print()
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

##exercise 64-71.12
"""Write a Python program that prints Floyd's Triangle with n number of rows.
    The value of n should be entered by the user. You may assume that it is a positive integer.
    Floyd's Triangle is made with consecutive numbers that fill the rows of the triangle (as shown below)."""
print()
input_row = int(input("Enter the number of rows: "))
count = 1
for i in range(1, input_row + 1):
    for j in range(i):
        print(count, end=" ")
        count += 1
    print()
	
##exercise 64-71.14
"""Write a Python program that prints a triangular pattern made with letters (as shown below).
    The first row should have one letter A (in uppercase). The second row should have two letters B. The third row should have three letters C and so on.
    The number of rows is determined by the value of n, which is entered by the user.
    The letters must be separated by a space."""

num_rows = int(input("Enter the number of rows: "))
for i in range(1, num_rows + 1):
    letter = chr(64 + i) 
    for j in range(i):
        print(letter,end=" " if j < i - 1 else "")
    print(sep="")
	
##exercise 64-71.16
"""Write a Python program that prints a diamond made with asterisks where the diamond's height (number of rows) is determined by the value of the variable height
    You can (optionally) ask the user to enter the value of height.
    This value can only have an odd number of rows, so you should print a descriptive message if the user enters an even value."""

height = int(input("Enter the diamond's height (an odd number): "))
if height % 2 == 0:
    print("The height must be an odd number.")
else:
    middle = height // 2 + 1
    for i in range(1, middle + 1):
        print(" " * (middle - i), end="")
        print("*" * (2 * i - 1))
    for i in range(middle - 1, 0, -1):
        print(" " * (middle - i), end="")
        print("*" * (2 * i - 1))

# Exercises 72 - 76  Recursion (Level 1)

##exercise 72-76.2
"""Write a Python program that finds the sum of a list (or tuple) of numbers recursively.
    Print the total sum.
    If the list (or tuple) is empty, print 0."""

def recursive_sum(numbers):
    if not numbers:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])

numbers = [1, 2, 3, 4, 5]
total_sum = recursive_sum(numbers)
print(f"The total sum is: {total_sum}")

##exercise 72-76.4
"""Write a Python program that calculates and prints the nth Fibonacci number.
    The value of n represents the position of the element in the sequence.
    The initial value of n should be 0.
    You may assume that the value of n is a non-negative integer."""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 9
fib_number = fibonacci(n)
print(f"The Fibonacci number at position {n} is: {fib_number}")

##exercise 72-76.6
"""Write a Python program that calculates and prints the value of the factorial of the number num using recursion.
    The factorial of a number x is denoted by x! and it is equal to x * (x-1) * (x-2) * ... * 1, the product of all positive integers less than or equal to the number.
    The value of 0! is equal to 1 by mathematical convention."""

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

num = 3
fact_value = factorial(num)
print(f"The factorial of {num} is: {fact_value}")

##exercise 72-76.9
"""Write a Python program that calculates and prints the sum of the digits of a positive integer num.
    The program must find the sum recursively.
    If the integer has only one digit, print the integer as the total sum."""

def sum_of_digits(num):
    if num < 10:
        return num
    return num % 10 + sum_of_digits(num // 10)

num = 123
total_sum = sum_of_digits(num)
print(f"The sum of the digits of {num} is: {total_sum}")

##exercise 72-76.11
"""Write a Python program that find the value of a raised to the power b recursively.
    The operation is a**b in Python, where a is the base and b is the exponent.
    If the value of b is 0, the result is automatically 1 because every number raised to the power 0 is 1."""

def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

base = 2  
exponent = 3  
result = power(base, exponent)
print(f"The result of {base} raised to the power of {exponent} is: {result}")

# Exercises 77 - 82  Recursion (Level 2)

##exercise 77-82.1
"""Write a Python program that finds and prints the Greatest Common Divisor (GCD) of the numbers a and b (the largest number that divides them both)."""

a = 60
b = 48
print(math.gcd(a, b))

##exercise 77-82.3
"""Write a Python program that checks if a string is a palindrome or not (if it's read the same backwards and forwards).
    The program should be case-insensitive. Therefore, "A" should be considered equivalent to "a".
    Print True if the string is a palindrome. Else, print False.
    If the string is empty, print True."""

word_palindrome = "Anna"
word_palindrome = word_palindrome.lower()
print(word_palindrome == word_palindrome[::-1])

##exercise 77-82.5
"""Write a Python program that counts the number of vowels in a string recursively.
    If the string is empty or only contains one consonant, print 0.
    The program should be case-insensitive. Therefore, vowels in uppercase should also be counted."""

def count_vowels(s):
    if not s:
        return 0
    vowels = "aeiouAEIOU"
    
    if s[0] in vowels:
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])

str = "Leo Dellosa"  
vowel_count = count_vowels(str)
print(f"The number of vowels in the string is: {vowel_count}")

##exercise 77-82.8
"""Write a Python program that prints the pattern of asterisks shown below for a given value of n.
    The program must include a recursive function.
    n represents the number of rows in the resulting pattern and the number of asterisks printed on the first row."""

# n_pattern = int(input("Enter the number of rows: "))
# for i in range(n, 0 ,-1):
#     print("*" * i)
	
def print_pattern(n):
	if n == 1:
		print("*")
	else:
		print("*" * n)
		print_pattern(n-1)

n_rows = 3
print_pattern(n_rows)

##exercise 77-82.10
"""Write a Python program that converts a decimal number to binary using recursion.
    The function must return the binary representation as a string.
    The program must print the value returned."""

def decimal_to_binary(n):
    if n == 0:
        return ""
    return decimal_to_binary(n // 2) + str(n % 2)

decimal_number = 34
if decimal_number == 0:
    print("0")
else:
    print(decimal_to_binary(decimal_number))

##exercise 77-82.12
"""Write a Python program that implements the Binary Search algorithm recursively.
    The function should search for an element in a list or sequence and return its index.
    If the element is not found, the value returned should be -1."""

def binary_search(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)

arr = [1, 2, 3]
target = 4
print(binary_search(arr, 0, len(arr) - 1, target))

# Exercises 83 - 87  Working with Files (Level 1)

##exercise 83-87.2
"""Write a Python program that reads a text file and saves its content line by line to a list called file_content.
    The list should contain strings that represent each line of the text file.
    The program should print the resulting list."""

file_path = "exercise 83_87_2.txt"
file_content = []
with open(file_path) as file:
	for line in file:
		file_content.append(line)
print(file_content)

##exercise 83-87.4
"""Write a Python program that reads a text file and prints the first n lines of the file.
    The value of n should be entered by the user.
    If the value of n is greater than the total number of lines in the file, print
    "Please enter a value for n. The file has <num_lines> lines"."""

num_line = int(input("How many lines would you like to read?: "))
with open(file_path) as file:
	lines = file.readlines()
	num_lines = len(lines)
	if num_lines < num_line:
		print(f"Please enter a valid value. The file has {num_lines} lines.")
	else:
		for i in range(num_line):
			print(lines[i].strip())

##exercise 83-87.7
"""Write a Python program that prints the last n lines of a text file in order.
    The value of n should be provided by the user.
    You may assume that n is a valid positive integer."""

n = int(input("How many lines would you like to read?: "))
with open(file_path) as file:
	lines = file.readlines()
	num_lines = len(lines)
	if num_lines < n:
		print(f"Please enter a valid value. The file has {num_lines} lines.")
	else:
		for i in range(-n, 0):
			print(lines[i].strip())	

##exercise 83-87.9
"""Write a Python program that finds and prints the longest word in a text file.
    For this challenge, you may assume that the file only contains one word per line."""

file_path = "exercise 83_87_9.txt"
longest_word = ""
with open(file_path) as file:
	for word in file:
		if len(word) > len(longest_word):
			longest_word = word
print(longest_word)

##exercise 83-87.11
"""Write a Python program that creates and prints a frequency dictionary of the words found in a text file.
    The keys of the dictionary should be the words in the file.
    The values should be their frequencies.
    You may assume that each line of the file only contains one word."""

file_path = "exercise 83_87_9.txt"
freq_dict = {}
with open(file_path) as file:
	for word in file:
		word = word.strip("\n")
		if word not in freq_dict:
			freq_dict[word] = 1
		else:
			freq_dict[word] += 1
print(freq_dict)

# Exercises 88 - 91  Working with Files (Level 2)

##exercise 88-91.1
"""Write a Python program that writes the elements of a list to the file denoted by the variable file.
    Each element should be written on a separate line.
    The file should be new or its existing content must be replaced by this new content."""

file_path = "exercise 88_91_1.txt"
my_list = [1, 2, 3, 4, 5]
with open(file_path, "w") as file:
	for elem in my_list:
		file.write(str(elem)+ "\n")
		
##exercise 88-91.3
"""Write a Python program that counts the number of characters in a file.
    Count all the characters in the file, including commas and quotes.
    Do not count spaces and remove \n (new line) characters."""

file_path = "exercise 88_91_3.txt"
character_count = 0
with open(file_path) as file:
	for line in file:
		character_count += len(line.replace(" ", "").strip("\n"))
print(character_count)

##exercise 88-91.6
"""Write a Python program that copies the content of a file to another file.
    If the new file doesn't exist, the program should create it."""

file_path = "exercise 88_91_3.txt"
copy_path = "exercise 88_91_3_copy.txt"
with open(file_path) as file, open(copy_path, "w") as copy:
	for line in file:
		copy.write(line)
		
##exercise 88-91.8
"""Write a Python program that checks if a file exists in the specified path or not.
    If it exists, print "The file <file_name> exists"
    If it doesn't, print "The file <file_name> doesn't exist"
    The file name could also be an absolute path to the file."""

import os.path

my_file = "exercise 88_91_32.txt"
if os.path.isfile(my_file):
    print(f"The file {my_file} exists")
else:
    print(f"The file {my_file} doesn't exist")
	
# Exercises 92 - 97  Miscellaneous and More Challenging Programs (Level 1)

##exercise 92-97.2
"""Write a Python program that displays the current date and time.
    The program should print Current Date and Time: on the previous line.
    The date should be formatted as YYYY-MM-DD
    The time should be formatted as HH:MM:SS"""

import datetime

current_date_time = datetime.datetime.now()
print("Current date and time: ")
print(current_date_time.strftime("%Y-%m-%d %H:%M:%S"))

##exercise 92-97.4
"""Write a Python program that converts seconds to minutes and hours.
    Present the minutes as an integer and the hours as a decimal value."""

seconds = 60
minutes = seconds//60 
hours = minutes/60
print(seconds, "seconds is equivalent to:")
print(minutes, "minutes")
print(hours, "hours")

##exercise 92-97.6
"""Write a Python program that finds the area of a circle from the value of the diameter d.
    The value of d should be provided by the user.
    The area of a circle is equal to pi*(radius)^2. The radius is the value of the diameter divided by 2.
    Round the value of the area to two decimal places.
    You may assume that the value of the diameter will be non-negative integer."""

diameter = int(input("Please enter the diameter: "))
radius = diameter/2
area = round(math.pi * (radius**2), 2)
print(f"The area of a circle with diameter {diameter} is {area}")

##exercise 92-97.9
"""Write a Python program that computes the area of a triangle from its base and height.
    The program should print the area of the triangle rounded to two decimal places (if necessary).
    The values of base and height should be entered by the user.
    The area of a triangle is found with this formula: (base*height)/2
    If either one of the values is invalid, the program should print
    "Please enter valid values for base and height"."""

base = int(input("Enter the base: "))
height = int(input("Enter the height: "))
if base > 0 and height > 0:
	area = round((base*height)/2, 2)
	print(f"The area of a triangle with base {base} and height {height} is: {area}")
else:
	print("Please enter valid values for base and height")

##exercise 92-97.11
"""Write a Python program that converts degrees Celsius to Fahrenheit and prints the result with a descriptive message.
    The user should enter the degrees Celsius as input.
    To convert degrees Celsius to Fahrenheit, we use this formula:
    <degrees_fahrenheit> = (<degrees_celsius> * 9/5) + 32
    The message should have this format: "<degrees> Celsius = <degrees> Fahrenheit"/"""

celsius = float(input("Degrees Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Degrees Fahrenheit: {fahrenheit}")

##exercise 92-97.13
"""Write a Python program that converts degrees Fahrenheit to Celsius and prints the result with a descriptive message.
    The user should enter the degrees Fahrenheit.
    To convert degrees Fahrenheit to Celsius, we use this formula:
    <degrees_celsius> = (<degrees_fahrenheit> - 32) * 5/9
    The message should have this format:
    "<degrees> Fahrenheit = <degrees> Celsius"/"""

fahrenheit = float(input("Degrees Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"Degrees Celsius: {celsius}")

# Exercises 98 - 101   Miscellaneous and More Challenging Programs (Level 2)

##exercise 98-101.1
"""Write a Python program that calculates body mass index.
    The formula to calculate body mass index is BMI = kg/m2 where kg is a person’s weight in kilograms and m2 is their height in meters squared.
    The user should be able to enter his or her height in centimeters and weight in kilograms.
    You may assume that the height and weight entered will be positive integers.
    The program must print a message with the value of the Body Mass Index (BMI) rounded to two decimals and the category:
    Underweight = less than 18.5
    Normal = from 18.5 to 24.9
    Overweight = from 25 to 29.9
    Obesity = 30 or greater"""

print("Welcome to the Body Mass Index Calculator")
height = float(input("Please enter your height (cm): "))
weight = float(input("Now enter your weight (kg): "))
height_meters = height / 100
BMI = round(weight / (height_meters**2), 2)
print(f"BMI: {BMI}")
print("Your result is:", end=" ")
if BMI < 18.5:
    print("Underweight")
elif BMI <= 24.9:
    print("Normal")
elif 25 <= BMI <= 29.9:
    print("Overweight")
else:
    print("Obesity")
	
##exercise 98-101.3
"""Write a Python program that prints the calendar of a given month in a given year.
    The user should be able to specify the month and year.
    The month must be an integer between 1 and 12.
    The year must be a valid integer.
    If the values entered by the user are not valid, a descriptive message should be displayed."""

import calendar

print("Welcome to your Python Calendar")
year = int(input("Enter the year (with this format YYYY): "))
month = int(input("Now enter the month (1-12): "))
print(calendar.month(year, month))

##exercise 98-101.6
"""Write a Python program that calculates and prints the number of days between to given dates. 
    The user should be able to enter the two dates (one per line) with this format Year Month Day.
    The year must be formatted with four digits. Example: 2021
    The month must be an integer between 1 and 12 (with no leading zeros).
    The day must be an integer between 1 and 31 (with no leading zeros).
    The first date must be previous or equal to the second date. 
    If the dates are equal (there are 0 days between them), display the message:
    "The dates are equal".
    If there is only one day between the two dates, display the message:
    "There is 1 day between these dates."
    If the first date is later than the second date, print the message:
    "Please enter valid dates"."""

from datetime import datetime

def get_date(date_input):
    while True:
        try:
            date_str = input(date_input)
            date = datetime.strptime(date_str, "%Y %m %d")
            return date
        except ValueError:
            print("Invalid input. Please enter the date in the format: Year Month Day (e.g., 2021 12 25).")

print("Enter the first date (Year Month Day):")
date1 = get_date("Enter the first date: ")
print("Enter the second date (Year Month Day):")
date2 = get_date("Enter the second date: ")
if date1 > date2:
    print("Please enter valid dates")
elif date1 == date2:
    print("The dates are equal")
else:
    date_dif = date2 - date1
    if date_dif.days == 1:
        print("There is 1 day between these dates.")
    else:
        print(f"There are {date_dif.days} days between these dates.")
		
##exercise 98-101.8
"""Write a Python program that checks if a string start with the string "My" and ends with the string "blue".
    The program should also check if the string only contains alphanumeric characters.
    For this program, you need to use a regular expression in Python. The built-in Python module re has very helpful functions to work with them, such as the search() function."""

import re

regex = "^My[\w\s]+blue$"
string = input("Enter a string to check if a match is found: ")
if re.search(regex, string):
    print("Match")  
else:  
    print("No Match")  
