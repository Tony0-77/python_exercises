# Exercise 1 - 8.2

s = "Python"

print(len(s))

# Exercise 1 - 8.4

num = "ss"
i = 23

if len(num) == 0:
    print("Empty String")
elif i > len(num):
    print("i is out of range")
else:
    print(num[i])

# Exercise 1 - 8.6

exer6 = 'JetHRo'

print(exer6[::-1])

# Exercise 1 - 8.8

s = 'Amazing'

if len(s) > 6:
    print(s[:3] + s[-3:])
else:
    print("")

# Exercise 1 - 8.11

s = 'Jethro'

if len(s) > 1:
    print(s[1::2])
else:
    print(s)

# Exercise 1 - 8.14

s = "Jethr05"

print(s.isdigit())

# Exercise 1 - 8.15

s = 'WOrld'
n = 3

if (len(s) == 0) or (n >= len(s)):
    print(s)
else:
    print(s[:n] + s[n+1:])

# Exercise 1 - 8.15

s = 'Python'
curr_char = 'p'
new_char = 'a'

x = s.replace(curr_char,new_char) if curr_char in s else s
print(s)

# Exercise 9 - 16.1

s = 'Hello, World!'

print(s.replace(',','.'))

# Exercise 9 - 16.3

import string
s = 'The quick brown fox jumps over the lazy dog'

x = set(s.lower().replace(' ','')) == set(string.ascii_lowercase)

print(x)

# Exercise 9 - 16.5

s = 'Python'

x = s if ' ' not in s else s.replace(' ', '')
print(x)

# Exercise 9 - 16.7

s = 'Hello'
prefix = 'He'

x = False if len(prefix) > len(s) else s[:len(prefix)] == prefix
print(x)

# Exercise 9 - 16.9

s = 'Coding'
suffix = 'eng'

print(s[-len(suffix):] == suffix)

# Exercise 9 - 16.12

s = 'Hello World'

x = ''.join([new.lower() if new.isupper() else new.upper() for new in s])
reverse = [i[::-1] for i in x.split()]
print(' '.join(reverse))

# Exercise 9 - 16.14

s = 'JhteJethroooo'

count = 0
repeated_letter = []

for i in s:
    if s.count(i)>1:
        if i not in repeated_letter:
            repeated_letter.append(i)
            count += 1
print(count)
if len(repeated_letter) == 0:
    print(None)
else:
    print(*repeated_letter, sep=' ')

# Exercise 9 - 16.16

s = 'Wonderful World'

reverse = [''.join(sorted(i[::-1].lower())) for i in s.split()]
print(' '.join(reverse))


# Exercise 17 - 24.2

l = [3,4,5,6]
l2 = ['a','b','c']
factor = 3

result = [x*factor for x in l2]

print(result)

# Exercise 17 - 24.4

l = [3,4,5,6]
l2 = ['a','b','c']

print(*l2)

# Exercise 17 - 24.6

l = [3,4,5,6]

if l:
    print(max(l), min(l))
else:
    print(None)
     
# Exercise 17 - 24.8

l = [4]

result = "Not Empty" if l else "Empty"

print(result)

# Exercise 17 - 24.11

l = ['a','b','c','d']

if l:
    for i, value in enumerate(l):
        print(value, i)
else:
    print("Empty List")

# Exercise 17 - 24.13

l = [1,2,3,4]
to_remove = 2

if not l:
    print("Empty List")
elif l.count(to_remove) == 0:
    print("Not Found")
else:
    for i in range(l.count(to_remove)):
        l.remove(to_remove)
print(l)

# Exercise 17 - 24.15

l = [1,1,2,2,3,4,4]

print(list(set(l)))

# Exercise 17 - 24.17

l = [7,8,9,10]

counter = sum(1 for i in l if i > 3)

print(counter)

# Exercise 25 - 32.1

list_a = [1,2,3,4]
list_b = [1,2,3]

if not list_a or list_a == list_b:
    print([])
else:
    print(list(set(list_a)-set(list_b)))

# Exercise 25 - 32.3

import math

pointA = [3,4,5]
pointB =[1,3,5]

ab = math.sqrt(
    math.pow(pointB[0]-pointA[0],2) + 
    math.pow(pointB[1]-pointA[1],2) + 
    math.pow(pointB[2]-pointA[2],2)
    )

print(ab)

# Exercise 25 - 32.5

pointA = [6,4,5]
pointB =[1,2,3]

print(list(set(pointA) & set(pointB)))

# Exercise 25 - 32.7

listA = []

listA.sort(reverse=True)

if not listA or len(listA) == 1:
    print(None)
else:
    print(listA[1])

# Exercise 25 - 32.10

listA = []
listA.sort()

if not listA or len(listA) == 1:
    print(None)
else:
    print(listA[1])

# Exercise 25 - 32.12

listA = ['a','a','b','c','a','b']
my_dict = {}

for i in listA:
    my_dict[i] = listA.count(i)

print(my_dict)


# Exercise 25 - 32.14

listA = [[1,2,3],[4,5,6],[7,8,9]]

flattened = []
for i in listA:
    flattened.extend(i)

print(flattened)

# Exercise 25 - 32.16

from itertools import permutations

listA = [1,2,3]

for i in permutations(listA):
    print(i)

# Exercise 33 - 38.2

my_dict = {
    'a':4,
    'b':6
}
KEY = 'c'

result = True if KEY in my_dict.keys() else False

print(result)

# Exercise 33 - 38.4

my_dict = {
    'January':45,
    'February':56,
    'March':67
}
KEY_VALUE_PAIR = {
    'January':67
}

key_to_check = list(KEY_VALUE_PAIR.keys())[0]

if key_to_check not in my_dict:
    my_dict.update(KEY_VALUE_PAIR)
    
print(my_dict)

# Exercise 33 - 38.4

my_dict1 = {'a':1,'b':2,'c':3}
my_dict2 = {'c':4,'d':6,'e':8}

final_dict = my_dict1 | my_dict2

print(final_dict)


# Exercise 33 - 38.9

my_dict1 = {}

values = set([ i for i in list(my_dict1.values())])
if not my_dict1:
    print("Empty")
elif len(values) > 1:
    print(False)
else:
    print(True)

# Exercise 33 - 38.11

my_dict1 = {'a':4,'b':4}

if not my_dict1:
    values = max([ i for i in list(my_dict1.values())])
    print(values)
else:
    print(None)

# Exercise 33 - 38.11

if not my_dict1:
    values = min([ i for i in list(my_dict1.values())])
    print(values)
else:
    print(None)

# Exercise 39 - 44.1

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

freq_dict = {

}

for key,value in my_dict.items():
    freq_dict[value] = list(my_dict.values()).count(value)
print(freq_dict)

# Exercise 39 - 44.3

my_list = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]

freq_dict = {

}

for i in my_list:
    freq_dict[i[0]] = i[1]

print(freq_dict)

# Exercise 39 - 44.5

my_dict = {
	"a": [1, 2, 3],
	"b": [4, 0, -4],
	"c": [3, 5, 9],
	"d": [45, 12, 100]
}

highest_value = max([sum(values) for key,values in my_dict.items()])

print(highest_value)

# Exercise 39 - 44.8

s = 'Hello, World'
modified_s = s.lower()

output_dict = {

}

for i in modified_s:
    if i in [',', ' ']:
        continue
    output_dict[i] = modified_s.count(i)

print(output_dict)

# Exercise 39 - 44.10

my_dict = {
	"a": [4, 3, 2],
	"b": [5, 3, 7],
	"c": [1, 9, 10],
	"d": [3, 4, 1]
}

for key, values in my_dict.items():
    values.sort()
    my_dict[key] = values

print(my_dict)

# Exercise 39 - 44.12

product_info = {
	"description": "shoe",
	"price": 4.56,
	"colors": ["green", "blue", "red"],
}

my_list = [ [key ,values] for key,values in product_info.items()]
print(my_list)

# Exercise 45 - 50.2

num = 0

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
    
# Exercise 45 - 50.4

s = 'Score: 36'
vowel = 'aeiou'

for i in s.lower():
    if i in vowel:
        print(f'{i} is a vowel')
    else:
        if i.isalpha():
        	print(f'{i} is a consonant')
        else:
             print(f'{i} is not a letter')

# Exercise 45 - 50.6

a = 1
b = 3
c = 4

print(max(a,b,c))

# Exercise 45 - 50.9

a = 1
b = 3
c = 4

print(min(a,b,c))

# Exercise 45 - 50.11

season_num = 4

match season_num:
    case 1:
        print('Spring')
    case 2:
        print('Summer')
    case 3:
        print('Fall')
    case 4:
        print('Winter')

# Exercise 45 - 50.13

a = 1
b = 2
c = 3

result = "Equal" if a == b == c else "Not Equal"

print(result)

# Exercise 51 - 56.1

MONTH = "February"
days_31 = ["January", "March", "May", "July", "August", "October", "December"]
days_30= ["April", "June", "September", "November"]

if MONTH in days_31:
    print(f"{MONTH} has: 31 days")
elif MONTH in days_30:
    print(f"{MONTH} has: 30 days")
else:
    print(f"{MONTH} has: 28 days")


# Exercise 51 - 56.3

a = 1
b = 2
c = 3

if a > b > c:
    print('Decreasing Order')
elif a < b < c:
    print('Increasing Order')
else:
    print('None')

# Exercise 51 - 56.5

import math

a = 2
b = 5
c = -3

discriminant = abs(math.pow(b,2) - 4*a*c)

positive_form = (-b + math.sqrt(discriminant)) / (2*a)
negative_form = (-b - math.sqrt(discriminant)) / (2*a)

print(negative_form, positive_form)

# Exercise 51 - 56.8

year = 2033

if year % 4 == 0 and year % 100 != 0:
    print(f'{year} is a leap year')  
elif year % 4 != 0:
    print(f'{year} is not a leap year')

# Exercise 51 - 56.10

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

operation = int(input('--> Enter the corresponding integer: '))

match operation:
    case 1:
        result = a + b
        print(f'The result of {a} + {b} is: {result}')
    case 2:
        result = a - b
        print(f'The result of {a} - {b} is: {result}')
    case 3:
        result = a * b
        print(f'The result of {a} * {b} is: {result}')
    case 4:
        result = a / b
        print(f'The result of {a} / {b} is: {result}')
    case 5:
        result = a // b
        print(f'The result of {a} // {b} is: {result}')
    case 6:
        result = a % b
        print(f'The result of {a} % {b} is: {result}')

# Exercise 51 - 56.12

import random

hand = ['Rock','Paper','Scissor']

computer_answer = hand[random.randint(0,2)]
print('====== Welcome to the game ======')
human_answer = input('Please enter Rock, Paper, or Scissors below:')

if human_answer.lower() == computer_answer.lower():
    print("It's a tie! Try again.")
elif human_answer.lower() == 'rock':
    if computer_answer.lower() == 'paper':
        print(f"You lose! Your opponent chose '{computer_answer}'")
    else:
        print(f"You win! Your opponent chose '{computer_answer}'")
elif human_answer.lower() == "paper":
    if computer_answer.lower() == "scissors":
        print(f"You lose! Your opponent chose '{computer_answer}'")
    else:
        print(f"You win! Your opponent chose '{computer_answer}'")
elif human_answer.lower() == "scissors":
    if computer_answer.lower() == "rock":
        print(f"You lose! Your opponent chose '{computer_answer}'")
    else:
        print(f"You win! Your opponent chose '{computer_answer}'")
else:
    print("Please enter a valid option.")

# Exercise 57 - 63.2

for i in range(1,16):
    print(i)

# Exercise 57 - 63.4

number = int(input('Enter a number: '))
for i in range(number,0,-1):
    print(i)

# Exercise 57 - 63.6

summation = sum([i for i in range(101)])
print(summation)

# Exercise 57 - 63.8

num = 3
for i in range(1,11):
    product = num * i
    print(f'{num} x {i} = {product}')

# Exercise 57 - 63.11

for i in range(65,91):
    converted = chr(i)
    print(converted)

# Exercise 57 - 63.13

for i in range(2,201,2):
    print(i)

# Exercise 57 - 63.15

num = 4
factorial = 1
for i in range(1,num+1):
    factorial *= i
print(factorial)
    
# Exercise 64 - 71.1

num = 3

if num in [0,1]:
	print("Not Prime")
else:
	for i in range(2, num):
		if num % i == 0:
			print("Not Prime")
			break
	else:
		print("Prime")

# Exercise 64 - 71.3

num = int(input('Enter a integer to determine number of rows: '))

for i in range(num+1):
    print('* '* i)

# Exercise 64 - 71.5

num = 3456

print(int(str(3456)[::-1]))

# Exercise 64 - 71.7

s = 'Hello'

reverse =''.join([s[i] for i in range(len(s)-1,-1,-1)])

print(reverse)

# Exercise 64 - 71.10

num = 5

for i in range(1, num + 1):
    print(" " * (2 * (num - i)) + " ".join("*" * i))


# Exercise 64 - 71.12

n = int(input("Enter a integer for Floyd's Triangle: "))
num = 1
	
for i in range(n+1):
	for j in range(i):
		print(num, end=' ')
		num += 1
	print()

# Exercise 64 - 71.14

n = int(input("Enter a integer for number of rows: "))
	
for i in range(n+1):
	for j in range(i):
		print(chr(64+i), end=' ')
	print()

# Exercise 64 - 71.14

height = int(input("Enter the height (an odd number): "))

if height % 2 == 0:
    print("Please enter an odd value for the height (number of rows).")
else:
    mid = (height + 2) // 2

    for i in range(mid):
        print(" " * (mid - i), "*" * (i*2 + 1))

    for i in range(mid-2, -1, -1):
        print(" " * (mid - i), "*" * (i*2 + 1))


# Exercise 72 - 76.2

def recursive_sum(num):
    if not num:
        return 0 
    return num[0] + recursive_sum(num[1:])

number = [1,2,3]
print(recursive_sum(number))

# Exercise 72 - 76.4

def fibonacci(n):
    if n == 0:
        return 0
    
    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)

fib = fibonacci(9)
print(fib)

# Exercise 72 - 76.6

def factorial(num:int):
    if num in [0,1]:
        return 1
    else:
    	return (num * factorial(num-1))
    
num = 5
print(factorial(5))


# Exercise 72 - 76.9

def sum_of_digits(num):
    if num < 10:
        return num
    else:
        return (num % 10) + sum_of_digits(num//10)
    
print(sum_of_digits(1234))

# Exercise 72 - 76.11

def power(a,b):
    if b == 0:
        return 1
    else:
        return (a*power(a,b-1))

print(power(2,3))

# Exercise 77 - 82.1
def greatest_common_divisor(a, b):
	if b == 0:
		return a
	else:
		return greatest_common_divisor(b, a % b)
	
print(greatest_common_divisor(60,48))

# Exercise 77 - 82.3

def palindrome(s:str):
     if len(s) <= 1:
          return True
     elif s.lower()[0] != s.lower()[-1]:
          return False
     else:
          return palindrome(s[1:-1])
     
print(palindrome('Anna'))

# Exercise 77 - 82.5

def count_vowel(s:str):
    vowels = 'aeiou'
    if not s or (len(s) < 2 and s not in vowels):
        return 0
    elif len(s) < 2 and s in vowels:
        return 1
    elif s[0] in vowels:
        return 1 + count_vowel(s[1:])
    else:
        return count_vowel(s[1:])
print(count_vowel('Python'))

# Exercise 77 - 82.8

def pattern(n):
	if n == 1:
		print("*")
	else:
		print("*" * n)
		pattern(n-1)

pattern(5)

# Exercise 77 - 82.10

def dec_to_bin(num):
    if num == 0:
        return 0
    else:
        return (str(dec_to_bin(num // 2)) + str(num % 2)).lstrip('0')

print(dec_to_bin(13))

# Exercise 77 - 82.12

def binary_search(array,element,low, high):
	if high >= low:
		mid = (low + high) // 2
		if array[mid] == element:
			return mid
		elif array[mid] > element:
			return binary_search(array,element,low,mid-1)
		else:
			return binary_search(array,element,mid+1,high)

arr = [4,5,6,7]
element = 7
print(binary_search(arr,element,0,len(arr)-1))

# Exercise 83 - 87.2

FILE_PATH = '2.1 basic_file.txt'

with open(FILE_PATH) as file:
    content = file.readlines()
    print(content)

# Exercise 83 - 87.4

FILE_PATH = '2.1 basic_file.txt'

with open(FILE_PATH) as file:
    content = file.readlines()
    num = int(input(f"Please enter a value for n. The file has {len(content)} lines: "))

    for i in range(num):
        print(content[i].strip('\n '))

# Exercise 83 - 87.7

FILE_PATH = '2.1 basic_file.txt'

with open(FILE_PATH) as file:
    content = file.readlines()
    num = int(input(f"Please enter a value for n. The file has {len(content)} lines: "))
    
    if num > len(content):
            print('Out of range')
    else:
        for i in range(num):
        	print(content[i+num].strip('\n '))

# Exercise 83 - 87.9

FILE_PATH = '12.1 words.txt'

longest = ''
with open(FILE_PATH) as file:
	for word in file:
		if len(word) > len(longest):
			longest = word

print(longest) 

# Exercise 83 - 87.11

FILE_PATH = '12.1 words.txt'

with open(FILE_PATH) as file:
    content = file.readlines()
    clean_list = [i.strip('\n') for i in content]
    my_dict = {word:clean_list.count(word) for word in clean_list}
    print(my_dict)

# Exercise 88 - 91.1

FILE_PATH = 'Exercise 88 - 91.1.txt'
my_list = [1,2,3,4,5]

with open(FILE_PATH, 'w') as file:
    content = ''
    for i in my_list:
        content += str(i) + '\n'
    file.write(content)

# Exercise 88 - 91.3

FILE_PATH = 'Exercise 88 - 91.3.txt'

with open(FILE_PATH) as file:
    content = file.readlines()
    total_char = sum([len(i.strip('\n').replace(' ','')) for i in content])
    print(total_char)

# Exercise 88 - 91.6

FILE_PATH = 'Exercise 88 - 91.6.txt'

with open(FILE_PATH) as file:
    content = file.read()

    with open('Exercise 88 - 91.6 - copy', 'w') as copy:
        copy.write(content)

# Exercise 88 - 91.8

from os import path

FILE_NAME = 'favorite_book.txt'

result = path.isfile(FILE_NAME)
if result:
	print(f'The file {FILE_NAME} exists')
else:
	print(f"The file {FILE_NAME} doesn't exists")
     
# Exercise 92 - 97.2

from datetime import datetime

datetime_now = datetime.now()
print('Current Date and Time:')
print(datetime_now.strftime("%Y-%m-%d %H:%M:%S"))

# Exercise 92 - 97.4
from datetime import datetime

SECONDS = 5400
MINUTES = SECONDS // 60
HOUR = MINUTES / 60

print(f'{SECONDS} seconds is equivalent to:')
print(f'{MINUTES} Minutes')
print(f'{HOUR} Hours')

# Exercise 92 - 97.6

import math
d = int(input('Provide a diameter to form a circle: '))

area = math.pi*(math.pow(d/2,2))
print(round(area,2))

# Exercise 92 - 97.9

try:
    b = int(input('Provide the base to form a triangle: '))
    h = int(input('Provide the height to form a triangle: '))
    area = (b * h) / 2
    print(area)
except ValueError:
    print("Please enter valid values for base and height")

# Exercise 92 - 97.11

c = int(input('Enter Celsius to convert: '))

f = (c * (9/5)) + 32
print(f'{c} Celsius = {f} Fahrenheit')

# Exercise 92 - 97.13

f = int(input('Enter Fahrenheit to convert: '))

c = (f - 32) * (5 / 9)
print(f'{f} Fahrenheit = {c} Celsius')

# Exercise 98 - 101.1

h = int(input('Enter height in centimeters: '))
w = int(input('Enter weight in kilograms: '))

bmi = round(w / (h/100)**2, 2)

if bmi < 18.5:
	print(bmi, 'Underweight')
elif bmi > 18.5 and bmi < 24.9:
	print(bmi, 'Normal ')
elif bmi > 25 and bmi < 29.9:
	print(bmi, 'Overweight  ')
else:
	print(bmi, 'Obesity')
     
# Exercise 98 - 101.3

import calendar
try:
    year = int(input('Enter a year: '))
    month = int(input('Enter a month in number: '))
    if month not in range(1,13):
	    print('Month out of range')
    print(calendar.month(year,month))
except ValueError: 
      print('Invalid input. Input positive integer only')

# Exercise 98 - 101.6

import datetime

d1 = input("Enter the first date: ")
d2 = input("Enter the second date: ")

d1_list = d1.split(" ")
year1 = int(d1_list[0])
month1 = int(d1_list[1])
day1 = int(d1_list[2])

date1_obj = datetime.date(year1, month1, day1)

d2_list = d2.split(" ")
year2 = int(d2_list[0])
month2 = int(d2_list[1])
day2 = int(d2_list[2])

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

# Exercise 98 - 101.8

import re

regex = "^My[\w\s]+blue$"

s = input('Enter a string to check: ')

if re.search(regex, s):
    print("Match")  
else:  
    print("No Match")  
