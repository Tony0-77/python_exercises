from collections import Counter
import string
import math
import itertools
import random
import os.path
import datetime
import calendar
import re

print("-----------------------------------------------------------")
print("Exercises 1-8: Strings (Level 1)")
print("-----------------------------------------------------------")
#Exercise 1: Printing the Length of a String
print("Exercise 1: Printing the Length of a String")
var1 = ""
var2 = "H"
var3 = "Hello"
var4 = "Amazing"

print(f"""{var1}           : {len(var1)}
{var2}          : {len(var2)}
{var3}      : {len(var3)}
{var4}    : {len(var4)}""")

#Exercise 2: Print a Character at a specific Index
print("\nExercise 2: Print the character at a specific Index")
var = "Hello"
i = 2
if len(var) == 0:
     print(f"      {var}  :  {i}  :   Empty String")
elif i < len(var):
    print(f"{var}   :  {i} :   {var[i]}")
else:
    print(f"{var}   :  {i}  :   i out of range")
var = "Pizza"
i = 4
if len(var) == 0:
     print(f"      {var}  :  {i}  :   Empty String")
elif i < len(var):
    print(f"{var}   :  {i} :   {var[i]}")
else:
    print(f"{var}   :  {i}  :   i out of range")
var = ""
i = 3
if len(var) == 0:
     print(f"      {var}  :  {i}  :  Empty String")
elif i < len(var):
    print(f"{var}   :  {i} :   {var[i]}")
else:
    print(f"{var}   :  {i}  :   i out of range")
var = "World"
i = 15
if len(var) == 0:
     print(f"      {var}  :  {i}  :   Empty String")
elif i < len(var):
    print(f"{var}   :  {i} :   {var[i]}")
else:
    print(f"{var}   :  {i} :  i out of range")

#Exercise 1-8.3: Reverse a String
print("\nExercise 3: Reverse a String")
var = "Hello"
print(f"{var}   : {var[::-1]}")

var = "Wo"
rev_word = var[::-1]
print(f"{var}      : {rev_word}")

var = ""
rev_word = "".join(reversed(var))
print(f"{var}        : {rev_word}")

#Exercise 1-8.4: First and Last three characters of a string
print("\nExercise 4: First and Last three characters of a string")
var = "Blue"
if len(var) < 6:
    print("")
else:
    new_string = var[:3] + var[len(var)-3:]
    print(f"{var}   : {new_string}")

var = "Wonderful"
if len(var) < 6:
    print("")
else:
    new_string = var[:3] + var[len(var)-3:]
    print(f"{var} : {new_string}")
    
var = "Amazing"
if len(var) < 6:
    print("")
else:
    new_string = var[:3] + var[len(var)-3:]
    print(f"{var}   : {new_string}")
    
#Exercise 1-8.5: Remove Characters at Even Indices
print("\nExercise 5: Remove Characters at Even Indices")
var = "Coding"
new_var = ""
for i in range(len(var)):
    if i % 2 != 0:
        new_var += var[i]
print(f"{var}  :   {new_var}")

var = "Pizza"
new_var = ""
for i in range(len(var)):
    if i % 2 != 0:
        new_var += var[i]
print(f"{var}   :   {new_var}")

var = "Python"
new_var = ""
for i in range(len(var)):
    if i % 2 != 0:
        new_var += var[i]
print(f"{var}  :   {new_var}")

var = "A"
new_var = ""
for i in range(1, len(var), 2):
    new_var += var[i]
print(f"{var}       :   {new_var}")

var = ""
new_var = ""
for i in range(1, len(var), 2):
    new_var += var[i]
print(f"{var}        :   {new_var}")

#Exercise 1-8.6: Check if a String only contains numbers
print("\nExercise 6: Check if a String only contains numbers")
var = "Hello"
print(f"{var}     : {var.isdigit()}")
var = "4567"
print(f"{var}      : {var.isdigit()}")
var = "Hello59"
print(f"{var}   : {var.isdigit()}")
var = ""
print(f"{var}          : {var.isdigit()}")

#Exercise 1-8.7: Remove the nth character from a string
print("\nExercise 7: Remove the nth character from a string")
var = "Hello"
n = 1
if (len(var) == 0) or (n >= len(var)):
    print(var)
else:
    new_var = ""
    for i in range(len(var)):
        if i != n:
            new_var += var[i]
    print(f"{var}   ->  {new_var}")

var = "World"
n = 3
new_var = var[:n] + var[n+1:]
print(f"{var}   ->  {new_var}")

var = "Dog"
n = 15
if (not var) or (n >= len(var)):
    print(f"{var}     ->  {var}")
else:
    new_var = ""
    for i in range(len(var)):
        if i != n:
            new_var += var[i]
    print(new_var)

var = ""
n = 2
new_var = var[:n] + var[n+1:]
print(f"{var}        ->  {new_var}")

#Exercise 1-8.8: Replace a character in a String
print("\nExercise 8: Replace a character in a String")
var = "Hello"
new_var = var.replace("l", "s")
print(f"{var}   -> {new_var}")

var = "World"
new_var = var.replace("W", "A")
print(f"{var}   -> {new_var}")

var = "Python"
new_var = var.replace("P", "x")
print(f"{var}  -> {new_var}")

var = "Python"
new_var = var.replace("p", "a")
print(f"{var}  -> {new_var}")

print("\n-----------------------------------------------------------")
print("Exercises 9-16 Strings (Level 2)")
print("-----------------------------------------------------------")
#Exercise 9-16.1: Replace commas with dots in a strings
print("\nExercise 9: Replace commas with dots in a strings")
COMMA = ","
DOT = "."
var = "Hello, World"
print(var.replace(COMMA,DOT))

var = "3,456,344"
print(var.replace(COMMA,DOT))

#Exercise 9-16.2: Check if the String contains all the Letters in Alphabet
print("\nExercise 10: Check if the String contains all the Letters in Alphabet")
#import string      #THIS IS ALREADY IMPORTED ABOVE
var = "abcdefghijklmnopqrstuvwxyz"
set_var = set(var.lower())
print(set_var == set(string.ascii_lowercase))

#import string      #THIS IS ALREADY IMPORTED ABOVE
var = "A quick brown fox jumps over the lazy dog"
set_var = set(var.lower().replace(" ",""))
print(set_var == set(string.ascii_lowercase))

#import string      #THIS IS ALREADY IMPORTED ABOVE
var = "Hello"
set_var = set(var.lower())
print(set_var == set(string.ascii_lowercase))

#Exercise 9-16.3: Remove Spaces from the String
print("\nExercise 11: Remove Spaces from the String")
var = "Hello, World"
print(var.replace(" ",""))

var = "Have a great day"
print(var.replace(" ",""))

var = "Python"
print(var.replace(" ",""))

#Exercise 9-16.4: Check if the string starts with a given prefix
print("\nExercise 12: Check if the string starts with a given prefix")
var = "Hello"
pref = "He"
print(var.startswith(pref))

var = "Coding"
pref = "Con"
print(var.startswith(pref))

var = "Nora"
pref = "Circum"
print(var.startswith(pref))

#Exercise 9-16.5: Check if the string ends with a given suffix
print("\nExercise 13: Check if the string ends with a given suffix")
var = "Hello"
suff = "ello"
print(var.endswith(suff))

var = "Coding"
suff = "eng"
print(var.endswith(suff))

var = "Nora"
suff = "rowing"
print(var.endswith(suff))

#Exercise 9-16.6: Reverse words in a string
print("\nExercise 14: Reverse words in a string")
var = "Hello World"
new_var = " ".join(word[::-1].swapcase() for word in var.split())
print(new_var)

var = "Python Is Awesome"
new_var = " ".join(word[::-1].swapcase() for word in var.split())
print(new_var)

#Exercise 19-16.7: Count Repeated Characters
print("\nExercise 15: Count Repeated Characters")

var = "Hello"
repeated_chars = {char for char in var if var.count(char) > 1}
print(len(repeated_chars) or 0)
print(" ".join(sorted(repeated_chars)) if repeated_chars else None)

var = 'Corporation'
repeated_str = []
for i in var:
    if var.count(i) >= 2:
        repeated_str.append(i)
repeated_str = sorted(set(repeated_str))
print(len(repeated_str))
print(" ".join(repeated_str)  if repeated_str else None)

var = "Python"
repeated_chars = {char for char in var if var.count(char) > 1}
print(len(repeated_chars) or 0)
print(" ".join(sorted(repeated_chars)) if repeated_chars else None)

#Exercise 9-16.8: Sort words in Alphabetical Order
print("\nExercise 16: Sort words in Alphabetical Order")
var = "Hello World"
new_var = ""
words_list = var.split(" ")
for word in words_list:
	new_var += "".join(sorted(word.lower())) + " "
new_var.rstrip()
print(new_var)

var = "Wonderful World"
new_var = " ".join("".join(sorted(word.lower())) for word in var.split())
print(new_var)

#Exercise 17-24: Lists and Tuples (Level 1)
print("\n-----------------------------------------------------------")
print("Exercise 17-24: Lists and Tuples (Level 1)")
print("-----------------------------------------------------------")

#Execise 17: Multiply all elements in a list
print("Execise 17: Multiply all elements in a list")
my_list = [3, 4, 5, 6]
factor = 2
for i in range(len(my_list)):
	my_list[i] *= factor
print(my_list)

my_list = ["a", "b", "c"]
factor = 3
my_list = [elem * factor for elem in my_list]
print(my_list)

#Exercise 18: Print the elements of a List
print("\nExercise 18: Print the elements of a List")
my_list = [3, 4, 5, 6]
for elem in my_list:
	print(elem, end=" ")
 
my_list = ["a", "b", "c"]
print(*my_list, sep=" ") #or print(" ".join(my_list)) -> if it's a lists of strings

#Exercise 19: Get Max and Min Values
print("\nExercise 19: Get Max and Min Values")
my_list = [3, 4, 5, 6]
if my_list:
	print(max(my_list), min(my_list))
else:
	print(None)
 
my_list = [-1, -2, -3, -4]
print((max(my_list), min(my_list)) if my_list else None)

my_list = [0, 0, 0, 0]
print((max(my_list), min(my_list)) if my_list else None)

my_list = []
print((max(my_list), min(my_list)) if my_list else "[]")

#Exercise 20: Check if List is empty or not empty
print("\nExercise 20: Check if List is empty or not empty")
my_list = []
print("Not Empty" if my_list else "Empty")

my_list = [4]
print("Not Empty" if my_list else "Empty")

my_list = [4, 5, 6, 7]
print("Not Empty" if my_list else "Empty")

#Exercise 21: Print List's elements and its Indices
print("\nExercise 21: Print List's elements and its Indices")
my_list = [1, 2, 3, 4]
if len(my_list) == 0:
	print("Empty List")
else:
	for i in range(len(my_list)):
		print(my_list[i], i)
    
my_list = ["a", "b", "c"]
if len(my_list) == 0:
	print("Empty List")
else:
	for i in range(len(my_list)):
		print(my_list[i], i)
  
my_list = []
if len(my_list) == 0:
	print("Empty List")
else:
	for i in range(len(my_list)):
		print(my_list[i], i)

#Exercise 22: Remove Matching Elements
print("\nExercise 22: Remove Matching Elements")
my_list = [1, 2, 3, 4]
elem_to_remove = 2
if not my_list:
	print("Empty List")
elif my_list.count(elem_to_remove) == 0:
	print("Not Found")
else:
	for i in range(my_list.count(elem_to_remove)):
		my_list.remove(elem_to_remove)
print("" if not my_list else my_list)

my_list = [3, 3, 2, 1]
elem_to_remove = 3
if not my_list:
	print("Empty List")
elif my_list.count(elem_to_remove) == 0:
	print("Not Found")
else:
	for i in range(my_list.count(elem_to_remove)):
		my_list.remove(elem_to_remove)
print("" if not my_list else my_list)

my_list = ["a", "b", "c", "b"]
elem_to_remove = "b"
if not my_list:
	print("Empty List")
elif my_list.count(elem_to_remove) == 0:
	print("Not Found")
else:
	for i in range(my_list.count(elem_to_remove)):
		my_list.remove(elem_to_remove)
print("" if not my_list else my_list)

my_list = [3, 4, 5, 6]
elem_to_remove = 7
if not my_list:
	print("Empty List")
elif my_list.count(elem_to_remove) == 0:
    print("Not Found")
else:
	for i in range(my_list.count(elem_to_remove)):
		my_list.remove(elem_to_remove)
print("" if my_list.count(elem_to_remove) == 0 else my_list)

my_list = []
elem_to_remove = 0
if not my_list:
	print("Empty List")
elif my_list.count(elem_to_remove) == 0:
	print("Not Found")
else:
	for i in range(my_list.count(elem_to_remove)):
		my_list.remove(elem_to_remove)
print("" if not my_list else my_list)

#Exercise 23: Remove Duplicates
print("\nExercise 23: Remove Duplicates")
my_list = [1, 1, 2, 3, 4, 4]
new_list = list(set(my_list))
print(new_list)

my_list = ["a", "b", "a", "a"]
new_list = list(set(my_list))
print(new_list)

my_list = [1, 2, 3]
new_list = list(set(my_list))
print(new_list)

my_list = []
new_list = list(set(my_list))
print(new_list)

#Exercise 24: Count Elements Greater than 3
print("\nExercise 24: Count Elements Greater than 3")
my_list = [1, -1, 0, 2, 2, 3]
count = sum(1 for elem in my_list if elem > 3)
print(count)

my_list = [1, 2, 3, 4]
count = sum(1 for elem in my_list if elem > 3)
print(count)

my_list = [7, 8, 9, 10]
count = sum(1 for elem in my_list if elem > 3)
print(count)

my_list = []
count = sum(1 for elem in my_list if elem > 3)
print(count)

print("\n-----------------------------------------------------------")
print("Exercises 25-32 Lists and Tuples (Level 2)")
print("-----------------------------------------------------------")

#Exercise 25: Difference Between Two Lists
print("\nExercise 25: Difference Between Two Lists")
list_A = [1, 2, 3, 4]
list_B = [1, 2]
difference = [elem for elem in list_A if elem not in list_B]
print(difference)

list_A = [1, 2, 3, 4]
list_B = [1, 2, 3]
difference = [elem for elem in list_A if elem not in list_B]
print(difference)

list_A = [1, 2, 3, 4]
list_B = [1, 2, 3, 4]
difference = [elem for elem in list_A if elem not in list_B]
print(difference)

list_A = []
list_B = [1, 3]
difference = [elem for elem in list_A if elem not in list_B]
print(difference)

#Exercise 26: Distance Between Two 3D Points
print("\n Exercise 26: Distance Between Two 3D Points")
#import math        #THIS IS ALREADY IMPORTED ABOVE
pointA = [1, 2, 3]
pointB = [1, 2, 3]
distance = math.sqrt(sum((pointA[i] - pointB[i]) ** 2 for i in range(len(pointA))))
print(distance)

pointA = [3, 4, 5]
pointB = [1, 3, 5]
distance = math.sqrt(sum((pointA[i] - pointB[i]) ** 2 for i in range(len(pointA))))
print(distance)

pointA = [-3, 4, -5]
pointB = [2, 0, -4]

distance = ((pointA[0] - pointB[0])**2
			+ (pointA[1] - pointB[1])**2
			+ (pointA[2] - pointB[2])**2)**(1/2)
print(distance)

#Exercise 27: Print common Elements in Two Lists
print("\nExercise 27: Print common Elements in Two Lists")
list_A = [1, 2, 3]
list_B = [1, 2, 3]
common = [elem for elem in list_A if elem in list_B]
print(common)

list_A = [4, 5, 6]
list_B = [1, 4, 5]
common = [elem for elem in list_A if elem in list_B]
print(common)

list_A = [3, 4, 5]
list_B = [1, 2, 3]
common = [elem for elem in list_A if elem in list_B]
print(common)

list_A = [4, 5, 6]
list_B = [1, 2, 3]
common = [elem for elem in list_A if elem in list_B]
print(common)

#Exercise 28: Find the second Largest value in a List
print("\nExercise 28: Find the Second Largest Value in a List")
my_list = [1, 2, 3, 4]
print(sorted(my_list)[-2] if len(my_list) > 1 else "None")

my_list = [1, 2]
print(sorted(my_list)[-2] if len(my_list) > 1 else "None")

my_list = [1]
print(sorted(my_list)[-2] if len(my_list) > 1 else "None")

my_list = []
print(sorted(my_list)[-2] if len(my_list) > 1 else "None")

#Exercise 29: Find the Second Smallest Value in a List
print("\nExercise 29: Find the Second Smallest Value in a List")
my_list = [1, 2, 3, 4]
print(sorted(my_list)[1] if len(my_list) > 1 else "None")

my_list = [1, 3]
print(sorted(my_list)[1] if len(my_list) > 1 else "None")

my_list = [1]
print(sorted(my_list)[1] if len(my_list) > 1 else "None")

my_list = []
print(sorted(my_list)[1] if len(my_list) > 1 else "None")

#Exercise 30: Make a Frequency dictionary From a List
print("\nExercise 30: Make a Frequency dictionary From a List")
my_list = ["a", "a", "b", "c", "a", "b"]
freq_dict = {}
for elem in my_list:
	if elem not in freq_dict:
		freq_dict[elem] = 1
	else:
		freq_dict[elem] += 1
print(freq_dict)

#from collections import Counter    #THIS IS ALREADY IMPORTED ABOVE
my_list = [1, 2, 3, 4, 3, 2, 1, 2]
freq_dict = Counter(my_list)
print(dict(freq_dict))

#Exercise 31: Flatten a List that contains List
print("\nExercise 31: Flatten a List that contains List")
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [item for sublist in my_list for item in sublist]
print(flat_list)

my_list = [1, 2, 3, 4, 5, 6, [7, 8, 9]]
flat_list = []
for elem in my_list:
	if isinstance(elem, list):
		for nested_elem in elem:
			flat_list.append(nested_elem)
	else:
		flat_list.append(elem)
print(flat_list)

my_list = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
flat_list = [nested_elem for elem in my_list for nested_elem in (elem if isinstance(elem, list) else [elem])]
print(flat_list)

"""
import itertools    #THIS IS ALREADY IMPORTED ABOVE
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = list(itertools.chain(*my_list))
print(flat_list)
"""

#Exercise 32: Generate Permutation of a List
print("\nExercise 32: Generate Permutation of a List")
#import itertools       #THIS IS ALREADY IMPORTED ABOVE
my_list = [1, 2, 3]
permutations = list(itertools.permutations(my_list))
for permutation in permutations:
	print(permutation)

print("\n-----------------------------------------------------------")
print("Exercises 33-38 Dictionaries (Level 1)")
print("-----------------------------------------------------------")

#Exercise 33: Check if a key exists in a dictionary
print("\nExercise 33: Check if a key exists in a dictionary")
my_dict = {"a": 4, "b": 6}
key = "a"
print(key in my_dict)

my_dict = {"a": 4, "b": 6}
key = "c"
print(key in my_dict)

my_dict = {}
key = "d"
print(key in my_dict)

#Exercise 34: Add a ke-value pair only if the key is not in the dictionary
print("\nExercise 34: Add a ke-value pair only if the key is not in the dictionary")
my_dict = {"January": 45, "February": 56, "March": 67}
new_key = "April"
value = 67
if new_key not in my_dict:
    my_dict[new_key] = value
print(my_dict)

my_dict = {"January": 45, "February": 56, "March": 67}
new_key = "January"
value = 67
if new_key not in my_dict:
    my_dict[new_key] = value
print(my_dict)

#Exercise 35: Merge two dictionaries
print("\nExercise 35: Merge two dictionaries")
my_dict1 = {"a": 1, "b": 2, "c": 3}
my_dict2 = {"c": 4, "d": 6, "e": 8}
final_dict = my_dict1 | my_dict2
print(final_dict)

#Exercise 36: Check if all values are equal
print("\nExercise 36: Check if all values are equal")
my_dict = {"a" : 4, "b" : 4, "c" : 4}
checker = (len(set(my_dict.values())))
if checker == 0:
    print("Empty")
elif checker == 1:
    print(True)
else:
    print(False)
    
my_dict = {"a" : 4, "b" : 6, "c" : 4}
checker = (len(set(my_dict.values())))
if checker == 0:
    print("Empty")
elif checker == 1:
    print(True)
else:
    print(False)
    
my_dict = {"a" : 4, "b" : 6, "c" : 10}
checker = (len(set(my_dict.values())))
if checker == 0:
    print("Empty")
elif checker == 1:
    print(True)
else:
    print(False)

my_dict = {}
checker = (len(set(my_dict.values())))
if checker == 0:
    print("Empty")
elif checker == 1:
    print(True)
else:
    print(False)
    
#Exercise 37: Find the maximum Value in a dictionary
print("\nExercise 37: Find the maximum Value in a dictionary")
my_dict = {"a" : 4, "b" : 3, "c" : 7}
print(max(set(my_dict.values())) if my_dict else None)

my_dict = {"a" : 4, "b" : 6}
print(max(set(my_dict.values())) if my_dict else None)

my_dict = {"a" : 4, "b" : 4}
print(max(set(my_dict.values())) if my_dict else None)

my_dict = {}
print(max(set(my_dict.values())) if my_dict else None)

#Exercise 38: Find the minimum Value in a dictionary
print("\nExercise 38: Find the minimum Value in a dictionary")
my_dict = {"a" : 4, "b" : 3, "c" : 7}
print(min(set(my_dict.values())) if my_dict else None)

my_dict = {"a" : 4, "b" : 6}
print(min(set(my_dict.values())) if my_dict else None)

my_dict = {"a" : 4, "b" : 4}
print(min(set(my_dict.values())) if my_dict else None)

my_dict = {}
print(min(set(my_dict.values())) if my_dict else None)

print("\n-----------------------------------------------------------")
print("Exercises 39-44 Dictionaries (Level 2)")
print("-----------------------------------------------------------")

#Exercise 39: Find the Frequency of the Values in a Dictionary
print("\nExercise 39: Find the Frequency of the Values in a Dictionary")
#from collections import Counter    #THIS IS ALREADY IMPORTED ABOVE
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
freq_dict = Counter(my_dict.values())
print(dict(freq_dict) if my_dict else {})

#Exercise 40: Make a Dictionary from Nested Lists
print("\nExercise 40: Make a Dictionary from Nested Lists")
my_list = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]
my_dict = {}
for sublist in my_list:
    keys = sublist[0]
    values = sublist[1]
    my_dict[keys] = values
print(my_dict)

#Exercie 41: Print Max Sum of Values
print("\nExercie 41: Print Max Sum of Values")
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

#Exercise 42: make Frequency Dictionary for Characters in a String
print("\nExercise 42: make Frequency Dictionary for Characters in a String")
my_string = "Hello, World"
freq_dict = {}
for char in my_string.lower():
	if char.isalpha():
		if char in freq_dict:
			freq_dict[char] += 1
		else:
			freq_dict[char] = 1
print(freq_dict)

my_string = "Excellent"
freq_dict = {}
for char in my_string.lower():
	if char.isalpha():
		if char in freq_dict:
			freq_dict[char] += 1
		else:
			freq_dict[char] = 1
print(freq_dict)

#Exercise 43: Sort Lists in Ascending Order
print("\nExercise 43: Sort Lists in Ascending Order")
my_dict = {
	"a": [4, 3, 2],
	"b": [5, 3, 7],
	"c": [1, 9, 10],
	"d": [3, 4, 1]
}
for list_value in my_dict.values():
	list_value.sort()
print(my_dict)

#Exercise 44: Convert Dictionary into a List
print("\nExercise 44: Convert Dictionary into a List")
product_info = {
	"description": "shoe",
	"price": 4.56,
	"colors": ["green", "blue", "red"],
}
new_list = []
for key, value in product_info.items():
	new_list.append([key, value])
print(new_list)

print("\n-----------------------------------------------------------")
print("Exercises 45-50 Programs with Conditionals (Level 1)")
print("-----------------------------------------------------------")
#Exercise 45: Zero, Positive, or Negative
print("\nExercise 45: Zero, Positive, or Negative")
num = 3
if num == 0:
	print("Zero")
elif num > 0:
	print("Positive")
else:
	print("Negative")
 
num = -1
if num == 0:
	print("Zero")
elif num > 0:
	print("Positive")
else:
	print("Negative")

num = 0
if num == 0:
	print("Zero")
elif num > 0:
	print("Positive")
else:
	print("Negative")

#Exercise 46: Check Vowels and Consonant
print("\nExercise 46: Check Vowels and Consonant")
text = "Score: 36"
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

#Exercise 47: Print Max of 3 Numbers
print("\nExercise 47: Print Max of 3 Numbers")
a = 1
b = 3
c = 4
print(max(a, b, c))

a = 1
b = 4
c = 15
print(max(a, b, c))

a = 3
b = 3
c = 3
print(max(a, b, c))

#Exercise 48: Print Min of 3 Numbers
print("\nExercise 48: Print Min of 3 Numbers")
a = 1
b = 2
c = 3
print(min(a, b, c))

a = 2
b = 2
c = 2
print(min(a, b, c))

a = -1
b = -3
c = -4
print(min(a, b, c))

#Exercise 49: Print Seasons
print("\nExercise 49: Print Seasons")
season_num = 2

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
 
#Exercise 50: Compare Three Numbers
print("\nExercise 50: Compare Three Numbers")
a = 3
b = 3
c = 3
if a == b == c:
	print("Equal")
else:
	print("Not Equal")
 
a = 3
b = 4
c = 3
if a == b == c:
	print("Equal")
else:
	print("Not Equal")
 
print("\n-----------------------------------------------------------")
print("Exercises 51-56 Programs with Conditionals (Level 2)")
print("-----------------------------------------------------------")
#Exercise 51: Find Number of Days in a Month
print("\nExercise 51: Find Number of Days in a Month")
month = "January"
months_with_31_days = ("January", "March", "May", "July", "August", "October", "December")
months_with_30_days = ("April", "June", "September", "November")
if month in months_with_31_days:
	print(f"{month} has 31 days")
elif month in months_with_30_days:
	print(f"{month} has 30 days")
else:
	print(f"{month} has 28 days")

#Exercise 52: Increasing or Decreasing Order
print("\nExercise 52: Increasing or Decreasing Order")
a = 1
b = 2
c = 3
if a > b > c:
	print("Decreasing Order")
elif a < b < c:
	print("Increasing Order")
else:
	print("None")
 
a = 3
b = 2
c = 1
if a > b > c:
	print("Decreasing Order")
elif a < b < c:
	print("Increasing Order")
else:
	print("None")
 
a = 1
b = 1
c = 1
if a > b > c:
	print("Decreasing Order")
elif a < b < c:
	print("Increasing Order")
else:
	print("None")
 
a = 1
b = 2
c = 1
if a > b > c:
	print("Decreasing Order")
elif a < b < c:
	print("Increasing Order")
else:
	print("None")

#Exercise 53: Solve Quadratic Equation
print("\nExercise 53: Solve Quadratic Equation")
#import math
a = 1
b = 2 
c = 1
disc = b**2 - 4*a*c
if disc < 0:
	print("Complex Roots")
elif disc == 0:
	x = (-b + math.sqrt(disc))/(2*a)
	print(f"x = {x}")
else:
	x1 = (-b - math.sqrt(disc))/(2*a)
	x2 = (-b + math.sqrt(disc))/(2*a)
	print(f"x = {x1}, x = {x2}")

a = 2
b = 5 
c = -3
disc = b**2 - 4*a*c
if disc < 0:
	print("Complex Roots")
elif disc == 0:
	x = (-b + math.sqrt(disc))/(2*a)
	print(f"x = {x}")
else:
	x1 = (-b - math.sqrt(disc))/(2*a)
	x2 = (-b + math.sqrt(disc))/(2*a)
	print(f"x = {x1}, x = {x2}")
 
a = 3
b = 4 
c = 5
disc = b**2 - 4*a*c
if disc < 0:
	print("Complex Roots")
elif disc == 0:
	x = (-b + math.sqrt(disc))/(2*a)
	print(f"x = {x}")
else:
	x1 = (-b - math.sqrt(disc))/(2*a)
	x2 = (-b + math.sqrt(disc))/(2*a)
	print(f"x = {x1}, x = {x2}")
 
#Exercise 54: Check if Year is Leap Year
print("\nExercise 54: Check if Year is Leap Year")
year = 2025
if year % 400 == 0 or year % 4 == 0:
	print(f"{year} is a leap year")
elif year % 100 == 0:
	print(f"{year} is not a leap year")
else:
	print(f"{year} is not a leap year")
 
year = 2033
if year % 400 == 0 or year % 4 == 0:
	print(f"{year} is a leap year")
elif year % 100 == 0:
	print(f"{year} is not a leap year")
else:
	print(f"{year} is not a leap year")
 
year = 1836
if year % 400 == 0 or year % 4 == 0:
	print(f"{year} is a leap year")
elif year % 100 == 0:
	print(f"{year} is not a leap year")
else:
	print(f"{year} is not a leap year")

year = 1912
if year % 400 == 0 or year % 4 == 0:
	print(f"{year} is a leap year")
elif year % 100 == 0:
	print(f"{year} is not a leap year")
else:
	print(f"{year} is not a leap year")

#Exercise 55: Interactive Calculator
print("\nExercise 55: Interactive Calculator")
ADDITION = 1
SUBTRACTION = 2
MULTIPLICATION = 3
DIVISION = 4
INTEGER_DIVISION = 5
MODULO = 6
print("Welcome to Python Interactive Calculator! ")
a = int(input("\nPlease enter the first value: "))
b = int(input("Please enter the second value: "))

print(f"""\nGreat! These are the available options:
      1 - ADDITION
      2 - SUBTRACTION
      3 - MULTIPLICATION
      4 - DIVISION
      5 - INTEGER DIVISION
      6 - MODULO""")

operation = int(input("Now Please Select the Operation You want to use: "))

if operation == ADDITION:
	print(f"The result of {a} + {b} is {a+b}")
elif operation == SUBTRACTION:
	print(f"The result of {a} - {b} is {a-b}")
elif operation == MULTIPLICATION:
	print(f"The result of {a} * {b} is {a*b}")
elif operation == DIVISION:
	if b == 0:
		print("Division by Zero. Please enter another value for b.")
	else:
		print(f"The result of {a} / {b} is {a/b}")
elif operation == INTEGER_DIVISION:
	if b == 0:
		print("Division by Zero. Please enter another value for b.")
	else:
		print(f"The result of {a} // {b} is {a//b}")
elif operation == MODULO:
	print(f"The result of {a} % {b} is {a%b}")
else:
	print("Please select the corresponding integer of the operation you wanted to use.")
 
#Exercise 56: Rock, Paper, Scissor
print("\nExercise 56: Rock, Paper, Scissor")
#import random      #IMPORTED ABOVE
print("Welcome to Rock, Paper, Scissors!")
player = input("Enter your choice (rock, paper, or scissors): ").lower()
if player not in ["rock", "paper", "scissors"]:
    print("Invalid choice! Please choose rock, paper, or scissors.")
else:
    computer = random.choice(["rock", "paper", "scissors"])
    if player == computer:
        print("It's a tie! Try Again.")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print(f"You win! Your opponent chose {computer}.")
    else:
        print(f"You lose! Your opponent chose {computer}.")

print("\n-----------------------------------------------------------")
print("Exercises 57-63 For Loops and While Loops (Level 1)")
print("-----------------------------------------------------------")
#Exercise 57: Print the firs 15 positive Integers
print("\nExercise 57: Print the firs 15 positive Integers")
for i in range(1, 16):
	print(i)

#Exercise 58: Print Integers in Reverse Order
print("\nExercise 58: Print Integers in Reverse Order")
n = int(input("Enter an Integer: "))
for i in reversed(range(1, n+1)):
	print(i)
 
#Exercise 59: Sum of first 100 Posiitive Integers
print("\nExercise 59: Sum of first Positive 100 Integers")
sum = 0
for i in range(1, 101):
	sum += i
print(sum)

#Exercise 60: Print The Multiplication Table
print("\nExercise 60: Print The Multiplication Table")
n = int(input("Enter an Integer: "))
print(f"Multiplication Table of {n}")
for i in range(1, 11):
	print(f"{n} x {i} = {n*i}")
 
#Exercise 61: Print The Alphabet using a Loop
print("\nExercise 61: Print The Alphabet using a Loop")
for i in range(65, 91):
	print(chr(i))
 
#Exercise 62: First 100 even Numbers
print("\nExercise 62: First 100 even Numbers")
for i in range(2, 201, 2):
    print(i)

#Exercise 63: Calculate Factorial
print("\nExercise 63: Calculate Factorial")
n = int(input("Enter an Integer: "))
factorial = 1
for i in range(2, n+1):
	factorial *= i
print(factorial)

print("\n-----------------------------------------------------------")
print("Exercises 64-71 For Loops and While Loops (Level 2)")
print("-----------------------------------------------------------")
#Exercise 64: Check if a Number is Prime
print("\nExercise 64: Check if a Number is Prime")
num = int(input("Enter an Integer: "))
if num == 0 or num == 1:
	print("Not Prime")
else:
	for i in range(2, num):
		if num % i == 0:
			print("Not Prime")
			break
	else:
		print("Prime")
  
#Exercise 65: Print Pattern using Loop
print("\nExercise 65: Print Pattern using Loop")
n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
	print("*" * i)

#Exercise 66: Print Digits in Reverse Order
print("\nExercise 66: Print Digits in Reverse Order")
num = 2662 #1 #123 #1111 #3456
reverse = int(str(num)[::-1])
print(reverse)

#Exercise 67: Reverse a String using a Loops
print("\nExercise 67: Reverse a String using a Loops")
s = "Hello" #World #Python
for char in reversed(s):
	print(char, end="")
 
#Exercise 68: print Half Pyramid using a Loop
print("\nExercise 68: print Half Pyramid using a Loop")
n = int(input("Enter the number of rows: "))
k = (2 * n) - 2
for i in range(n):
    for j in range(k):
        print("", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print("")
    k = k - 2

#Exercise 69: Floyd's Triangle
print("\nExercise 69: Floyd's Triangle")
n = int(input("Enter the number of rows: "))
count = 1
for i in range(1, n+1):
    for j in range(i):
        print(count, end=" ")
        count += 1
    print()
    
#Exercise 70: Triangular Letters Pattern
print("\nExercise 70: Triangular Letters Pattern")
n = int(input("Enter the number of rows: "))
for i in range(n):
	print(chr(65 + i) * (i + 1))
 
#Exercise 71: Diamond Made with Asterisks
print("\nExercise 71: Diamond Made with Asterisks")
height = int(input("Enter an odd number for diamond's height : "))
if height % 2 == 0:
    print("The Value must be an odd number.")
else:
    middle_rows = (height + 2) // 2
    for i in range(middle_rows):
        print(" " * (middle_rows - i), "*" * (i*2 + 1))
    for i in range(middle_rows-2, -1, -1):
        print(" " * (middle_rows - i), "*" * (i*2 + 1))

print("\n-----------------------------------------------------------")
print("Exercises 72-76 Recursion (Level 1)")
print("-----------------------------------------------------------")
#Exercise 72: Find the sum of a Lists using Recursion
print("\nExercise 72: Find the sum of a Lists using Recursion")
#my_list = [4, 5, 6]
#my_list = [-1, 2, 0]
#my_list = [0, 0, 0]
#my_list = []
my_list = [1, 2, 3] 
i = 0
sum = 0
while i < len(my_list):
    sum += my_list[i]
    i += 1
print(sum)

#Exercise 73: Find the nth Fibonacci Number
print("\nExercise 73: Find the nth Fibonacci Number")
n = int(input("Please Enter an Integer: "))
if n <= 1:
    result = n
else:
    def fib(x):
        if x <= 1:
            return x
        return fib(x - 1) + fib(x - 2)
    result = fib(n)
print(f"The {n}th Fibonacci number is:", result)

#Exercise 74: Recursive Factorial
print("\nExercise 74: Recursive Factorial")
n = int(input("Please Enter an Integer: "))
factorial = 1
current = n
while current > 0:
    factorial *= current
    current -= 1
print(f"{n}! = {factorial}")

#Exercise 75: Find the sum of the digits of a Positive Integers
print("\nExercise 75: Find the sum of the digits of a Positive Integers")
num = int(input("Please Enter an Integer: "))
digit_sum = 0
while num > 0:
    digit_sum += num % 10
    num //= 10
print("Sum of digits:", digit_sum)

#Exercise 76: Solve a Power Recursively
print("\nExercise 76: Solve a Power Recursively")
base = int(input("Please Enter the Base: "))
exp = int(input("Please Enter the Exponent: "))
result = 1
count = 0
while count < exp:
    result *= base
    count += 1
print(f"{base} raised to {exp} =", result)

print("\n-----------------------------------------------------------")
print("Exercises 77-82 Recursion (Level 2)")
print("-----------------------------------------------------------")
#Exercise 77: Find the Greatest Common Divisor
print("\nExercise 77: Find the Greatest Common Divisor")
def find_gcd(a, b):
	if b == 0:
		return a
	else:
		return find_gcd(b, a % b)
"""a = 42
b = 56
a = 7
b = 3
a = 6
b = 2
"""

a = 60
b = 48
print(find_gcd(a,b))

#Exercise 78: Check if String is a Palindrome
print("\nExercise 78: Check if String is a Palindrome")
def is_palindrome(string):
	string = string.lower()
	if len(string) <= 1:
		return True
	elif string[0] != string[-1]:
		return False
	else:
		return is_palindrome(string[1:-1])

s = input("Enter a String: ")
if is_palindrome(s):
    print(f'"{s}" is a palindrome.')
else:
    print(f'"{s}" is not a palindrome.')
    
#Exercise 79: Count Vowels Recursively
print("\nExercise 79: Count Vowels Recursively")
def count_vowels(string):
	string = string.lower()
	if not string:
		return 0
	elif string[0] in ("a", "e", "i", "o", "u"):
		return 1 + count_vowels(string[1:])
	else:
		return count_vowels(string[1:])

s = input("Enter a String: ")
print(count_vowels(s))

#Exercise 80: Print a Pattern Using Recursion
print("\nExercise 80: Print a Pattern Using Recursion")
def print_pattern(n, current=1):
    if current > n:
        return
    else:
        print("*" * current)
        print_pattern(n, current + 1)

s = int(input("Enter Number of rows: "))
print_pattern(s)

#Exercise 81: Convert from Decimal to Binary
print("\nExercise 81: Convert from Decimal to Binary")
def convert_to_binary(decimal_num):
    if decimal_num == 0:
        return '0'
    else:
        return (convert_to_binary(decimal_num // 2) + str(decimal_num % 2)).lstrip("0")

n = int(input("Enter an Integer you want to convert into Binary:  "))
print(convert_to_binary(n))

#Exercise 82: Implement Binary Search Recursively
print("\nExercise 82: Implement Binary Search Recursively")
def binary_search(seq, low, high, elem):
	if low > high:
		return -1
	else:
		middle = (low + high)//2

		if elem == seq[middle]:
			return middle
		elif elem < seq[middle]:
			return binary_search(seq, low, middle-1, elem)
		else:
			return binary_search(seq, middle+1, high, elem)

seq = [1, 2, 3]
target = 2
result = binary_search(seq, 0, len(seq)-1, target)
print(result)

print("\n-----------------------------------------------------------")
print("Exercises 83-87 Working with Files (Level 1)")
print("-----------------------------------------------------------")
#Exercise 83: Read a Text File
print("\nExercise 83: Read a Text File")

file_path = "File.txt"
file_content = []
with open(file_path) as file:
	for line in file:
		file_content.append(line)

print(file_content)

#Exercise 84: Print the First n Lines of a File
print("\nExercise 84: Print the First n Lines of a File")
file_path = "File.txt"
n = int(input("How many lines would you like to read?: "))
with open(file_path) as file:
	lines = file.readlines()
	num_lines = len(lines)

	if num_lines < n:
		print(f"Please enter a valid value. The file has {num_lines} lines.")
	else:
		for i in range(n):
			print(lines[i].strip("\n"))

#Exercise 85: Print the Last n Lines of a File
print("\nExercise 85: Print the Last n Lines of a File")
file_path = "File.txt"
n = int(input("How many lines would you like to read?: "))
with open(file_path) as file:
	lines = file.readlines()
	num_lines = len(lines)

	if num_lines < n:
		print(f"Please enter a valid value. The file has {num_lines} lines.")
	else:
		for i in range(-n, 0):
			print(lines[i].strip("\n"))	

#Exercise 86: find the Longest Word in a File
print("\nExercise 86: find the Longest Word in a File")
file_path = "File.txt"
longest_word = ""

with open(file_path) as file:
	for word in file:
		if len(word) > len(longest_word):
			longest_word = word

print(longest_word)

#Exercise 87: Make a Frequency Dictionary of the Words in a File
print("\nExercise 87: Make a Frequency Dictionary of the Words in a File")
file_path = "File.txt"
freq_dict = {}

with open(file_path) as file:
	for word in file:
		word = word.strip("\n")
		if word not in freq_dict:
			freq_dict[word] = 1
		else:
			freq_dict[word] += 1

print(freq_dict)

print("\n-----------------------------------------------------------")
print("Exercises 88-91 Working with Files (Level 2)")
print("-----------------------------------------------------------")
#Exercise 88: Write a List to a File
print("\nExercise 88: Write a List to a File")
file_path = "list.txt"
my_list = [1, 2, 3, 4, 5]

with open(file_path, "w") as file:
	for elem in my_list:
		file.write(str(elem))
  
#Exercise 89: Count Characters in a File
print("\nExercise 89: Count Characters in a File")
file_path = "File.txt"
character_count = 0
with open(file_path) as file:
	for line in file:
		character_count += len(line.replace(" ", "").strip("\n"))
print(character_count)

#Exercise 90: Copy the Content of a File to Another File
print("\nExercise 90: Copy the Content of a File to Another File")
file_path = "File.txt"
copy_path = "list.txt"
with open(file_path) as file, open(copy_path, "w") as copy:
	for line in file:
		copy.write(line)
  
#Exercise 91: Check if a File Exists
print("\nExercise 91: Check if a File Exists")
#import os.path     #IMPORTED ABOVE
my_file = "list.txt"
if os.path.isfile(my_file):
    print(f"The file {my_file} exists")
else:
    print(f"The file {my_file} doesn't exist")
    
print("\n-----------------------------------------------------------")
print("Miscellaneous and More Challenging Programs (Level 1)")
print("-----------------------------------------------------------")
#Exercise 92: Display Current Date and Time
print("\nExercise 92: Display Current Date and Time")
#import datetime        #IMPORTED ABOVE
current_date_time = datetime.datetime.now()
print("Current date and time: ")
print(current_date_time.strftime("%Y-%m-%d %H:%M:%S"))

#Exercise 93: Convert Seconds to Minutes and Hours
print("\nExercise 93: Convert Seconds to Minutes and Hours")
seconds = int(input("Enter the nubers of seconds(time): "))
minutes = seconds//60 
hours = minutes/60

print(seconds, "seconds is equivalent to:")
print(minutes, "minutes")
print(hours, "hours")

#Exercise 94: Calculate the Area of a Circle
print("\nExercise 94: Calculate the Area of a Circle")
diameter = int(input("Please enter the diameter: "))
radius = diameter/2
area = round(math.pi * (radius**2), 2)
print(f"The area of a circle with diameter {diameter} is {area}")

#Exercise 95: Compute the Area of a Triangle
print("\nExercise 95: Compute the Area of a Triangle")
base = int(input("Enter the base: "))
height = int(input("Enter the height: "))

if base > 0 and height > 0:
	area = round((base*height)/2, 2)
	print(f"The area of a triangle with base {base} and height {height} is: {area}")
else:
	print("Please enter valid values for base and height")
 
#Exercise 96: Celsius to Fahrenheit Conversion
print("\nExercise 96: Celsius to Fahrenheit Conversion")
celsius = float(input("Degrees Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} Degrees Celsius = {fahrenheit} Degrees Fahrenheit")

#Exercise 97: Fahrenheit to Celsius Conversion
print("\nExercise 97: Fahrenheit to Celsius Conversion")
fahrenheit = float(input("Degrees Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit} Degrees Fahrenheit = {celsius} Degrees Celsius")

print("\n-----------------------------------------------------------")
print("Miscellaneous and More Challenging Programs (Level 2)")
print("-----------------------------------------------------------")
#Exercise 98: Calculate Body Mass Index
print("\nExercise 98: Calculate Body Mass Index")
print("Welcome to the Body Mass Index Calculator")

height = float(input("Please Enter your height (cm): "))
weight = float(input("Please Enter your weight (kg): "))

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

#Exercise 99: Print a Calendar
print("\nExercise 99: Print a Calendar")
#import calendar        #ALREADY IMPORTED ABOVE
print("Welcome to your Python Calendar")
year = int(input("Enter the year (with this format YYYY): "))
month = int(input("Now enter the month (1-12): "))

print(calendar.month(year, month))

#Exercise 100: Find the Number of Days Between Two Dates
print("\nExercise 100: Find the Number of Days Between Two Dates")
#import datetime
print("For Date format, Please use YYYY<space>MM<space>DD (ex: 2025 2 10)")
date1_input = input("Enter the first date: ")
date2_input = input("Enter the second date: ")

date1_list = date1_input.split(" ")
year1 = int(date1_list[0])
month1 = int(date1_list[1])
day1 = int(date1_list[2])

date1_obj = datetime.date(year1, month1, day1)

date2_list = date2_input.split(" ")
year2 = int(date2_list[0])
month2 = int(date2_list[1])
day2 = int(date2_list[2])

date2_obj = datetime.date(year2, month2, day2)

if date2_obj < date1_obj:
    print("Please enter valid dates.")
else:
    difference = (date2_obj - date1_obj).days

    if difference == 0:
        print("These dates are equal.")
    elif difference == 1:
    	print(f"There is 1 day between these dates.")
    else:
        print(f"There are {difference} days between these dates.")

#Exercise 101: Check a Pattern using a Regular Expression
print("\nExercise 101: Check a Pattern using a Regular Expression")
#import re      #IMPORTED ABOVE
def check_string(s):
    pattern = r"^My[\w\s]+blue$"

    if re.search(pattern, s):
        return "Match"
    else:
        return "No Match"

print(check_string("My favorite color is blue"))
print(check_string("My shoes are blue"))
print(check_string("My favorite color is red"))
print(check_string("My friend's username is @blue"))
print(check_string("Hello, I'm 102 years old"))