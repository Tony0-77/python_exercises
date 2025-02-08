##exercise 1-8.2

s = "Python Programming"
print(len(s))

##exercise 1-8.4

s = "Python Programming"
i = 15

if len(s) == 0:
    print("Empty String")
elif i < len(s):
    print(s[i])
else:
    print("i out of range")

##exercise 1-8.6

s = "Python Programming"

reversed_word = s[::-1]
print(reversed_word)

##exercise 1-8.8

s = "Programming Language"
num_chars = 3

if len(s) < 6:
    print("")
else:
    new_string = s[:num_chars] + s[len(s)-num_chars:]
    print(new_string)

##exercise 1-8.11

s = "Programming"
new_s = ""
if (s == " ") or (len(s) == 1):
    print(s)
else:
    for i in range(len(s)):
        if i % 2 != 0:
          new_s += s[i]

    print(new_s)


##exercise 1-8.13

s = "5"
print(s.isdigit())

##exercise 1-8.15

s = "Python Programming"
n = 4

if (len(s) == 0) or (n >= len(s)):
    print(s)
else:
    new_s = ""
    for i in range(len(s)):
        if i != n:
            new_s += s[i]
    print(new_s)  

##exercise 1-8.17

s = "Programming"

curr_char = "i"
new_char = "O"

print(s.replace(curr_char, new_char))

##exercise 9-16.1

s = "10,123,456,789"
COMMA = ","
DOT = "."

print(s.replace(COMMA, DOT))

##exercise 9-16.3

import string

s = "The quick brown fox jumps over the lazy dog"

set_s = set(s.lower().replace(" ",""))

print(set_s == set(string.ascii_lowercase))

##exercise 9-16.5

s = "Python Programming"

print(s.replace(" ", ""))

##exercise 9-16.7

s = "Programming"
prefix = "Prog"

if len(prefix) > len(s):
    print(False)
else:
    print(s.startswith(prefix))

##exercise 9-16.9

s = "Programming"
suffix = "Ming"

if len(suffix) > len(s):
    print(False)
else:
    print(s.endswith(suffix))

##exercise 9-16.12

s = "Python Programming"

words_list = s.split(" ")
new_s = ""

for word in words_list:
	reversed_word = "".join(reversed(word))
	swapped_case = reversed_word.swapcase()
	new_s += swapped_case + " "

new_s.rstrip()

print(new_s)

##exercise 9-16.14

s = "Programming Language"

repeated_chars = []

for char in s:
	if (s.count(char) > 1) and (char not in repeated_chars):
		repeated_chars.append(char)

print(len(repeated_chars))

if repeated_chars:
	print(*sorted(repeated_chars), sep=" ")
else:
	print("None")
     
##exercise 9-16.16

s = "Python Programming"
new_s = ""

words_list = s.split(" ")

for word in words_list:
	new_s += "".join(sorted(word.lower())) + " "

new_s.rstrip()

print(new_s)

##exercise 17-24.2

item_list = [1, 2, 3, "a", "b","c"]
factor = 9
output_list = []

for i in range(len(item_list)):
	output_list.append(item_list[i] * factor)

print(output_list)

##exercise 17-24.4

item_list = [1, 2, 3, "a", "b","c"]

print(*item_list,sep=" ")

##exercise 17-24.6

item_list = [1, 3, 5, 7, 9, 0]

if item_list:
	print(max(item_list), min(item_list))
else:
	print(None)

##exercise 17-24.8

item_list = [2]

if len(item_list) == 0:
	print("Empty")
else:
	print("Not Empty")

##exercise 17-24.11

item_list = ["A", "B", "C", "D"]

if len(item_list) == 0:
	print("Empty List")
else:
	for index, element in enumerate(item_list):
		print(f"{element} {index}")
            
##exercise 17-24.13

item_list = [3, 3, 2, 1,3]
elem_to_remove = 3
removed_items = 0

if not item_list:
	print("Empty List")
elif item_list.count(elem_to_remove) == 0:
	print("Not Found")
else:
	for i in range(item_list.count(elem_to_remove)):
		item_list.remove(elem_to_remove)
		removed_items +=1
		
if removed_items > 0:
    print(item_list)

##exercise 17-24.15

item_list = [3, 3, 2, 1, 3, 4, 2]
distinct_val= list(set(item_list))
print(distinct_val)

##exercise 17-24.17

item_list = [3, 3, 1, 3, 4, 2, 5,6 , 7]
item_count = 0
for i in item_list :
    if i > 3:
        item_count +=1
print(item_count)

##exercise 25-32.1

listA = [1, 2, 3, 4, 5, 6]
listB = [1,2,3,4,5,6]
output = []
for i in listA:
    if i not in listB:
        output.append(i)
print(output)

##exercise 25-32.3

pointA = [2, 3, 5]
pointB = [2, 3, 5]

distance = ((pointA[0] - pointB[0])**2
			+ (pointA[1] - pointB[1])**2
			+ (pointA[2] - pointB[2])**2)**(1/2)

print(distance)

##exercise 25-32.5

listA = [1,2,3,4,5,6,7,8]
listB = [1,3,5,7,9]
common = []

for x in listA:
    if x in listB:
        common.append(x)

print(common)

##exercise 25-32.7

item_list = [1,3,6,8,9,8]
if  len(item_list) < 2:
    print(None)
else:
    desc_list= sorted(item_list, reverse=True)
    print(desc_list[1])

##exercise 25-32.10

item_list = [1,3,6,8,9,8]
if  len(item_list) < 2:
    print(None)
else:
    asc_list= sorted(item_list)
    print(asc_list[1])

##exercise 25-32.12

item_list = ["a","a","a","b","b","c","C","d","d"]
dictionary = {}
for x in item_list:
    if x in dictionary:
        dictionary[x] += 1
    else:
        dictionary[x] = 1
print(dictionary)

##exercise 25-32.14

item_list = ["h", "e", "l", "l", "o", "w", ["o", "r", "l","d"]]
flat_list = []

for x in item_list:
	if isinstance(x, list):
		for nested_item in x:
			flat_list.append(nested_item)
	else:
		flat_list.append(x)

print(flat_list)

##exercise 25-32.16

import itertools

item_list = [1, 2, 3]
permutations = list(itertools.permutations(item_list))

for permutation in permutations:
	print(list(permutation))
      
##exercise 25-32.18

import itertools

item_tuple = (1, 2, 3)
permutations = list(itertools.permutations(item_tuple))

for permutation in permutations:
	print(tuple(permutation))
      
##exercise 33-38.2
dictionary = {"a": 1,"b": 2}
key = "2"

if key in dictionary:
    print(True)
else:
    print(False)

##exercise 33-38.4

my_dict = {"a": 1, "b": 2, "c": 3}

new_key ="d"
new_value = 3

if new_key not in my_dict:
    my_dict[new_key] = new_value
print(my_dict)

##exercise 33-38.6

dictionary1 = {"a": 1, "b": 2, "c": 3}
dictionary2 = {"b": 4, "c": 6, "e": 8}
final_dict = dictionary1 | dictionary2
print(final_dict)

##exercise 33-38.9

dictionary = {"a": 4, "b": 4, "c": 4}
values = len(set(dictionary.values()))
if values == 0:
    print("Empty")
elif values > 1:
    print(False)
else:
    print(True)

##exercise 33-38.11

dictionary = {"a":5,"b":10,"c":15}
values = dictionary.values()
invalid_char = 0
for x in values:
    if not isinstance(x,int):
       invalid_char +=1
if invalid_char > 0:
    print(None)
else:
    print(max(dictionary.values()))

##exercise 33-38.13

dictionary = {"a":5,"b":10,"c":15}
values = dictionary.values()
invalid_char = 0
for x in values:
    if not isinstance(x,int):
       invalid_char +=1
if invalid_char > 0:
    print(None)
else:
    print(min(dictionary.values()))

##exercise 39-44.1

my_dict = {
	"a": 9,
	"b": 9,
	"c": 6,
	"d": 3,
	"e": 9,
	"f": 6,
	"g": 3,
	"h": 3
 }
freq_dict={}
values = list(my_dict.values())
for x in values:
    total = values.count(x)
    freq_dict[x] = total     
print(freq_dict)

##exercise 39-44.3

item_list = [["a", 2], ["b", 4], ["c", 6], ["d", 8]]
dictionary = {}

for x in item_list:
	key = x[0] 
	value = x[1]
	dictionary[key] = value

print(dictionary)

##exercise 39-44.5

dictionary = {
	"a": [1,2,3],
	"b": [4,5,6],
	"c": [7,8,9],
	"d": [10,11,12]
}
total = []
values = dictionary.values() 
for x in values:
    total.append(sum(x))
print(max(total))

##exercise 39-44.8

my_string = "Python Programming"
dictionary ={}
for i in my_string.lower():
    if i.isalpha():
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
print(dictionary)

##exercise 39-44.10

dictionary = {
	"a": [1, 3, 2],
	"b": [5, 4, 6],
	"c": [8, 10, 9],
	"d": [13, 11, 12]
}
for values in dictionary.values():
	values.sort()

print(dictionary)

##exercise 39-44.12

motor_desc = {
	"motor": "Click 125i",
	"price": 82000,
	"colors": ["black", "blue", "red","white"],
}
new_list = []

for key, value in motor_desc.items():
	new_list.append([key, value])

print(new_list)

##exercise 45-50.2

num = -3

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

##exercise 45-50.4

my_string = "Color: White"
vowel =["a","e","i","o","u"]

if not my_string:
    print("Empty String")
else:
    for x in my_string.lower():
        if not x.isalpha():
            print(f"{x} is not a letter")
        elif x not in vowel:
            print(f"{x} is a consonant")
        else:
            print(f"{x} is a vowel")

##exercise 45-50.6

a = 2
b = 4
c = 6

print(max(a,b,c))

##exercise 45-50.9

a = 2
b = 4
c = 6

print(min(a,b,c))

##exercise 45-50.11

season_num = 4

if season_num ==1:
    print("Spring")
elif season_num ==2:
    print("Summer")
elif season_num ==3:
    print("Fall")
elif season_num ==4:
    print("Winter")
else:
    print("Please enter a valid number")

##exercise 45-50.13

a = 2
b = 2
c = 2

if a == b and b == c:
    print("Equal")
else:
    print("Not Equal")

##exercise 51-56.1

month = "January"

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

a = 1
b = 2
c = 3

if a > b > c:
    print("Decreasing Order")
elif a < b < c:
    print("Increasing Order")
else:
    print(None)

##exercise 51-56.5

import math

a = 3
b = 5
c = -2

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

year = 1912

if not year  %4 == 0:
    print(f"{year} is a common year")
elif not year %100 == 0:
    print(f"{year} is a leap year")
elif not year %400 == 0:
    print(f"{year} is a common year")
else:
    print(f"{year} is a leap year")

##exercise 51-56.10

print("=== Welcome to your Interactive Python Calculator ===")
num1 = int(input("Please enter te 1st value: "))
num2 = int(input("Please enter the second value: "))

print("Great! Now enter the operation.")
print("These are the available options:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Integer Division")
print("6 - Modulo")

operation = int(input("Please enter the corresponding integer: "))

if operation == 1:
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")
elif operation == 2:
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")
elif operation == 3:
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")
elif operation == 4:
    result = num1 / num2
    print(f"The result of {num1} / {num2} is: {result}")
elif operation == 5:
    result = num1 // num2
    print(f"The result of {num1} // {num2} is: {result}")
elif operation == 6:
    result = num1 % num2
    print(f"The result of {num1} % {num2} is: {result}")
else:
    print("invalid operation")

##exercise 51-56.12

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

##exercise 57-63.2

num = 15
for x  in range(15):
    print(x+1)

##exercise 57-63.4

num = int(input("Enter a number: "))
for x  in range(num,0,-1):
    print(x)

##exercise 57-63.6

total = 0
for x in range(100):
    total += x+1


print(total)

##exercise 57-63.8

n = int(input("Enter a value : "))
print(f"===== Multiplication Table of {n} =====")

for x in range(1,11):
    print(f"{n} x {x} = { n*x}")

##exercise 57-63.11

for x in range(65, 91):
	print(chr(x))
     
##exercise 57-63.13

for x in range(2, 201, 2):
    print(x)

##exercise 57-63.15
n = int(input("Enter the value of 'n': "))

factorial = 1

for x in range(2, n+1):
	factorial *= x

print(factorial)

##exercise 57-63.17

num = int(input("Enter the value: "))
x = 0
factorial = 1

while x < num:
    x+=1
    factorial*=x   

print(factorial)

##exercise 64-71.1

num = 17

if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(f"{num} is not a prime number")
           print(f"{i} times {num//i} is {num}")
           break
   else:
       print(f"{num} is a prime number") 

else:
   print(f"{num} is not a prime number")

##exercise 64-71.3

n = int(input("Enter the value of 'n': "))

for x in range(n):
    print((x+1) * "*")

##exercise 64-71.5

num = 2468

reverse = int(str(num)[::-1])

print(reverse)

##exercise 64-71.7  

my_string = "Python"

for x in reversed(my_string):
	print(x, end="")
     
##exercise 64-71.10

n= int(input("enter the number of rows: "))
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    
    print()

##exercise 64-71.12

n= int(input("enter the number of rows: "))
count = 1
for i in range(1,n+1):
    for x in range(i):
        print(count,end=" ")
        count +=1
    print()

##exercise 64-71.14

n= int(input("enter the number of rows: "))
char = 65

for x in range(1,n+1):
    print(chr(char)* x,end="")
    char+=1
    print()

##exercise 64-71.16

height = int(input("Enter the diamond's height (an odd number): "))

if height % 2 == 0:
    print("Please enter an odd value for the height (number of rows).")
else:
    middle_rows = (height + 2) // 2

    for i in range(middle_rows):
        print(" " * (middle_rows - i), "*" * (i*2 + 1))

    for i in range(middle_rows-2, -1, -1):
        print(" " * (middle_rows - i), "*" * (i*2 + 1))

##exercise 72-76.2

def sum(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum(numbers[1:])

n = [1, 3, 5, 7, 9]
print(sum(n))

##exercise 72-76.4

def fibonacci_of(n):
    if n in {0, 1}:  
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)
n = 1
print(fibonacci_of(n))

##exercise 72-76.6

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
    
num = 6
print( factorial(num))

##exercise 72-76.9
def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

num = 4
print(sum_of_digits(num))

##exercise 72-76.11
def exponent(n,m):
    if m == 0:
        return 1
    else:
        return n * exponent(n, m - 1)

num1= 4
num2 = 2
print(exponent(num1,num2))

##exercise 77-82.1
def gcd(n, i):
    if i == 0:
        return n
    else:
        return gcd(i, n % i)


n = 20
i = 96
print(gcd(n, i))

##exercise 77-82.3
def ispalindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return ispalindrome(word[1:-1])

s = "Hello"

print(ispalindrome(s))

##exercise 77-82.5

def vowelCount(s):
    if not s:
        return 0
    return (1 if s[0] in 'aeiouAEIOU' else 0) + vowelCount(s[1:])
s = "TEST"
print(vowelCount(s))

##exercise 77-82.8

def pattern(n):
	if n == 1:
		print("*")
	else:
		print("*" * n)
		pattern(n-1)

print(pattern(5))

##exercise 77-82.10

def convertToBinary(n):
    if n > 1:
        return convertToBinary(n // 2) + str(n % 2)
    return str(n)

print(convertToBinary(8))

##exercise 77-82.12

def binary_search(arr, target, low, high):
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, low, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, high)
    else:
        return -1
    
arr = [2,4,6,8,10]
target = int(input("Enter number to search: "))

result = binary_search(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Found at index {result}")
else:
    print("Not found")

##exercise 83-87.2
with open('2.1 basic_file.txt', 'r') as file:
    file_content = file.readlines()
file_content = [line.strip() for line in file_content]

print(file_content)

##exercise 83-87.4
n = int(input("Enter the number of lines to print: "))

with open('3.1 basic_file.txt', 'r') as file:
    file_content = file.readlines()

if n > len(file_content):
    print(f"Please enter a value for n. The file has {len(file_content)} lines.")
else:
    for i in range(n):
        print(file_content[i].strip())

##exercise 83-87.7
n = int(input("Enter the number of last lines to print: "))

with open('8.1 basic_file.txt', 'r') as file:
    file_content = file.readlines()

if n <= len(file_content):
    for line in file_content[-n:]:
        print(line.strip())
else:
    print(f"The file has only {len(file_content)} lines.")


##exercise 83-87.9
with open('10.1 words.txt', 'r') as file:
    words = [line.strip() for line in file.readlines()]

longest_word = max(words, key=len)

print(longest_word)

##exercise 83-87.11
word_frequency = {}

with open('12.1 words.txt', 'r') as file:
    for line in file:
        word = line.strip()
        
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

print(word_frequency)

##exercise 88-91.1
elements = [1, 2, 3, 4, 5]

with open('mywords.txt', 'w') as file:
    for element in elements:
        file.write(str(element) + '\n')

print("List elements have been written to the file.")

##exercise 88-91.3
with open('words.txt', 'r') as file:
    total_chars = 0
    
    for line in file:
        line = line.strip().replace(' ', '')
        total_chars += len(line)

print(f"Total Number of Characters: {total_chars}")

##exercise 88-91.6
with open('7.2 famous_quotes.txt', 'r') as source_file, open('destination.txt', 'w') as destination_file:
    content = source_file.read()
    
    destination_file.write(content)

print("File copied successfully.")

##exercise 88-91.8
import os

file_path = input("Enter the file path or name: ")

if os.path.isfile(file_path):
    print(f"The file {file_path} exists")
else:
    print(f"The file {file_path} doesn't exist")

##exercise 92-97.4
def convert_seconds(seconds):
    minutes = seconds // 60
    
    hours = seconds / 3600
    
    print(f"{seconds} seconds is equivalent to:")
    print(f"{minutes} Minutes")
    print(f"{hours:.2f} Hours")

seconds_input = int(input("Enter the number of seconds: "))
convert_seconds(seconds_input)

##exercise 92-97.6
import math

def calculate_area(diameter):
    radius = diameter / 2
    
    area = math.pi * (radius ** 2)
    
    area = round(area, 2)
    
    print(f"The area of a circle with diameter {diameter} is {area}")

diameter = int(input("Enter the diameter of the circle: "))

calculate_area(diameter)


##exercise 92-97.9
try:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))

    if base <= 0 or height <= 0:
        print("Please enter valid values for base and height")
    else:
        area = (base * height) / 2
        print(f"The area of the triangle is {round(area, 2)}")

except ValueError:
    print("Please enter valid values for base and height")


##exercise 92-97.11
celsius = float(input("Enter the temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")


##exercise 92-97.13
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

print(f"{fahrenheit} Fahrenheit = {celsius} Celsius")

##exercise 98-101.1
height_cm = float(input("Enter your height in centimeters: "))
weight_kg = float(input("Enter your weight in kilograms: "))

height_m = height_cm / 100

bmi = weight_kg / (height_m ** 2)

bmi_rounded = round(bmi, 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"

print(f"BMI: {bmi_rounded}, Category: {category}")


##exercise 98-101.3
import calendar

try:
    month = int(input("Enter the month (1-12): "))
    year = int(input("Enter the year: "))

    if month < 1 or month > 12:
        print("Please enter a valid month between 1 and 12.")
    else:
        print(calendar.month(year, month))
        
except ValueError:
    print("Please enter valid integers for the month and year.")


##exercise 98-101.6
from datetime import date

try:
    year1, month1, day1 = map(int, input("Enter the first date (Year Month Day): ").split())
    year2, month2, day2 = map(int, input("Enter the second date (Year Month Day): ").split())

    date1 = date(year1, month1, day1)
    date2 = date(year2, month2, day2)

    if date1 > date2:
        print("Please enter valid dates")
    elif date1 == date2:
        print("The dates are equal")
    else:
        delta = (date2 - date1).days
        if delta == 1:
            print("There is 1 day between these dates.")
        else:
            print(f"There are {delta} days between these dates.")
except ValueError:
    print("Please enter valid dates in the format Year Month Day.")

##exercise 98-101.8
import re

user_input = input("Enter a string: ")

pattern = r"^My\w*$"  

if re.match(pattern, user_input) and user_input.endswith("blue"):
    print("Match")
else:
    print("Not Match")






