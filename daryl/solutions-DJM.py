# EXERCISE 1-8.2
# len(yourstring)
# define your string

S = "Python"
print(len(S))

# EXERCISE 1-8.4
# print(yourstring[characterposition])
# define your string
# define the character position

S = "Hello"
i = 0

if len(S) == 0:
    print("Empty String")
elif len(S) > 0:
    print(S[i])
else:
    print("i is out of range")

# EXERCISE 1-8.6
# define your string
# create a slice that starts at the end of the string,
# and moves backwards

S = "Hello World"

print(S[::-1])


# EXERCISE 1-8.8

S = "Amazing"

if len(S) < 6:
    print("")
else:
    NEW_STRING = S[:3] + S[len(S)-3:]
    print(NEW_STRING)

#EXERCISE 1-8.11

S = "Coding"

if len(S) <= 1:
    print(S)
else:
    print(S[1::2])

#EXERCISE 1-8.13

S = "59"

print(S.isdecimal())

#EXERCISE 1-8.15

S = "Hello"
n = 1

if len(S) < n:
    print(S)
else:
    NEW_STRING = S[:n] + S[n+1:]
    print(NEW_STRING)

#EXERCISE 1-8.17

S = "Python"
curr_char = "P"
new_char = "x"

print(S.replace(curr_char,new_char))


## EXERCISE 9-16.1

S = "3,456,344"

print(S.replace(",","."))


# EXERCISE 9-16.3
import string

S = "Hello"
does_contain = True

for char in string.ascii_lowercase:
    if char not in set(S.lower()):
        does_contain = False

print(does_contain)


## EXERCISE 9-16.5

S = "Hello, World"

print(S.replace(" ",""))


## EXERCISE 9-16.7

S = "Coding"
prefix = "cod"

print(S.startswith(prefix))

## EXERCISE 9-16.9

S = "Coding"
suffix = "ello"

print(S.endswith(suffix))

## EXERCISE 9-16.12

S = "Hello World"
list_of_words = S.split()
new_s = ""

for word in list_of_words:
    reversed_word = word[::-1]
    swapped_case = reversed_word.swapcase()
    new_s += swapped_case + " "

new_s.strip()
print(new_s)


## EXERCISE 9-16.14

S = "Helo"
repeat_count = 0
repeat_char = []

for char in S:
    if (S.count(char) > 1) and (char not in repeat_char):
        repeat_count += 1
        repeat_char.append(char)
print(repeat_count)

if len(repeat_char) > 0:
    for char in sorted(repeat_char):
        print(char, end= " ")
else:
    print("None")


## EXERCISE 9-16.16

S = "Hello World"
list_of_words = S.split()
new_s = ""

for word in list_of_words:
    convert_to_lower = word.lower()
    sorted_word = sorted(convert_to_lower)
    join_word = "".join(sorted_word)
    new_s += join_word + " "

new_s.strip()
print(new_s)


## EXERCISE 17-24.2

mylist = ["a","b","c","d"]
factor = 2

for index, value in enumerate(mylist):
    mylist[index] = value * factor


print(mylist)

## EXERCISE 17-24.4

## * in front of list variable unpack the values of that list
## my_list = [1,2,3] | print(*my_list) >> 1 2 3

mylist = [3,4,5,6]

print(*mylist, sep=" ")


## EXERCISE 17-24.6

mylist = [3,4,5,6]

if mylist:
    print(max(mylist),min(mylist))
else:
    print(None)


## EXERCISE 17-24.8

mylist = []

if mylist:
    print("Not Empty")
else:
    print("Empty")


## EXERCISE 17-24.11

mylist = [3,4,5,6]

if mylist:
    for index, value in enumerate(mylist):
        print(index,value)
else:
    print("Empty")


## EXERCISE 17-24.13

my_list = [3,3,2,1]
elem_to_remove = 3

if my_list:
    if my_list.count(elem_to_remove) == 0:
        print("Not found")
    else:
        for i in enumerate(my_list):
            my_list.remove(elem_to_remove)

        print(my_list)
else:
    print("Empty")


## EXERCISE 17-24.15

my_list = [1,1,2,2,3,3,4,4]

new_list = list(set(my_list))

print(new_list)


## EXERCISE 17-24.17

my_list = []

count = 0

for elem in my_list:
    if elem > 3:
        count += 1
print(count)


## EXERCISE 25-32.1

listA = [1,2,3,4]
listB = [1,2]
output = []

for item in listA:
    if item not in listB:
        output.append(item)
print(output)


## EXERCISE 25-32.3

pointA = [3,4,5]
pointB = [1,3,5]


distance = (((pointA[0] - pointB[0])**2) + ((pointA[1] - pointB[1])**2) 
            + ((pointA[2] - pointB[2])**2))**(1/2)

print(distance)


# EXERCISE 25-32.5

listA = [4,5,6]
listB = [1,2,3]
output = []

for item in listA:
    if item in listB:
        output.append(item)

print(output)


##EXERCISE 25-32.7

my_list = [1]

if len(my_list) > 1:
    my_list.sort(reverse=True)
    
    print(my_list[1])

else:
    print(None)



## EXERCISE 25-32.10

my_list = [10,11,8,3]

if len(my_list) > 1:
    my_list.sort()

    print(my_list[1])
else:
    print(None)


## EXERCISE 25-32.12

my_list = [1,1,2,3]

dictionary_freq = {}

for item in my_list:
    if item not in dictionary_freq:
        dictionary_freq[item] = 1
    else:
        dictionary_freq[item] += 1
    
print(dictionary_freq)


## EXERCISE 25-32.14

nested_list = [[1,2,3],[4,5,6],[7,8,9]]
new_list = []

for sublist in nested_list:
    for item in sublist:
        new_list.append(item)

print(new_list)


## EXERCISE 25-32.16

import itertools

my_list = [1,2,3]


perm = itertools.permutations(my_list)

new_list = list(perm)

for sublist in new_list:
    print(list(sublist))



## EXERCISE 33-38.2

my_dict = {"a":4,"b":6}
key = "b"

##if key in my_dict:
##    print(True)
##else:
##    print(False)

print(key in my_dict)


## EXERCISE 33-38.4

my_dict = {"January":45,"February":56,"March":67}
new_key = "April"
new_value = 67

if new_key not in my_dict:
    my_dict[new_key] = new_value

print(my_dict)

## EXERCISE 33-38.6

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"c": 4, "d": 6, "e": 8}

merge_dict = {**dict1, **dict2}

print(merge_dict)


## EXERCISE 33-38.9

my_dict = {"a":4,"b":4,"c":4}
unique_values = len(set(my_dict.values()))

if unique_values == 0:
    print("Empty")
elif unique_values == 1:
    print(True)
else:
    print(False)


## EXERCISE 33-38.11

my_dict = {"a":4,"b":3,"c":7}

if my_dict:
    print(max(set(my_dict.values())))
else:
    print(None)


## EXERCISE 33-38.13

my_dict = {"a":4,"b":3,"c":7}

if my_dict:
    print(min(set(my_dict.values())))
else:
    print(None)


## EXERCISE 39-44.1

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

dictionary_freq = {}

for value in my_dict.values():
    if value not in dictionary_freq:
        dictionary_freq[value] = 1
    else:
        dictionary_freq[value] += 1
    
print(dictionary_freq)


## EXERCISE 39-45.3

my_list = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]
my_dict = {}

for sublist in my_list:
    my_dict[sublist[0]] = sublist[1]

print(my_dict)


## EXERCISE 39-45.5

my_dict = {
	"a": [1, 2, 3],
	"b": [4, 0, -4],
	"c": [3, 5, 9],
	"d": [45, 12, 100]
}
new_list = []

for values in my_dict.values():
    new_list.append(sum(values))

print(max(new_list))


## EXERCISE 39-45.8

s = "Hello World"
freq_dict = {}
for char in s.lower():
    if char.isalpha():
        if char not in freq_dict:
            freq_dict[char] = 1
        else:
            freq_dict[char] += 1

print(freq_dict)

## EXERCISE 39-45.10

my_dict = {
	"a": [4, 3, 2],
	"b": [5, 3, 7],
	"c": [1, 9, 10],
	"d": [3, 4, 1]
}

for values in my_dict.values():
    values.sort()

print(my_dict)

## EXERCISE 39-45.12

product_info = {
	"description": "shoe",
	"price": 4.56,
	"colors": ["green", "blue", "red"],
}
new_list = []
for key, values in product_info.items():
    new_list.append([key,values])

print(new_list)


## EXERCISE 45-50.2

num = -2

if num == 0:
    print("Zero")
elif num > 0:
    print("Positive")
else:
    print("Negative")


## EXERCISE 45-50.4

s = "Score: 36"

for char in s.lower():
    if char.isalpha():
        if char in "aeiou":
            print(char + " is a vowel")
        else:
            print (char + "  is a consonant")
    else:
        print(char + " is not a letter")


## EXERCISE 45-50.6

a = 1
b = 3
c = 4

print(max(a,b,c))

## EXERCISE 45-50.9
a = 1
b = 3
c = 4

print(min(a,b,c))


## EXERCISE 45-50.11

num_season = 4

if num_season == 1:
    print("Spring")
elif num_season == 2:
    print("Summer")
elif num_season == 3:
    print("Fall")
elif num_season == 4:
    print("Winter")
else:
    print("Please input a valid number")



## EXERCISE 45-50.13

a = 3
b = 3
c = 3

if a == b == c:
    print("Equal")
else:
    print("Not Equal")



## EXERCISE 51-56.1

month = "January"

months_with_31_days = ("January", "March", "May", "July", 
					"August", "October", "December")

months_with_30_days = ("April", "June", "September", "November")

if month in months_with_31_days:
    print(f"{month} have 31 days")
elif month in months_with_30_days:
    print(f"{month} have 30 days")
else:
    print(f"{month} have 28 days")



## EXERCISE 51-56.3

a = 1
b = 2
c = 3

if a < b < c:
    print("Increasing Order")
elif a > b > c:
    print("Decreasing Order")
else:
    print(None)



## EXERCISE 51-56.5

a = 3
b = 4
c = 5

if ((b**2) - 4*a*c) < 0:
    print("Complex Roots")
elif ((b**2) - 4*a*c) == 0:
    print((-b-((b**2)-4*a*c)**(1/2))/(2*a))
else:
    print((-b-((b**2)-4*a*c)**(1/2))/(2*a),(-b+((b**2)-4*a*c)**(1/2))/(2*a))


## EXERCISE 51-56.8

year = 2025

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")


## EXERCISE 51-56.10

#Add = 1
#Substract = 2
#Multiply = 3
#Divide = 4
#Integer_Division = 5
#Modulo = 6

#print("=== Welcome to your Interactive Python Calculator ===")

#a = int(input("Please enter the first value: "))
#b = int(input("Please enter the second value: "))

#print("Great! Now enter the operation.")
#print("These are the available options:")
#print("1 - Addition")
#print("2 -Subtraction")
#print("3 - Multiplication")
#print("4 - Division")
#print("5 - Integer Division")
#print("6 - Modulo")

#operation = int(input("--> Enter the corresponding integer: "))

#if operation == Add:
#    print(f"The result of {a} + {b} is {a+b}")
#elif operation == Substract:
#    print(f"The result of {a} - {b} is {a-b}")
#elif operation == Multiply:
#    print(f"The result of {a} * {b} is {a*b}")
#elif operation == Divide:
#    if b == 0:
#        print("Divisor cannot be 0. Please input a valid number")
#    else:
#        print(f"The result of {a} / {b} is {a/b}")
#elif operation == Integer_Division:
#    if b == 0:
#        print("Divisor cannot be 0. Please input a valid number")
#    else:
#        print(f"The result of {a} // {b} is {a//b}")
#elif operation == Modulo:
#    print(f"The result of {a} % {b} is {a%b}")
#else:
#    print("Please choose a valid operation")
    


## EXERCISE 51-56.12

import random

options = ("rock", "paper", "scissor")
computer = options[random.randint(0,2)]

print("====== Welcome to the game ======")
player = input("Please enter Rock, Paper, or Scissor below:\n")

if player.lower() == computer:
    print("It's a tie! Try again.")
elif (player.lower() == "rock" and computer == "scissor") or (player.lower() == "scissor" and computer == "paper") or (player.lower() == "paper" and computer == "rock"):
    print(f"You win! Your opponet chose '{computer.capitalize()}'.")
elif (player.lower() == "scissor" and computer == "rock") or (player.lower() == "paper" and computer == "scissor") or (player.lower() == "rock" and computer == "paper"):
    print(f"You lose! Your opponent chose '{computer.capitalize()}'.")
else:
    print("Please choose a valid option")



#EXERCISE 57-63.2


for i in range(1,16):
    print(i)


#EXERCISE 57-63.4

n = 10

for i in range(n,0,-1):
    print(i)


# EXERCISE 57-63.6

total = 0

for i in range(1,101):
    total += i

print(total)


# EXERCISE 57-63.8

n = 3

print("==== Multiplication Table of 3 ====")

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")


# EXERCISE 57-63.11

for i in range(65,91):
    print(chr(i))


# EXERCISE 57-63.13

for i in range(1,201):
    if i % 2 == 0:
        print(i)

number = 2
count = 0

while count < 100:
    print(number)
    number += 2
    count += 1


## EXERCISE 57-63.15

n = int(input("Input a number: "))
factorial_n = 1

for i in range(n,0,-1):
    factorial_n *= i

print(factorial_n)


## EXERCISE 64-71.1

prime_num = int(input("Input an Integer: "))
is_prime = True

if prime_num <= 1:
    print("Not Prime")
else:
    for i in range(2, int(prime_num**0.5) + 1):
        if prime_num % i == 0:
            is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not Prime")


## EXERCISE 64-71.3

n_pattern = int(input("Input number of rows here: "))


for i in range(1, n_pattern + 1):
    print("*"*i)


## EXERCISE 64-71.5

num = 352

reverse = int(str(num)[::-1])

print(reverse)


## EXERCISE 64-71.7

s = "Hello"
new_s = ""

for char in s[::-1]:
    new_s += char

print(new_s, end="")

print("")


## EXERCISE 64-71.10

n = int(input("Input a number here: "))

m = (2*n) - 2

for i in range(0,n):

    for k in range(0,m):
        print("", end=" ")

    m = m -2

    for k in range(0,i+1):
        print("*", end=" ")
           
    print("")

## EXERCISE 64-71.12

n = int(input("Enter the number of rows here: "))

count = 1

for i in range(1,n+1):
    for j in range(0, i):
        print(count,end=" ")
        count += 1

    print()

## EXERCISE 64-71.14

n = int(input("Enter number of rows here: "))
char_count = 65
for i in range(1,n+1):
    for j in range(0,i):
        print(chr(char_count),end=" ")

    char_count += 1

    print()


## EXERCISE 64-71.16

height = int(input("Enter diamond's height here: "))

if height % 2 == 0:
    print("Please enter an odd value for the height.")
else:
    middle_row = (height // 2) + 1

    for i in range(middle_row):
        print(" " * (middle_row - i), "*" * (i * 2 + 1))

    for i in range(middle_row - 2, -1, -1):
        print(" " * (middle_row - i), "*" * (i * 2 + 1))


## EXERCISE 72-76.2

def recursive_sum(numbers):

    if not numbers:
        return 0
    else:
        return numbers[0] + recursive_sum(numbers[1:])
    

numbers_list = [1,2,3]
result = recursive_sum(numbers_list)

print(result)


## EXERCISE 72-76.4

def fibonacci(f_n):
    # Base case: the first two numbers in the Fibonacci sequence
    if f_n == 0:
        return 0
    elif f_n == 1:
        return 1
    else:
        # Recursive case: Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
        return fibonacci(f_n-1) + fibonacci(f_n-2)
    
fn = 9
result = fibonacci(fn)
print(result)

## EXERCISE 72-76.6

def factorial(f):
    # Base case
    if f == 1 or f == 0:
        return 1
    # Recursive case
    else:
        return f * factorial(f - 1)


print(factorial(5))

## EXERCISE 72-76.9

def recursive_sum_of_digits(num):
    # Base case: if the number is a single digit
    if num == 0:
        return 0
    else:
        # Recursive case: sum the last digit and the sum of the rest
        return num % 10 + recursive_sum_of_digits(num // 10)
    
n = 1234
result = recursive_sum_of_digits(n)
print(result)

## EXERCISE 72-76.11

def power(a,b):
    if b == 0:
        return 1
    else:
        return a * power(a,b-1)

a_n = 2
b_n = 3
result = power(a_n,b_n)
print(result)


## EXERCISE 77-82.1

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
a_n = 42
b_n = 56
print(gcd(a_n,b_n))

## EXERCISE 77-82.3

def is_palindrome(s):
   s = s.replace(" ","").lower()

   return s == s[::-1]

word = input("Enter text here: ")
print(is_palindrome(word))

## EXERCISE 77-82.5

def vowel_count(s, index=0):
    if index == len(s):
        return 0
    else:
        count = 0
        vowels = "aeiou"
        if s[index].lower() in vowels:
            count += 1

    return count + vowel_count(s,index + 1)

word = input("Enter text here: ")
print(vowel_count(word))

## EXERCISE 77-82.8

def print_pattern(row):
    if row == 1:
        print("*")
    else:
        print("*" * row)
        print_pattern(row - 1)

print(print_pattern(4))

## EXERCISE 77-82.10

def dec_to_binary(dec):
    if dec == 0:
        return ""
    else:
        binary = ""
        if dec % 2 == 0:
            binary += "0"
        else:
            binary += "1"

    return dec_to_binary(dec//2) + binary

n = int(input("Enter decimal here: "))
print(dec_to_binary(n))

## EXERCISE 77-82.12

def binary_search(seq_list,low,high,target):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2

    if seq_list[mid] == target:
        return mid
    elif seq_list[mid] > target:
        return binary_search(seq_list,low,mid-1,target)
    else:
        return binary_search(seq_list,mid+1,high,target)
    
seq = [4,5,6,7]
el = 2
print(binary_search(seq,0,len(seq),5))



## EXERCISE 83-87.2

file_path = "basic_file.txt"
file_content = []

with open(file_path, encoding="utf-8") as file:
    for line in file:
        file_content.append(line)

print(file_content)

## EXERCISE 83-87.4

file_path = "basic_file.txt"

n = int(input("Enter number of lines to print: "))

with open(file_path, encoding="utf-8") as file:
    lines = file.readlines()
    n_lines = len(lines)

    if n > n_lines:
        print(f"Please enter a valid value. The file has {n_lines} lines.")
    else:
        for i in range(n):
            print(lines[i].strip("\n"))

## EXERCISE 83-87.7

file_path = "basic_file.txt"

n = int(input("Enter number of lines to print: "))

with open(file_path, encoding="utf-8") as file:
    lines = file.readlines()
    n_lines = len(lines)

    if n > n_lines:
       print(f"Please enter a valid value. The file has {n_lines} lines.")
    else:
        for i in lines[-n:]:
            print(i.strip("\n"))

## EXERCISE 83-87.9

file_path = "words.txt"
longest_word = ""

with open(file_path, encoding="utf-8") as file:
    lines = file.readlines()

    for word in lines:
        if len(word) > len(longest_word):
            longest_word = word

print(longest_word)

## EXERCISE 83-87.11

file_path = "words2.txt"

with open(file_path, encoding="utf-8") as file:
    lines = file.readlines()

    my_dict = {}

    for word in lines:
        word = word.strip("\n")
        if word not in my_dict:
            my_dict[word] = 1
        else:
            my_dict[word] += 1

print(my_dict)


## EXERCISE 88-91.1

file_path = "list_file.txt"

my_list = [1,2,3,4,5]


with open(file_path, "w", encoding="utf-8") as file:
    for i in my_list:
        file.write(str(i) + "\n")


## EXERCISE 88-91.3

file_path = "count_char.txt"
char_count = 0

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()
    
    for line in lines:
        line = line.strip("\n").replace(" ","")
        char_count += len(line)

print(char_count)


## EXERCISE 88-91.6

orig_file_path = "count_char.txt"
copy_file_path = "new_char.txt"
content = ""

with open(orig_file_path, "r", encoding="utf-8") as orig_file:
    for line in orig_file:
        content += line
    with open(copy_file_path, "w", encoding="utf-8") as copy_file:
        copy_file.write(content)

## EXERCISE 88-91.8

import os

file_path = "new_char.txt"

if os.path.exists(file_path):
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' doesn't exist.")


## EXERCISE 92-97.2

from datetime import datetime

print("Current Date and Time:")
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

## EXERCISE 92-97.4

seconds = int(input("Enter seconds here: "))

minute = int(seconds * (1/60))
hour = seconds * (1/3600)

print(f"{seconds} seconds is equivalent to\n{minute} Minutes\n{hour} Hours")

## EXERCISE 92-97.6

import math

d = float(input("Enter diameter here: "))

area = round(math.pi * (d/2)**2,2)

print(f"The area of a circle with diameter {d} is {area}")

## EXERCISE 92-97.9

b = float(input("Enter base here: "))
h = float(input("Enter height here: "))

if b <= 0 or h <=0:
    print("Please enter valid values for base and height.")
else:
    area = round((1/2)*b*h,2)

print(f"The area of the triangle with base: {b} and height: {h} is {area}.")

## EXERCISE 92-97.11

c_deg = float(input("Input temperature in Celcius: "))

con_result = (c_deg * (9/5)) + 32

print(f"{c_deg} Fahrenheit = {con_result} Celsius")

## EXERCISE 92-97.13

f_deg = int(input("Input temperature in Fahreinheit: "))

con_result = (f_deg -32) * 5/9

print(f"{f_deg} Fahrenheit = {con_result} Celsius")

## EXERCISE 98-101.1

kg = float(input("Enter weigt in kilograms: "))
h = float(input("Enter height in centimers: "))

bmi = round(kg / ((h/100)**2),2)

if bmi < 18.5:
    print(f"BMI is {bmi},Underweight")
elif 18.5 <= bmi <= 24.9:
    print(f"BMI is {bmi},Normal")
elif 25 <= bmi <=29.9:
    print(f"BMI is {bmi},Overweight")
else:
    print(f"BMI is {bmi},Obesity")

## EXERCISE 98-101.3

from calendar import month

in_month = int(input("Enter month here: "))
in_year = int(input("Enter year here: "))

print(month(in_year,in_month))

## EXERCISE 98-101.6

import datetime

first_date = input("Enter first date here (year month date ex. 2025 1, 1): ")
sec_date = input("Enter second date here (year month date ex. 2025 1, 1): ")

first_date_comps = first_date.split(" ")
sec_date_comps = sec_date.split(" ")

first_date_year = int(first_date_comps[0])
first_date_month = int(first_date_comps[1])
first_date_day = int(first_date_comps[2])

actual_first_date = datetime.date(first_date_year, first_date_month, first_date_day)

sec_date_year = int(sec_date_comps[0])
sec_date_month = int(sec_date_comps[1])
sec_date_day = int(sec_date_comps[2])

actual_sec_date = datetime.date(sec_date_year, sec_date_month, sec_date_day)

if actual_sec_date < actual_first_date:
    print("Please enter valid dates.")
elif actual_first_date == actual_sec_date:
    print("The dates are equal")
else:
    diff_days = (actual_sec_date - actual_first_date).days

    if diff_days == 1:
        print("There is 1 day between these dates.")
    else:
        print(f"There are {diff_days} days between these dates.")

## EXERCISE 98-101.8

import re

regex = "^My[\w\s]+blue$"

s = input("Enter a string to check if a match is found: ")

if re.search(regex, s):
    print("Match")  
else:  
    print("No Match")  


