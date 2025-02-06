##exercise 1-8.2
s = 'Python'
if not s:
    print("")
else:
    print(len(s))

##exercise 1-8.4
s = 'Python'
i = 2
if not s:
    print("")
elif i <= len(s):
    print(s[2])
else:
    print(s)

##exercise 1-8.6
s = 'Python'
print(s[::-1])

##exercise 1-8.8
s = 'PythonExercises'
if len(s) < 5:
    print("")
else:
    print(f"{s[:1]}{s[-3:]}")

##exercise 1-8.11
s = 'PythonExercises'
output = [s[i] for i in range(len(s)) if (i + 1) % 2 == 0]
print(''.join(output))

##exercise 1-8.13
s = '123Python'
print(s.isdigit())

##exercise 1-8.15
s = '123Python'
i = 5
if not s:
    print("")
elif i <= len(s):
    print(s.replace(s[i], ''))
else:
    print(s)

##exercise 1-8.17
s = '123Python'
curr_char = 't'
new_char = 'g'

print(s.replace(curr_char, new_char))

##exercise 9-16.1
s = '123,Py,th,on'
print(s.replace(',', '.'))

##exercise 9-16.3
import string

s = 'abcdefghi  jklmnopqrstuvwxyz'
set_s = set(s.lower().replace(" ", ""))
print(set_s == set(string.ascii_lowercase))

##exercise 9-16.5
s = 'I love python'
print(s.replace(" ", ""))

##exercise 9-16.7
s = 'Python'
prefix = 'Py'
if not prefix or not s or (len(prefix) > len(s)):
    print(False)
else:
    print(s[:len(prefix)] == prefix)

##exercise 9-16.9
s = 'Python'
suffix = 'thon'
if not suffix or not s or (len(suffix) > len(s)):
    print(False)
else:
    print(s[-len(suffix):] == suffix)

##exercise 9-16.12
s = 'Python is Wows'
reversed_s = [i[::-1].swapcase() for i in s.split(" ")]
print(" ".join(reversed_s))

##exercise 9-16.14
s = 'Python'
repeated_str = []
for i in s:
    if s.count(i) >= 2:
        repeated_str.append(i)
repeated_str = sorted(set(repeated_str))
print(len(repeated_str))
print('None' if reversed_s else " ".join(repeated_str))

##exercise 9-16.16
s = 'Hello World'
reversed_s = ["".join(sorted(i[::-1].lower())) for i in s.split(" ")]
print(" ".join(reversed_s))

##exercise 17-24.2
myList = ['a', 2, 'cb']
factor = 2
output = [(x * factor) for x in myList]
print(output)

##exercise 17-24.4
myList = [3, 4, 5, 6, "a"]
print(*myList, sep=" ")

##exercise 17-24.6
myList = [3, 4, 5, 6, -4]
print(max(myList), min(myList), sep=" ")

##exercise 17-24.8
myList = [1]
if myList:
    print('Not empty')
else:
    print('Empty')

##exercise 17-24.11
myList = [3, 4, 5, 6, 'a']
if not myList:
    print("Empty List")
else:
    for index, item in enumerate(myList):
        print(item, index, sep=" ")

##exercise 17-24.13
myList = [3, 4, 5, 6, -4, 5]
elem_to_remove = 5
if not myList:
    print("Empty List")
elif elem_to_remove not in myList:
    print('Not found')
else:
    myList = set(myList)
    myList.remove(elem_to_remove)
    print(list(myList))

##exercise 17-24.15
myList = ['a', 5, 'a', -4, 5]
print(list(set(myList)))

##exercise 17-24.17
myList = [2, 5, -1, -4, 5]
newList = [i for i in myList if i > 3]
print(len(newList))

##exercise 25-32.1
listA = []
listB = [1, 2, 3, 4]
output = [i for i in listA if i not in listB]
print(output)

##exercise 25-32.3
import math
pointA = [3, 4, 5]
pointB = [1, 3, 5]
distance = (pointA[0] - pointB[0])**2 + \
            (pointA[1] - pointB[1])**2 + \
            (pointA[2] - pointB[2])**2
print(math.sqrt(distance))

##exercise 25-32.5
pointA = [3, 4, 5]
pointB = [1, 3, 5]
print(list(set(pointA) & set(pointB)))

##exercise 25-32.7
myList = [3, 4, 5, 6, 6]
if len(myList) <= 1:
    print('None')
else:
    second_largest = sorted(list(set(myList)), reverse=True)[1]
    print(second_largest)

##exercise 25-32.10
myList = [3, 4, 5, 6, 6]
if len(myList) <= 1:
    print('None')
else:
    second_largest = sorted(list(set(myList)))[1]
    print(second_largest)

##exercise 25-32.12
myList = [3, 4, 5, 6, 6, 1, 1]
myDict = {}
for i in myList:
    myDict[i] = myList.count(i)

print(myDict)

##exercise 25-32.14
myList = [[3, 4, 5], [6, 6, 1], 1]
flatList = []
for i in myList:
    if isinstance(i, list):
        for nested in i:
            flatList.append(nested)
    else:
        flatList.append(i)
print(flatList)

##exercise 25-32.16
import itertools
myList = [3, 4, 5]
permutations = list(itertools.permutations(myList))
print(permutations)

##exercise 33-38.2
myDict = {
    'a': 4,
    'b': 6
}
key = 'a'
print(key in myDict.keys())

##exercise 33-38.4
myDict = {
    'a': 4,
    'b': 6
}
new_key = 'April'
new_value = 67
if new_key not in myDict.keys():
    myDict[new_key] = new_value
print(myDict)

##exercise 33-38.6
myDict1 = {
    'a': 4,
    'b': 6
}
myDict2 = {
    'c': 4,
    'a': 6
}
myDict1.update(myDict2)
print(myDict1)

##exercise 33-38.9
myDict = {
    'a': 4,
    'b': 4,
    'c': 4
}
if not myDict:
    print('Empty')
else:
    set_myDict = set(myDict.values())
    print(len(set_myDict) == 1)

##exercise 33-38.11
myDict = {
    'a': 4,
    'b': 6,
    'c': 4
}
if not myDict:
    print('None')
else:
    max_val = max(myDict.values())
    print(max_val)

##exercise 33-38.13
myDict = {}
if not myDict:
    print('None')
else:
    max_val = min(myDict.values())
    print(max_val)

##exercise 39-44.1
myDict = {
    'a': 4,
    'b': 6,
    'c': 4,
    'd': 2
}
dict_values = list(myDict.values())
freq_dict = {}
for i in dict_values:
    freq_dict[i] = dict_values.count(i)
print(freq_dict)

##exercise 39-44.3
my_list = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]
has_nested = len([1 for i in my_list if isinstance(i, list)]) >= 1
my_dict = {}
if not has_nested:
    print({})
else:
    for item in my_list:
        my_dict[item[0]] = item[1]
print(my_dict)

##exercise 39-44.5
my_dict = {
	"a": [1, 2, 3],
	"b": [4, 0, -4],
	"c": [3, 5, 9],
	"d": [45, 12, 100]
}
dict_sum = [sum(values) for values in my_dict.values()]
print(max(dict_sum))

##exercise 39-44.8
s = 'Hello World'
my_dict = {}
lower_s = s.lower()
for i in lower_s:
    my_dict[i] = lower_s.count(i)
print(my_dict)

##exercise 39-44.10
my_dict = {
	"a": [4, 3, 2],
	"b": [5, 3, 7],
	"c": [1, 9, 10],
	"d": [3, 4, 1]
}
for key, val in my_dict.items():
    val.sort()
    my_dict[key] = val
print(my_dict)

##exercise 39-44.12
product_info = {
	"description": "shoe",
	"price": 4.56,
	"colors": ["green", "blue", "red"],
}
my_list = [[key, val] for key, val in product_info.items()]
print(my_list)

##exercise 45-50.2
num = -1
if num < 0:
    print('Negative')
elif num == 0:
    print('Zero')
else:
    print('Positive')

##exercise 45-50.4
s = 'Score: 36'
vowels = 'aeiouAEIOU'
if not s:
    print('Empty String')
else:
    for i in s.lower():
        if not i.isalpha():
            print(f"{i} is not a letter")
        elif i in vowels:
            print(f"{i} is a vowel")
        else:
            print(f"{i} is a consonant")

##exercise 45-50.6
numbers = (1, 3, 4)
print(max(numbers))

##exercise 45-50.9
numbers = (-1, 3, 4)
print(min(numbers))

##exercise 45-50.11
season_num = 3
if not isinstance(season_num, int) or not season_num or season_num > 4 or season_num < 1:
    print('Please enter a valid number')
else:
    if season_num == 1:
        print('Spring')
    elif season_num == 2:
        print('Summer')
    elif season_num == 3:
        print('Fall')
    else:
        print('Winter')

##exercise 45-50.6
numbers = (3, 3, 3)
a, b, c = numbers
print(a is b is c)

##exercise 51-56.1
import calendar
year = 2025
name_months = list(calendar.month_name)[1:]
for i in range(len(name_months)):
    num_of_days = calendar.monthrange(year, i + 1)[1]
    print(name_months[i], num_of_days)

##exercise 51-56.3
numbers = (4, 3, 2)
a, b, c = numbers
if a > b and b > c:
    print('Decreasing Order')
elif c > b and b > a:
    print('Increasing Order')
else:
    print('None')

##exercise 51-56.5
import math
numbers = (2, 5, -3)
a, b, c = numbers
discriminant = b**2 - (4*a*c)
if discriminant < 0:
    print('Complex Roots')
elif discriminant == 0:
    root = -b / (2*a)
    print(root)
else:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(root2, root1)

##exercise 51-56.8
import calendar
year = 1912
if calendar.isleap(year):
    print('Yes')
else:
    print('No')

##exercise 51-56.10
ADD = 1
SUBTRACT = 2
MULT = 3
DIV = 4
INT_DIV = 5
MOD = 6

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

if operation == ADD:
	result = a + b
	print(f"The result of {a} + {b} is: {result}")
elif operation == SUBTRACT:
	result = a - b
	print(f"The result of {a} - {b} is: {result}")
elif operation == MULT:
	result = a * b
	print(f"The result of {a} * {b} is: {result}")
elif operation == DIV:
	if b == 0:
		print("Division by Zero. Please enter another value for b.")
	else:
		result = a / b
		print(f"The result of {a} / {b} is: {result}")
elif operation == INT_DIV:
	if b == 0:
		print("Division by Zero. Please enter another value for b.")
	else:
		result = a // b
		print(f"The result of {a} // {b} is: {result}")
elif operation == MOD:
	result = a % b
	print(f"The result of {a} % {b} is: {result}")
else:
	print("Please choose a valid operation.")
     
##exercise 51-56.12
import random
rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
computer = random.choice([rock, paper, scissors])
print('====== Welcome to the game ======')
player = input('Please enter Rock, Paper or Scissors below:\n')
if not isinstance(player, str):
    'Invalid value, Please restart the game!'
else:
    player = player.capitalize()
    if player == computer:
        print('It\'s a tie! Try again.')
    elif (player == rock and computer == scissors) or\
        (player == paper and computer == rock) or\
        (player == scissors and computer == paper):
        print(f'You win! Your opponent chose \'{computer.capitalize()}\'')
    else:
        print(f'You lose! Your opponent chose \'{computer.capitalize()}\'')

##exercise 57-63.2
for i in range(1, 16):
    print(i)

##exercise 57-63.4
num = int(input('Enter n: '))
for i in range(num, 0, -1):
    print(i)

##exercise 57-63.6
num = 0
for i in range(1, 101):
    num += i
print(num)

##exercise 57-63.8
num = 3
for i in range(1, 11):
    product = num*i
    print(f'{num} x {i} = {product}')

##exercise 57-63.11
import string
for i in string.ascii_uppercase:
    print(i)

##exercise 57-63.11
counter = 0
n = 1
while counter < 100:
    if n % 2 == 0:
        counter += 1
        print(n)
    n += 1

##exercise 57-63.15
n = int(input('Enter n: '))
factorial = 1
if n == 0:
    print('1')
else:
    for i in range(1, n + 1):
        factorial *= i
    print(factorial)

##exercise 64-71.1
num = 17
if not isinstance(num, int):
    print('Invalid number')
elif num == 0 or num == 1:
    print('Not Prime')
else:
    for i in range(2, num):
        if num % i == 0:
            print('Not Prime')
            break
    print('Prime')

##exercise 64-71.3
n = 5
for i in range(1, n + 1):
    print('* ' * i)

##exercise 64-71.5
num = 3456
string_num = str(num)
print(string_num[::-1])

##exercise 64-71.7
s = 'Python'
for i in range(len(s) - 1, -1, -1):
    print(s[i], end="")
print("")

##exercise 64-71.10
n = 3
for i in range(1, n + 1):
    print("  " * (n-i), sep="", end="")
    print('* ' * i, sep="")

##exercise 64-71.12
rows = 3
num = 1
for i in range(1, rows + 1):
    for k in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()

##exercise 64-71.14
import string
letters = string.ascii_uppercase
rows = 3
for i in range(1, rows + 1):
    for k in range(i):
        print(letters[i - 1], end=" ")
    print()

##exercise 64-71.16
n = 7
rows = n // 2
if n % 2 == 0:
    print("Number can only be odd")
else:
    for i in range(1, rows + 1):
        print("  " * (rows-i + 1), sep="", end="")
        print('* ' * ((i * 2) - 1), sep="")
    print('* ' * n)
    for k in range(rows, 0, -1):
        print("  " * (rows-k + 1), sep="", end="")
        print('* ' * ((k * 2) - 1), sep="")

##exercise 72-76.2
numbers = [4, 5, 6]
index = 0
sum_recursive = 0
while index < len(numbers):
    sum_recursive += numbers[index]
    index += 1
print(sum_recursive)

##exercise 72-76.4
n = 9
def fibonacci_seq(number: int = 0) -> int:
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci_seq(number - 1) + fibonacci_seq(number - 2)
print(fibonacci_seq(n))

##exercise 72-76.6
n = 8
def factorial(number: int = 0) -> int:
    if number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        return number * factorial(number - 1)
print(factorial(n))

##exercise 72-76.9
n = 3726
def sum_digits(number: int) -> int:
    if number == 0:
        return 0
    return number % 10 + sum_digits(number // 10)
print(sum_digits(n))

##exercise 72-76.11
a = 3
b = 2
def power(a: int, b: int) -> int:
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)
print(power(2, 3))

##exercise 77-82.1
a = 60
b = 48
def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(gcd(a, b))

##exercise 77-82.3
s = 'Hello'
def is_palindrome(s: str = None) -> bool:
    if not s:
        return True
    else:
        s = s.replace(" ", "").lower()
    return s == s[::-1]
print(is_palindrome(s))

##exercise 77-82.5
s = 'Amazing'
def count_vowels(s: str):
    vowels = 'aeiouAEIOU'
    if not s:
        return 0
    elif s[0] in vowels:
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])
print(count_vowels(s))

##exercise 77-82.8
n = 6
def inverted_half_pyramid(n: int) -> None:
    if n == 0:
        return None
    else:
        print("*" * n)
        return inverted_half_pyramid(n - 1)
inverted_half_pyramid(n)

##exercise 77-82.10
n = 5
def convert_to_binary(n: int) -> str:
    if n == 0 or n == 1:
        return str(n)
    return convert_to_binary(n // 2) + str(n % 2)
print(convert_to_binary(n))

##exercise 77-82.12
myList = [4, 5, 6, 7]
n = 6
def binary_search(myList: list, n: int, ilow: int, ihigh: int) -> int:
    if ilow > ihigh:
        return -1
    mid_index = (ilow + ihigh) // 2

    if myList[mid_index] == n:
        return mid_index
    elif myList[mid_index] > n:
        return binary_search(myList, n, ilow, mid_index - 1)
    else:
        return binary_search(myList, n, mid_index + 1, ihigh)
print(binary_search(myList, n, 0, len(myList) - 1))

##exercise 83-87.2
filename = 'file.txt'
contents = []
with open(filename, 'r') as file:
    contents = file.readlines()
print(contents)

##exercise 83-87.4
filename = 'file.txt'
contents = []
with open(filename, 'r') as file:
    contents = file.readlines()
num_of_lines = len(contents)
while True:
    n = int(input(f'Please enter a value for n. The file has {num_of_lines} lines: '))
    if n < 1 or n > num_of_lines:
        print(f'Please enter a value. The file has {num_of_lines} lines.')
    else:
        break

for i in range(n):
    print(contents[i].strip())

##exercise 83-87.7
filename = 'file.txt'
contents = []
with open(filename, 'r') as file:
    contents = file.readlines()
num_of_lines = len(contents)
while True:
    n = int(input(f'Please enter a value for n. The file has {num_of_lines} lines: '))
    if n < 1 or n > num_of_lines:
        print(f'Please enter a value. The file has {num_of_lines} lines.')
    else:
        break

for i in range(-n, 0, 1):
    print(contents[i].strip())

##exercise 83-87.9
filename = 'file.txt'
longest_word = ''
with open(filename, 'r') as file:
    for item in file:
        if len(item) > len(longest_word):
            longest_word = item
print(longest_word)

##exercise 83-87.11
filename = 'file.txt'
myDict = {}
with open(filename, 'r') as file:
    for item in file:
        item = item.strip()
        if item not in myDict.keys():
            myDict[item] = 1
        else:
            myDict[item] += 1
print(myDict)

##exercise 88-91.1
filename = 'file.txt'
myList = [1, 2, 3, 4, 5]
with open(filename, 'w') as file:
    myList = [str(i) + '\n' for i in myList]
    file.writelines(myList)

##exercise 88-91.3
filename = 'file.txt'
with open(filename, 'r') as file:
    contents = file.read()
    contents = contents.replace('\n', '')
clean_content = contents.replace(' ', '')
print(f'Total number of characters: {len(clean_content)}')

##exercise 88-91.6
filename = 'file.txt'
name_to_write = 'newFile.txt'
with open(filename, 'r') as file:
    content = file.read()
    with open(name_to_write, 'w') as writeFile:
        writeFile = writeFile.write(content)

##exercise 88-91.8
import os.path

my_file = "newFile.txt"
if os.path.isfile(my_file):
    print(f"The file {my_file} exists")
else:
    print(f"The file {my_file} doesn't exist")

##exercise 92-97.1
from datetime import datetime
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

##exercise 92-97.4
seconds = 7200
minute = seconds / 60
hours = seconds / 3600
print(f'{seconds} seconds is equivalent to:\n{minute} Minutes\n{hours} Hours')

##exercise 92-97.6
from math import pi
diameter = 10
area = round(pi*(diameter/2)**2, 2)
print(f"The area of the circle with a diameter of {diameter} is {area}")

##exercise 92-97.9
base = int(input("Please enter base of triangle: "))
height = int(input("Please enter height of triangle: "))
if base <= 0 or height <= 0:
    print("Please enter valid values for base and height")
else:
    area = round((base * height)/2, 2)
    print(f'The area of the triangle with base: {base} and height: {height} is {area}')

##exercise 92-97.11
celsius = int(input("Please enter degrees in Celsius: "))
fahrenheit = round((celsius * 9/5) + 32)
print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")

##exercise 92-97.13
fahrenheit = int(input("Please enter degrees in Celsius: "))
celsius = round((fahrenheit - 32) * 5/9, 1)
print(f"{fahrenheit} Fahrenheit = {celsius} Celsius")\

##exercise 98-101.1
height = int(input("Please enter height (cm): "))
weight = int(input("Please enter weight (kg): "))
bmi = weight/(height/100)**2
print(f"BMI: {bmi}")
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normal")
elif bmi >= 25 and bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")

##exercise 98-101.3
import calendar
year = int(input("Please enter year: "))
month = int(input("Please enter month (1-12): "))

if year <= 0 or month < 1 or month > 12:
    print("Invalid date. Please try again")
else:
    print(calendar.month(year, month))

##exercise 98-101.6
from datetime import date
first_date = input("Please enter first date (YYYY M D): ")
sec_date = input("Please enter second date (YYYY M D): ")
date1 = (int(i) for i in first_date.split(" "))
date1 = date(*date1)
date2 = (int(i) for i in sec_date.split(" "))
date2 = date(*date2)
if date1 == date2:
    print("The dates are equal")
elif date2 < date1:
    print("Please enter valid dates")
else:
    dateDiff = (date2 - date1).days
    if dateDiff == 1:
        print(f"There is {dateDiff} day between these dates")
    else:
        print(f"There is {dateDiff} days between these dates")

##exercise 98-101.8
import re
s = 'My favorite color is blue'
pattern = '^My[\\w\\s]+blue$'

is_match = re.match(pattern, s)
if is_match:
    print("Match")
else:
    print("No Match")