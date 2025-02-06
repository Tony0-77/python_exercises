#Exercise 1-8.1 Print the length of a string
s="Hello"
print(f"The length of the string is: {(len(s))}")

#Exercise 1-8.2 Print the character at a specific index
s="Hello"
i=2

if len(s) == 0:
    print(f"Empty string")

else:
    if i >= len(s):
        print(f"Index is out of range")
    else:
        print(f"The output is {s[i]}")

#Exercise 1-8.3 Reverse a string
s="Hello"
print(s[::-1])

#Exercise 1-8.4 First and last three characters in a string
s="Wonderful"
if len(s) < 6:
    print("")
else:
    print(f"{s[:3]}{s[-3:]}")

#Exercise 1-8.5 Remove characters at even indices
s="Coding"
output=s[1::2]

if len(s) < 2:
    print(s)
else:
    print(output)

#Exercise 1-8.6 Check if a string only contains numbers
s="Hello"
print(s.isdigit())

#Exercise 1-8.7 Remove nth character from a string
s="Hello"
n=1
if len(s) == 0:
    print(s)

else:
    if n >= len(s):
        print(s)

    else:
        print(f'{s[:n]}{s[n+1:]}')

#Exercise 1-8.8 Replace a character in a string
s="Hello"
curr_char="l"
new_char="s"
char_list=list(s)

for i in range(len(char_list)):
  if char_list[i] == curr_char:
        char_list[i] = new_char

new_word=''.join(char_list)
print(new_word)

#Exercise 9-16.9 Change commas by dots
s="Hello, world"
char_list=list(s)
for i in range(len(char_list)):
  if char_list[i] == ",":
        char_list[i] = "."

new_word=''.join(char_list)
print(new_word)

#Exercise 9-16.10 Check if string contains all characters in the alphabet
import string

s="The quick brown fox jumps over the lazy dog"
s_lower=s.lower()
s_charset=set(s_lower)
letter_set=set(string.ascii_lowercase)
intersection=s_charset.intersection(letter_set)

if len(intersection) == 26:
    print(True)
else:
    print(False)

#Exercise 9-16.11 Remove spaces from a string
s="Have a great day"
char_list=list(s)
for i in range(len(char_list)):
  if char_list[i] == " ":
        char_list[i] = ""

new_word=''.join(char_list)
print(new_word)

##Exercise 9-16.12 Check if a string starts with a prefix
s="Hello"
prefix="He"
if len(prefix) > len(s):
    print(False)
elif s[:len(prefix)] == prefix:
    print(True)
else:
    print(False)

##Exercise 9-16.13 Check if a string ends with a suffix
s="Hello"
suffix="ello"

if len(suffix) > len(s):
    print(False)
elif s[len(suffix):] == suffix:
    print(True)
else:
    print(False)

##Exercise 9-16.14 Reverse words in a string
s="Hello World"
print(s[::-1].swapcase())

##Exercise 9-16.15 Count repeated characters
s="Corporation"
char_list=list(s)
unique_char=[]
repeated_char=[]

for char in char_list:
    if char in unique_char:
        repeated_char.append(char)

    else:
        unique_char.append(char)

if len(repeated_char) == 0:
    print(f"""0
            None""")
else:
    print(f"""
        {len(repeated_char)}
        {repeated_char}
        """)

#Exercise 9-16.16 Sort words in alphabetical order
s = "Hello world".lower()

for item in s.split():
    new_word = ''.join(sorted(item))
    print(new_word, end=' ')

#Exercise 17-24.17 Multiply all elements in a list
my_list=[1,2,3,4]
new_list=[]
factor=2

for num in my_list:
    product=num*factor
    new_list.append(product)

print(new_list)

#Exercise 17-24.18 Print the elements of a list
my_list=["a","b","c"]
output=" ".join(map(str,my_list))
print(output)

#Exercise 17-24.19 Get max and min value
my_list=[1,2,3,4]
if len(my_list) == 0:
    print(None)
else:    
    print(max(my_list),min(my_list))

#Exercise 17-24.20 Check if list is empty or not
my_list=[]
if len(my_list) == 0:
    print("Empty")
else:
    print("Not Empty")

#Exercise 17-24.21 Print the elements and their indices
my_list=["a","b","c"]
for key,value in enumerate(my_list):
    print(value,key)

#Exercise 17-24.22 Remove matching element
my_list=[1,2,3,4]
elem_to_remove=4
new_list=[]

if len(my_list) == 0:
    print("Empty List")
elif len(new_list) == 0:
    print("Not found")
else:
    for elem in my_list:
        if elem != elem_to_remove:
            new_list.append(elem)
        else:
            continue
   
    print(new_list)

#Exercise 17-24.23 Remove duplicates from a list
my_list=[1,2,2,3,3]
print(list(set(my_list)))

#Exercise 17-24.24 Count elements greater than 3
my_list=[1,2,3,5,6]
new_list=[]

for elem in my_list:
    if elem > 3:
        new_list.append(elem)
    else:
        continue

print(len(new_list))

#Exercise 25-32.25 Difference between two lists
list_a = [1, 2, 3, 4]
list_b = [1,2,3,4]

for elem in list_b:
    if elem in list_a:
        list_a.remove(elem)
print(list_a)

#Exercise 25-32.26 Distance between two 3D points
import math

list_a=[3,4,5]
list_b=[2,0,-4]

distance=math.dist(list_a,list_b)
print(distance)

#Exercise 25-32.27 Print common elements in two lists
list_a = [1, 2, 3, 4]
list_b = [3,4,6]
new_list = []

for elem in list_b:
    if elem in list_a:
        new_list.append(elem)
print(new_list)

#Exercise 25-32.28 Find the second largest value in a list
my_list = [1,2]
if len(my_list) <= 1:
    print(None)
else:    
    duplicate_removed= sorted(list(set(my_list)))
    print(duplicate_removed[len(duplicate_removed)-2])

#Exercise 25-32.29 Find the second smallest value in a list
my_list = [1,2,3,4]
if len(my_list) <= 1:
    print(None)
else:    
    duplicate_removed= sorted(list(set(my_list)))
    print(duplicate_removed[1])

#Exercise 25-32.30 Make a frequency dictionary from the elements of a list
my_list = [1,1,2,2,3]
my_dict={}

for elem in my_list:
    if elem in my_dict:
        my_dict[elem] += 1
    else:
        my_dict[elem] = 1

print(my_dict)

#Exercise 25-32.31 Flatten a list that contains list
my_list=[[1,2,3],[4,5,6],[7,8,9]]
flatten_list=[]

for lists in my_list:
    for elem in lists:
        flatten_list.append(elem)

print(flatten_list)

#Exercise 25-32.32 Generate all permutations of a list
import itertools

my_list=[1,2,3]
print(list(itertools.permutations(my_list)))

#Exercise 33-38.33 Check if a key exists in a dictionary
my_dict={"a":4,"b":6}
a_key="a"

if a_key in my_dict.keys():
    print(True)
else:
    print(False)

#Exercise 33-38.34 Add a key-value pair only if the key is not in the dictionary
initial_dict={"a":4,"b":6}
new_pair={"a":4}

if new_pair not in initial_dict.items():
    initial_dict.update(new_pair)

print(initial_dict)

#Exercise 33-38.35 Merge two dictionaries
first_dict={"a":1,"b":2,"c":3}
second_dict={"c":4,"d":6,"e":8}

final_dict=first_dict | second_dict

print(final_dict)

#Exercise 33-38.36 Check if all values are equal
my_dict={"c":4,"d":4,"e":4}
values_array=[]


for values in my_dict.values():
    values_array.append(values)

array_to_set_values=set(values_array)

if len(my_dict) == 0:
    print("Empty")
elif len(array_to_set_values) == 1:
    print(True)
else:
    print(False)

#Exercise 33-38.37 Find the maximum value in a dictionary
my_dict={"c":4,"d":9,"e":15}
values_array=[]


for values in my_dict.values():
    values_array.append(values)

max_value=max(values_array)

if len(my_dict) == 0:
    print(None)
else:
    print(max_value)

#Exercise 33-38.38 Find the minimum value in a dictionary
my_dict={"c":4,"d":9,"e":15}
values_array=[]


for values in my_dict.values():
    values_array.append(values)

min_value=min(values_array)

if len(my_dict) == 0:
    print(None)
else:
    print(min_value)

#Exercise 39-44.39 Find frequency of values in a dictionary
my_dict = {"a":4,"b":4,"c":2,"d":7,"e":4,"f":2,"g":7,"h":7}
freq_dict={}
for value in my_dict.values():
    if value in freq_dict:
        freq_dict[value] += 1
    else:
        freq_dict[value] = 1

print(freq_dict)

#Exercise 39-44.40 Make a dictionary from nested lists
my_list = [["a",1],["b",1]]
my_dict={}

for dict_items in my_list:
    my_dict[dict_items[0]]=dict_items[1]

print(my_dict)

#Exercise 39-44.41 Print largest sum of values
my_dict={"a":[1,2,35],"b":[7,8,9],"c":[10,11,12]}
max_sum = sum(my_dict[max(my_dict, key=lambda k: sum(my_dict[k]))])

print(max_sum)

#Exercise 39-44.42 Make a frequency dictionary for characters in a string
s=input("Enter String: ").lower()
freq_dict={}

for char in s:
    if char.isalpha():
        if char in freq_dict:
            freq_dict[char]+=1
        else:
            freq_dict[char]=1

print(freq_dict)

#Exercise 39-44.43 Sort list in ascending order
my_dict = {"a":[4,3,2],"b":[1,5,4]}
new_dict={}

for key,value in my_dict.items():
    value.sort()
    new_dict[key]=value

print(new_dict)
    
#Exercise 39-44.44 Convert dictionary into a list of lists
product_info={"description":"shoe","price":4.56,"color":["green","blue","red"]}
my_list=[]

for key, value in product_info.items():
    my_list.append([key,value])

print(my_list)
    
#Exercise 45-50.45 Zero, positive, or negative
num = int(input("Enter Number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#Exercise 45-50.46 Check vowels and consonants
s=input("Input String: ")
vowel=["a","e","i","o","u"]

for char in s:
    if char.isalpha():
        if char in vowel:
            print(f'{char} is a vowel')
        else:
            print(f'{char} is a consonant')
    else:
        print(f'{char} is not a letter')

#Exercise 45-50.47 Print max of three numbers
a=int(input("Enter first integer: "))
b=int(input("Enter second integer: "))
c=int(input("Enter third integer: "))

max_num=max(a,b,c)
print(f'Integers: ({a},{b},{c}) Output: {max_num}')

#Exercise 45-50.48 Print min of three numbers
a=int(input("Enter first integer: "))
b=int(input("Enter second integer: "))
c=int(input("Enter third integer: "))

min_num=min(a,b,c)
print(f'Integers: ({a},{b},{c}) Output: {min_num}')

#Exercise 45-50.49 Four seasons
season_num=int(input("Input number: "))
season_dict={1:"Spring",2:"Summer",3:"Fall",4:"Winter"}

if season_num in season_dict.keys():
    print(season_dict[season_num])
else:
    print("Please enter a valid number")

#Exercise 45-50.50 Compare three numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
num_set={a,b,c}

if len(num_set) == 1:
    print("Equal")
else:
    print("Not Equal")

#Exercise 51-56.51 Find number of days in a month
month="January"
month_31=["January","March","May","July","August","October","December"]
month_30=["April","June","September","November"]

if month in month_31:
    print(f'{month} has 31 days')
elif month == "February":
    print(f'{month} has 28 days')
elif month in month_30:
    print(f'{month} has 30 days')
else:
    print('Please enter a valid month')

#Exercise 51-56.52 Increasing or decreasing order
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

if a > b > c:
    print("Decreasing order")
elif a < b < c:
    print("Increasing order")
else:
    print(None)

#Exercise 51-56.53 Solve quadratic equations
import math

a=int(input("Enter value a: "))
b=int(input("Enter value b: "))
c=int(input("Enter value c: "))

discriminant = b**2 - (4 * a * c)

root_a = (-b + math.sqrt(discriminant))/(2*a)
root_b = (-b - math.sqrt(discriminant))/(2*a)

if discriminant < 0:
    print("Complex Roots")
elif discriminant > 0:
    if root_a > root_b:
        print(root_b,root_a)
    else:
        print(root_a,root_b)
else:
    print(root_a)

#Exercise 51-56.54 Check if a year is a leap year or not
year = int(input("Input year: "))

if year%4 == 0 :
    if year%100 == 0:
        if year%400 == 0:
            print("Yes")
        else:
            print("No")
    else:
       print("Yes")
else:
    print("No")

#Exercise 51-56.55 Interactive calculator
print("===Welcome to your Interactive Python Calculator===")
a=int(input("Please enter first value: "))
b=int(input("Please enter second value: "))
print(f"""        Great! Now enter the operation.
        These are the available options:
                1 - Addition
                2 - Subtraction
                3 - Multiplication
                4 - Division
                5 - Integer Division
                6 - Modulo
        """)
c=int(input("Enter the corresponding integer: "))
operation_dict={1:"+",2:"-",3:"*",4:"/",5:"//",6:"%"}

if c in operation_dict.keys():
    if c == 1:
        result = a + b
    elif c == 2:
        result = a - b
    elif c == 3:
        result = a*b
    elif c == 4:
        result = a/b
    elif c == 5:
        result = a//b
    elif c == 6:
        result = a%b
    
    print(f'The result of {a} {operation_dict[c]} {b} is {result}')
else:
    print("Please choose a valid operation.")

#Exercise 51-56.56 Rock, paper, scissors
import random

print("===Welcom to the Game===")
user=input("Please enter 'Rock','Paper','Scissors':")
option_list=["Rock", "Paper", "Scissors"]
computer = random.choice(option_list)

if user in option_list:
    if user == "Rock":
        if computer == 'Rock':
            print("It's a tie")
        elif computer == "Scissors":
            print(f'You win! Your opponent chose {computer}')
        else:
            print(f'You lose! Your opponent chose {computer}')
    elif user == "Paper":
        if computer == 'Paper':
            print("It's a tie")
        elif computer == "Rock":
            print(f'You win! Your opponent chose {computer}')
        else:
            print(f'You lose! Your opponent chose {computer}')
    else:
        if computer == 'Scissors':
            print("It's a tie")
        elif computer == "Paper":
            print(f'You win! Your opponent chose {computer}')
        else:
            print(f'You lose! Your opponent chose {computer}')
else:
    print("Please enter valid option.")

#Exercise 57-63.57 Print the first 15 positive integers
for num in range(1,16,1):
    print(num)

#Exercise 57-63.58 Print integers in reverse order
n=5

for num in range(n,0,-1):
    print(num)

#Exercise 57-63.59 Sum of first 100 positive integer
print(sum(range(1,101,1)))

#Exercise 57-63.60 Print the multiplication table
print("===Multiplication Table of 3===")
for num in range(1,11,1):
    result = 3 * num
    print(f'3 x {num} = {result}')

#Exercise 57-63.61 Print the alphabet using a loop
for char in range(65,91,1):
    print(chr(char))

#Exercise 57-63.62 First 100 even numbers
for num in range(2,201,2):
    print(num)

#Exercise 57-63.63 Calculate factorial
import math
n=5
num_list=[]

if n == 0:
    num_list.append(1)
else:
    for num in range(n,0,-1):
        num_list.append(num)

result=math.prod(num_list)
print(result)

#Exercise 64-71.64 Check if a number is prime
n = 3

if n <= 1:  
    print("Not Prime")
else:
    for x in range(2, n):  
        if n % x == 0:
            print("Not Prime")
            break  
    else:
        print("Prime")

#Exercise 64-71.65 Print pattern using loops
n = 5

for x in range(1,n+1):
    print("*"*x)

#Exercise 64-71.66 Print digits in reverse order
n = int(input("Input number: "))
num_list=[]
for x in str(n):
    num_list.append(x)

new_num="".join(sorted(num_list,reverse=True))
print(new_num)

#Exercise 64-71.67 Reverse a string using a loop
s = input("Input string: ")
char_list=[]
for char in s:
    char_list.append(char)

char_list.reverse()
new_word="".join(char_list)
print(new_word)

#Exercise 64-71.68 Print half pyramid using loops
n = int(input("Input number: "))
for x in range(1, n + 1):
    print(" " * (n - x) + "*" * x)

#Exercise 64-71.69 Floyd Triangle
n = int(input("Input number: "))
initial_number = 1
for x in range(1, n+1):
    for y in range(x):
        print(initial_number,end=" ")
        initial_number += 1
    print("")

#Exercise 64-71.70 Triangular letters pattern
n = 3
a = 65 

for x in range(1, n + 1):
    for y in range(x):
        initial_char = chr(a)
        print(initial_char, end=" ")
    a += 1
    print()

#Exercise 64-71.71 Diamond made with asteriks
n = 3
increasing = list(range(1, n+1, 2))  
decreasing = list(range(n-2,0,-2))
result = increasing + decreasing

if n%2 == 0:
    print("Value is an even number. Please enter odd number.")
else:
    for x in result:
        spaces = (n - x) // 2 
        print(" " * spaces + "*" * x + " " * spaces)

#Exercise 72-76.72 Find the sum of a list using recursion
def recursive_sum(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + recursive_sum(numbers[1:])

my_list = [1,7,4]
print("Sum:", recursive_sum(my_list))

#Exercise 72-76.73 Find the nth fibonacci number
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = int(input("Enter a number: "))
print(f"The {n}th Fibonacci number is: {fibonacci_recursive(n)}")

#Exercise 72-76.74 Recursive factorial
def factorial_recursive(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*factorial_recursive(n-1)

n = int(input("Enter a number: "))
print(f"The result is: {factorial_recursive(n)}")

#Exercise 72-76.75 Find the sum of the digits of a positive integer
def recursive_sum(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + recursive_sum(numbers[1:])
    
n=int(input("Enter number: "))
my_list = []

for x in str(n):
    my_list.append(int(x))

print("Sum:", recursive_sum(my_list))

#Exercise 72-76.76 Solve a power recursively
def power_recursive(a, b):
    if b == 0:
        return 1
    else:
        return a * power_recursive(a, b - 1)

a = int(input("Enter the base (a): "))
b = int(input("Enter the exponent (b): "))
print(f"The result of {a} raised to the power of {b} is: {power_recursive(a, b)}")

#Exercise 77-82.77 Find the greatest common divisor
import math

a = 12
b = 48

c = math.gcd(a,b)
print(c)

#Exercise 77-82.78 Check if a string is a palindrome
s = input("Enter string: ").lower()
len_s = len(s)

first_half = s[:len_s//2]
second_half = s[len_s//2 + (1 if len_s % 2 != 0 else 0):]
second_half_reverse = second_half[::-1]

if s == "":
    print(False)
elif first_half == second_half_reverse:
    print(True)
else:
    print(False)

#Exercise 77-82.79 Count vowels in a string
def recursive_count_vowels(s):
    if not s:
        return 0
    vowels = "aeiou"
    if s[0].lower() in vowels:
        return 1 + recursive_count_vowels(s[1:])
    else:
        return recursive_count_vowels(s[1:])

s = input("Enter string: ")
vowel_count = recursive_count_vowels(s)
print(vowel_count)

#Exercise 77-82.80 Print a pattern using recursion
def recursive_pattern(n):
    if n == 0:
        return 0
    else:
        print("*"*n)
        recursive_pattern(n-1)

num_rows = int(input("Enter number of rows: "))
recursive_pattern(num_rows)

#Exercise 77-82.81 Convert decimal to binary
def bin_convert(n):
    if n == 0:
        return '0'
    else:
        return (bin_convert(n // 2) + str(n % 2)).lstrip("0")

num = int(input("Enter number: "))
print(bin_convert(num))

#Exercise 77-82.82 Implement binary search recursively

#Exercise 83-87.83 Read a text file
file_content = []

with open('basic_file.txt') as file:
    for line in file:
        file_content.append(line)

print(file_content)

#Exercise 83-87.84 Print the first n lines of a file
n=int(input("Enter number of lines: "))

with open('basic_file.txt') as file:
    line = file.readlines()
    num_lines = len(line)

if num_lines < n:
    print(f'Please enter valid value. The line has {n} lines')
else:
    for x in range(n):
	    print(line[x].strip("\n"))

#Exercise 83-87.85 Print the last n lines of a file
n=int(input("Enter number of lines: "))

with open('basic_file.txt') as file:
    line = file.readlines()
    num_lines = len(line)

if num_lines < n:
    print(f'Please enter valid value. The line has {n} lines')
else:
    for x in range(n,-1):
	    print(line[x].strip("\n"))

#Exercise 83-87.86 Find the longest word in a file
long_word = ""

with open('word.txt') as file:
    for word in file:
        if len(word) > len(long_word):
            long_word = word

print(long_word)

#Exercise 83-87.87 Make a frequency dictionary of the words in a file
word_dict: {}

with open('word.txt') as file:
    for word in file:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

print(word_dict)

#Exercise 88-91.88 Write a list to a file
my_list = [1,2,3,4,5]

file_path = "list.txt"

with open(file_path, "w") as file:
    for item in my_list:
        file.write(str(item) + "\n")

#Exercise 88-91.89 Count characters in a file
file_path = "file.txt"

char_count = 0

with open(file_path, "r") as file:
	for line in file:
		char_count += len(line.replace(" ", "").strip("\n"))

print(char_count)

#Exercise 88-91.90 Copy the content of a file to another file
file_path = "file.txt"
file_copy = "file_copy.txt"

with open(file_path,"r") as file, open(file_copy, "w") as copy:
    for line in file:
        copy.write(line)

#Exercise 88-91.91 Check if a file exists
import os

file_path = 'file.txt'

if os.path.exists(file_path):
    print(f"The file {file_path} exists")
else:
    print(f"The file {file_path} doesn't exist")

#Exercise 92-97.92 Display current date and time
import datetime

current_dt = datetime.datetime.now()
print(f"""Current date and time: 
{current_dt.strftime("%Y-%m-%d %H:%M:%S")}
      """)

#Exercise 92-97.93 Convert seconds to minutes and hours
sec = int(input("Enter number of seconds: "))
minutes = sec//60 
hours = minutes/60

print(f"""{sec} seconds is equivalent to:
      {minutes} minutes
      {hours} hour
      """)

#Exercise 92-97.94 Calculate the area of a circle
import math

d = int(input("Enter diameter: "))
area_circle = (math.pi*(d**2))/2

print(f"The area of the circle is {area_circle} sq. units")

#Exercise 92-97.95 Compute the area of a triangle
base = int(input("Input base: "))
height = int(input("Input height: "))

if base > 0  and height > 0:
    area_triangle = round((base*height)/2,2)
else:
    print("Please enter valid values")
    
#Exercise 92-97.96 Celsius to fahrenheit conversion
celsius = float(input("Enter the temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")

#Exercise 92-97.97 Fahrenheit to celsius conversion
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

print(f"{fahrenheit} Fahrenheit = {celsius} Celsius")

#Exercise 98-101.98 Calculate body mass index
height = float(input("Enter height in centimers: "))
weight = float(input("Enter weight in kg: "))

bmi = round(weight/((height/100)**2),2)

if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal")
elif 25.9 <= bmi <= 29.9:
    print("Overweight")
else:
    print("Obesity")

#Exercise 98-101.99 Print a calendar
import calendar

month  = int(input("Enter month(1-12): "))
year = int(input("Enter year: "))

print(calendar.month(year,month))

#Exercise 98-101.100 Find the number of days between two dates
from datetime import datetime

def get_date_input(prompt):
    while True:
        try:
            date_input = input(prompt)
            date = datetime.strptime(date_input, "%Y %m %d")
            return date
        except ValueError:
            print("Invalid date format. Please use 'Year Month Day' (e.g., 2021 3 15).")

def calculate_days_between_dates(date1, date2):
    delta = date2 - date1
    return delta.days

date1 = get_date_input("Enter the first date (Year Month Day): ")
date2 = get_date_input("Enter the second date (Year Month Day): ")

if date1 > date2:
    print("Please enter valid dates.")
else:
    days_between = calculate_days_between_dates(date1, date2)
    
    if days_between == 0:
        print("The dates are equal.")
    elif days_between == 1:
        print("There is 1 day between these dates.")
    else:
        print(f"There are {days_between} days between these dates.")

#Exercise 98-101.101 Check a pattern using regular expression
import re

def check_string(s):
    pattern = r"^My[\w\s]+blue$"

    if re.match(pattern, s):
        print("The string starts with 'My', ends with 'blue', and contains only alphanumeric characters.")
    else:
        print("The string does not meet the criteria.")

user_string = input("Enter a string: ")

check_string(user_string)