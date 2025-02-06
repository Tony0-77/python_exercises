##exercise 1-8.2
userInput = input("Enter a string: ")
length = len(userInput)
print(f"{length}")

##exercise 1-8.4
def print_character(s, i):
    if len(s) == 0:
        print("Empty String")
    elif i < 0 or i >= len(s):
        print(f"{i} is out of range")
    else:
        print(s[i])

s = "Hello, World!"
i = 5
print_character(s, i)

##exercise 1-8.6
s = input()
print(s[::-1])

##exercise 1-8.8
s = input()
print(s[:3] + s[-3:] if len(s) >= 6 else "")

##exercise 1-8.11
s = input()
print(s if len(s) <= 1 else s[1::2])

##exercise 1-8.13
s = input()
print(s.isdigit())

##exercise 1-8.15
s = input()
n = int(input())

print(s if n < 0 or n >= len(s) else s[:n] + s[n+1:])


##exercise 1-8.17
s = input()
curr_char = input()
new_char = input()

print(s.replace(curr_char, new_char))

##exercise 9-16.1
s = input()
print(s.replace(",", "."))


##exercise 9-16.3
import string

s = input().lower().replace(" ", "")
alphabet_set = set(string.ascii_lowercase)

if set(s) >= alphabet_set:
    print(True)
else:
    print(False)


##exercise 9-16.5
s = input()
print(s.replace(" ", ""))


##exercise 9-16.7
s = input()
prefix = input()

print(s.startswith(prefix))


##exercise 9-16.9
s = input()
suffix = input()

print(s.endswith(suffix))


##exercise 9-16.12
s = input()
reversed_words = [word[::-1].swapcase() for word in s.split()]
print(" ".join(reversed_words))


##exercise 9-16.14
from collections import Counter

s = input()
counter = Counter(s)

repeated_chars = [char for char, count in counter.items() if count > 1]

if repeated_chars:
    print(len(repeated_chars))
    print(" ".join(sorted(repeated_chars)))
else:
    print(0)
    print("None")


##exercise 9-16.16
s = input()
words = s.split()

sorted_words = ["".join(sorted(word.lower())) for word in words]
result = " ".join(sorted_words)

print(result)


##exercise 17-24.2
factor = int(input())
items = input().split()

result = [item * factor if isinstance(item, str) else item * factor for item in items]

print(result)


##exercise 17-24.4
lst = input().split()
print(" ".join(lst))


##exercise 17-24.6
lst = list(map(int, input().split()))

if lst:
    print(max(lst), min(lst))
else:
    print(None)


##exercise 17-24.8
lst = input().split()

if len(lst) == 0:
    print("Empty")
else:
    print("Not Empty")


##exercise 17-24.11
lst = input().split()

if lst:
    for index, element in enumerate(lst):
        print(index, element)
else:
    print("Empty List")


##exercise 17-24.13
lst = input().split()
elem_to_remove = input()

if len(lst) == 0:
    print("Empty List")
else:
    count = lst.count(elem_to_remove)
    if count > 0:
        lst = [elem for elem in lst if elem != elem_to_remove]
        print(lst)
    else:
        print("Not Found")


##exercise 17-24.15
lst = input().split()

lst = list(set(lst))

print(lst)


##exercise 17-24.17
lst = list(map(int, input().split()))

count = sum(1 for x in lst if x > 3)

print(count)


##exercise 25-32.1
listA = input().split()
listB = input().split()

result = [item for item in listA if item not in listB]

print(result)


##exercise 25-32.3
import math

point1 = list(map(float, input().split()))
point2 = list(map(float, input().split()))

distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)

print(f"{distance:.1f}")


##exercise 25-32.5
listA = input().split()
listB = input().split()

common_elements = [item for item in listA if item in listB]

print(common_elements)


##exercise 25-32.7
lst = list(map(int, input().split()))

if len(lst) < 2:
    print(None)
else:
    lst_sorted = sorted(lst)
    print(lst_sorted[-2])


##exercise 25-32.10
lst = list(map(int, input().split()))

if len(lst) < 2:
    print(None)
else:
    lst_sorted = sorted(lst)
    print(lst_sorted[1])


##exercise 25-32.12
lst = input().split()

freq_dict = {}

for item in lst:
    if item in freq_dict:
        freq_dict[item] += 1
    else:
        freq_dict[item] = 1

print(freq_dict)


##exercise 25-32.14
def flatten(lst):
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten(item))
        else:
            flattened.append(item)
    return flattened

lst = input()
nested_list = eval(lst)

flattened_list = flatten(nested_list)
print(flattened_list)


##exercise 25-32.16
import itertools

lst = input().split()

permutations = itertools.permutations(lst)

for perm in permutations:
    print(list(perm))


##exercise 33-38.2
my_dict = {'a': 1, 'b': 2, 'c': 3}
key = input()

if key in my_dict:
    print(True)
else:
    print(False)


##exercise 33-38.4
my_dict = {"January": 45, "February": 56, "March": 67}

new_key = input()
new_value = int(input())

if new_key not in my_dict:
    my_dict[new_key] = new_value
    print("New Pair Added")
else:
    print("No Change")

print(my_dict)


##exercise 33-38.6
my_dict1 = {"a": 1, "b": 2, "c": 3}
my_dict2 = {"c": 4, "d": 6, "e": 8}

final_dict = my_dict1.copy()
final_dict.update(my_dict2)

print(final_dict)


##exercise 33-38.9
my_dict = {"a": 1, "b": 1, "c": 1}

if not my_dict:
    print("Empty")
else:
    values = list(my_dict.values())
    
    if len(set(values)) == 1:
        print(True)
    else:
        print(False)


##exercise 33-38.11
my_dict = {"a": 5, "b": 10, "c": 3}

if not my_dict:
    print(None)
else:
    largest_value = max(my_dict.values())
    print(largest_value)


##exercise 33-38.13
my_dict = {"a": 5, "b": 1, "c": 3}

if not my_dict:
    print(None)
else:
    smallest_value = min(my_dict.values())
    print(smallest_value)


##exercise 39-44.1
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

if not my_dict:
    print({})
else:
    freq_dict = {}
    
    for value in my_dict.values():
        if value in freq_dict:
            freq_dict[value] += 1
        else:
            freq_dict[value] = 1
    
    print(freq_dict)


##exercise 39-44.3
nested_list = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]

if not nested_list:
    print({})
else:
    result_dict = {key: value for key, value in nested_list}

    print(result_dict)


##exercise 39-44.5
my_dict = {
    "a": [1, 2, 3],
    "b": [4, 0, -4],
    "c": [3, 5, 9],
    "d": [45, 12, 100]
}

largest_sum = float('-inf')

for key, value in my_dict.items():
    current_sum = sum(value) 
    largest_sum = max(largest_sum, current_sum)

print(largest_sum)


##exercise 39-44.8
from collections import defaultdict

def letter_frequency(s):
    s = ''.join(filter(str.isalpha, s.lower()))
    
    frequency_dict = defaultdict(int)

    for char in s:
        frequency_dict[char] += 1
    
    return dict(frequency_dict)

s1 = "Hello, World"
print(letter_frequency(s1))

s2 = "Excellent"
print(letter_frequency(s2))


##exercise 39-44.10
def sort_dict_lists(my_dict):
    for key in my_dict:
        my_dict[key].sort()
    return my_dict

my_dict = {
    "a": [4, 3, 2],
    "b": [5, 3, 7],
    "c": [1, 9, 10],
    "d": [3, 4, 1]
}

sorted_dict = sort_dict_lists(my_dict)

print(sorted_dict)


##exercise 39-44.12
def dict_to_list_of_lists(product_info):
    return [[key, value] for key, value in product_info.items()]

product_info = {
    "description": "shoe",
    "price": 4.56,
    "colors": ["green", "blue", "red"],
}

result = dict_to_list_of_lists(product_info)

print(result)


##exercise 45-50.2
num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


##exercise 45-50.4
s = input("Enter a string: ")

if not s:
    print("Empty String")
else:
    for char in s:
        if char.isalpha():
            if char.lower() in 'aeiou':
                print(f"{char} is a vowel")
            else:
                print(f"{char} is a consonant")
        elif char == ' ':
            print(f"Space is not a letter")
        else:
            print(f"{char} is not a letter")


##exercise 45-50.6
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

max_value = max(a, b, c)
print(f"The maximum value is: {max_value}")


##exercise 45-50.9
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

min_value = min(a, b, c)
print(f"The smallest value is: {min_value}")


##exercise 45-50.11
season_num = int(input("Enter a number (1-4) to get the corresponding season: "))

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
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a == b == c:
    print("Equal")
else:
    print("Not Equal")

##exercise 51-56.1
month = input("Enter the name of the month: ")

month_days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

if month in month_days:
    print(f"{month} has: {month_days[month]} days.")
else:
    print("Please enter a valid month name.")


##exercise 51-56.3
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

if a > b > c:
    print("Decreasing Order")
elif a < b < c:
    print("Increasing Order")
else:
    print("None")


##exercise 51-56.5
import math

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

discriminant = b**2 - 4 * a * c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"{root2} {root1}")
elif discriminant == 0:
    root = -b / (2 * a)
    print(root)
else:
    print("Complex Roots")

##exercise 51-56.8
year = int(input("Enter a year: "))

if year % 4 != 0:
    print(f"{year} is not a leap year")
elif year % 100 != 0:
    print(f"{year} is a leap year")
elif year % 400 != 0:
    print(f"{year} is not a leap year")
else:
    print(f"{year} is a leap year")

##exercise 51-56.10
def calculator():
    print("=== Welcome to your Interactive Python Calculator ===")
    
    try:
        first_value = float(input("Please enter the first value: "))
        second_value = float(input("Please enter the second value: "))
        
        print("Great! Now enter the operation.")
        print("These are the available options:")
        print("1 - Addition")
        print("2 - Subtraction")
        print("3 - Multiplication")
        print("4 - Division")
        print("5 - Integer Division")
        print("6 - Modulo")
        
        operation = int(input("--> Enter the corresponding integer: "))
        
        if operation == 1:
            result = first_value + second_value
            print(f"The result of {first_value} + {second_value} is: {result}")
        
        elif operation == 2:
            result = first_value - second_value
            print(f"The result of {first_value} - {second_value} is: {result}")
        
        elif operation == 3:
            result = first_value * second_value
            print(f"The result of {first_value} * {second_value} is: {result}")
        
        elif operation == 4:
            if second_value == 0:
                print("Error: Division by 0 is not allowed.")
            else:
                result = first_value / second_value
                print(f"The result of {first_value} / {second_value} is: {result}")
        
        elif operation == 5:
            if second_value == 0:
                print("Error: Integer division by 0 is not allowed.")
            else:
                result = first_value // second_value
                print(f"The result of {first_value} // {second_value} is: {result}")
        
        elif operation == 6:
            if second_value == 0:
                print("Error: Modulo by 0 is not allowed.")
            else:
                result = first_value % second_value
                print(f"The result of {first_value} % {second_value} is: {result}")
        
        else:
            print("Please choose a valid operation")
    
    except ValueError:
        print("Error: Please enter valid numbers.")

calculator()

     
##exercise 51-56.12
import random

def rock_paper_scissors():
    print("====== Welcome to the game ======")

    player_choice = input("Please enter Rock, Paper, or Scissors below:\n").capitalize()

    if player_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice! Please enter Rock, Paper, or Scissors.")
        return
    
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    print(f"Your opponent chose '{computer_choice}'")

    if player_choice == computer_choice:
        print("It's a tie! Try again.")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        print(f"You win! Your opponent chose '{computer_choice}'")
    else:
        print(f"You lose! Your opponent chose '{computer_choice}'")

rock_paper_scissors()

##exercise 57-63.2
# Using range() to generate numbers from 1 to 15
for i in range(1, 16):
    print(i)


##exercise 57-63.4
n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    print(i)


##exercise 57-63.6
total_sum = 0

for i in range(1, 101):
    total_sum += i

print("The sum of the first 100 non-negative integers is:", total_sum)


##exercise 57-63.8
n = int(input("Enter a positive integer: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

##exercise 57-63.11
for code in range(65, 91):
    print(chr(code))


##exercise 57-63.11
for num in range(2, 201, 2):
    print(num)

##exercise 57-63.15
n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"The factorial of {n} is: {factorial}")

##exercise 64-71.1
num = int(input("Enter a number: "))

if num <= 1:
    print("Not prime")
else:
    is_prime = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not prime")

##exercise 64-71.3
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    print('* ' * i)


##exercise 64-71.5
number = input("Enter a number: ")

for digit in reversed(number):
    print(digit, end="")


##exercise 64-71.7
string = input("Enter a string: ")

for i in range(len(string) - 1, -1, -1):
    print(string[i], end="")

##exercise 64-71.10
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    
    for k in range(i):
        print("*", end=" ")
    
    print()

##exercise 64-71.12
n = int(input("Enter the number of rows: "))

num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1 
    print()  


##exercise 64-71.14
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    letter = chr(64 + i)
    
    print(" ".join([letter] * i))

##exercise 64-71.16
height = int(input("Enter the height of the diamond (odd number only): "))

if height % 2 == 0:
    print("Please enter an odd number for the height.")
else:
    for i in range(1, height + 1, 2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i)

    for i in range(height - 2, 0, -2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i)


##exercise 72-76.2
def recursive_sum(numbers):
    if not numbers:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])

numbers = [1, 2, 3, 4, 5]
print(recursive_sum(numbers))

##exercise 72-76.4
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 6
print(fibonacci(n))

##exercise 72-76.6
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

num = 5
print(f"The factorial of {num} is: {factorial(num)}")


##exercise 72-76.9
def sum_of_digits(num):
    if num == 0:
        return 0
    else:
        return num % 10 + sum_of_digits(num // 10)

num = 123
print(f"The sum of the digits of {num} is: {sum_of_digits(num)}")

##exercise 72-76.11
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1) 

a = 2
b = 5
result = power(a, b)
print(f"{a} raised to the power of {b} is: {result}")

##exercise 77-82.1
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Example usage
a = 56
b = 98
print(f"The GCD of {a} and {b} is: {gcd(a, b)}")

##exercise 77-82.3
string = input("Enter a string: ").lower()

if string == string[::-1]:
    print(True)
else:
    print(False)

##exercise 77-82.5
def count_vowels(string):
    if not string:
        return 0
    
    if string[0].lower() in 'aeiou':
        return 1 + count_vowels(string[1:])
    else:
        return count_vowels(string[1:])

input_string = input("Enter a string: ")

print(count_vowels(input_string))

##exercise 77-82.8
def print_pattern(n):
    if n > 0:
        print('*' * n)
        print_pattern(n - 1)

n = int(input("Enter the number of rows (n): "))
print_pattern(n)

##exercise 77-82.10
def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    return decimal_to_binary(n // 2) + str(n % 2)

n = int(input("Enter a decimal number: "))
print(decimal_to_binary(n))

##exercise 77-82.12
def binary_search(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

arr = [1, 3, 5, 7, 9, 11, 13]
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

pattern = r"^My\w*$"  # Starts with 'My' and only contains alphanumeric characters (word characters)

if re.match(pattern, user_input) and user_input.endswith("blue"):
    print("Match")
else:
    print("Not Match")
