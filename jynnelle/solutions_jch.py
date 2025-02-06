"""
This is for Python Exercises
"""
## exercise 1-8.2 s = "Python"
# Prints the length of the string s.
s = "Python"
print(len(s))  # Output: 6


## exercise 1-8.4 s = "Hello" i = 0
# Prints the character at index i in the string s.
s = "Hello"
i = 0
if s == "":
    print("Empty String")
elif i >= 0 and i < len(s):
    print(s[i])  # Output: H
else:
    print("i is out of range")


## exercise 1-8.6 s = "HelloWorld"
# Prints the reversed version of the string s, preserving case.
s = "HelloWorld"
if s == "":
    print(s)
else:
    print(s[::-1])  # Output: dlroWolleH


## exercise 1-8.8 s = "HelloWorld"
# Prints the first and last three characters of s as a single string.
s = "HelloWorld"
if len(s) < 6:
    print("")
else:
    print(s[:3] + s[-3:])  # Output: Helrld


## exercise 1-8.11 s = "HelloWorld"
# Prints the string s without characters at even indices.
s = "HelloWorld"
if len(s) <= 1:
    print(s)
else:
    print(s[1::2])  # Output: elWrd


## exercise 1-8.13 s = "12345"
# Checks if the string s contains only numbers.
s = "12345"
if s.isdigit():
    print(True)  # Output: True
else:
    print(False)


## exercise 1-8.15 s = "HelloWorld" n = 5
# Prints the string s without the character at index n.
s = "HelloWorld"
n = 5
if s == "" or n < 0 or n >= len(s):
    print(s)
else:
    print(s[:n] + s[n+1:])  # Output: Helloorld


## exercise 1-8.17 s = "HelloWorld" curr_char = 'o' new_char = '0'
# Prints the string s with curr_char replaced by new_char (case-sensitive).
s = "HelloWorld"
curr_char = 'o'
new_char = '0'
if curr_char in s:
    print(s.replace(curr_char, new_char))  # Output: Hell0W0rld
else:
    print(s)


## exercise 9-16.1 s = "1,234,567"
# Prints a version of the string s with all commas replaced by dots.
s = "1,234,567"
print(s.replace(",", "."))  # Output: 1.234.567


## exercise 9-16.3 s = "The quick brown fox jumps over the lazy dog"
# Checks if the string s contains all the letters in the alphabet (case-insensitive).
import string
s = "The quick brown fox jumps over the lazy dog"
s_clean = s.replace(" ", "").lower()
if set(string.ascii_lowercase).issubset(set(s_clean)):
    print(True)  # Output: True
else:
    print(False)


## exercise 9-16.5 s = "Hello World"
# Prints a copy of the string s without any spaces.
s = "Hello World"
print(s.replace(" ", ""))  # Output: HelloWorld


## exercise 9-16.7 s = "HelloWorld" prefix = "Hello"
# Checks if the string s starts with the sequence of characters denoted by prefix.
s = "HelloWorld"
prefix = "Hello"
if len(prefix) > len(s):
    print(False)
elif s.startswith(prefix):
    print(True)  # Output: True
else:
    print(False)


## exercise 9-16.9 s = "HelloWorld" suffix = "World"
# Checks if the string s ends with the sequence of characters denoted by suffix.
s = "HelloWorld"
suffix = "World"
if len(suffix) > len(s):
    print(False)
elif s.endswith(suffix):
    print(True)  # Output: True
else:
    print(False)


## exercise 9-16.12 s = "Hello World"
# Reverses the individual words in the string s and changes their capitalization.
s = "Hello World"
words = s.split()
result = []
for word in words:
    reversed_word = word[::-1]
    swapped_case = reversed_word.swapcase()
    result.append(swapped_case)
print(" ".join(result))  # Output: OLLEh DLROw


## exercise 9-16.14 s = "programming"
# Counts the number of repeated characters in the string s.
s = "programming"
repeated_chars = []
for char in set(s):
    if s.count(char) > 1:
        repeated_chars.append(char)
if repeated_chars:
    print(len(repeated_chars))  # Output: 3
    print(" ".join(sorted(repeated_chars)))  # Output: g m r
else:
    print(0)
    print("None")


## exercise 9-16.16 s = "Hello World"
# Converts the string s to lowercase, sorts the characters of each word, and prints the result.
s = "Hello World"
words = s.lower().split()
sorted_words = []
for word in words:
    sorted_word = "".join(sorted(word))
    sorted_words.append(sorted_word)
print(" ".join(sorted_words))  # Output: ehllo dlorw


## exercise 17-24.2 lst = [1, 2, 3] factor = 2
# Multiplies all items in the list by factor and prints the list.
lst = [1, 2, 3]
factor = 2
result = [item * factor for item in lst]
print(result)  # Output: [2, 4, 6]


## exercise 17-24.4 lst = [1, 2, 3, 4]
# Prints the elements of the list on the same line separated by a space.
lst = [1, 2, 3, 4]
print(" ".join(map(str, lst)))  # Output: 1 2 3 4


## exercise 17-24.6 lst = [3, 1, 4, 1, 5]
# Prints the largest and smallest values in the list.
lst = [3, 1, 4, 1, 5]
if lst:
    print(max(lst), min(lst))  # Output: 5 1
else:
    print("None")


## exercise 17-24.8 lst = []
# Checks if the list is empty or not.
lst = []
if len(lst) == 0:
    print("Empty")
else:
    print("Not Empty")


## exercise 17-24.11 lst = ['a', 'b', 'c']
# Prints the elements of the list followed by their indices.
lst = ['a', 'b', 'c']
if lst:
    for index, item in enumerate(lst):
        print(item, index)
else:
    print("Empty List")


## exercise 17-24.13 lst = [1, 2, 3, 2, 4] elem_to_remove = 2
# Removes all occurrences of elem_to_remove from the list.
lst = [1, 2, 3, 2, 4]
elem_to_remove = 2
if not lst:
    print("Empty List")
elif elem_to_remove not in lst:
    print("Not Found")
else:
    lst = [item for item in lst if item != elem_to_remove]
    print(lst)  # Output: [1, 3, 4]


## exercise 17-24.15 lst = [1, 2, 2, 3, 4, 4]
# Removes duplicate elements from the list.
lst = [1, 2, 2, 3, 4, 4]
lst = list(set(lst))
print(lst)  # Output: [1, 2, 3, 4]


## exercise 17-24.17 lst = [1, 2, 3, 4, 5]
# Counts the number of elements greater than 3 in the list.
lst = [1, 2, 3, 4, 5]
count = sum(1 for item in lst if item > 3)
print(count)  # Output: 2


## 25-32.1: Find elements in listA not in listB
listA = [1, 2, 3, 4]
listB = [3, 4, 5, 6]
print([x for x in listA if x not in listB])

## 25-32.3: Compute distance between two 3D points
import math
point1, point2 = [1, 2, 3], [4, 5, 6]
distance = math.sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)))
print(distance)

## 25-32.5: Find common elements in two lists
listA, listB = [1, 2, 3], [3, 4, 5]
print([x for x in listA if x in listB])

## 25-32.7: Find the second largest value in a list
lst = [10, 20, 4, 45, 99]
print(sorted(lst)[-2] if len(lst) > 1 else None)

## 25-32.12: Count frequency of elements in a list
lst = ["apple", "banana", "apple", "orange", "banana", "apple"]
freq_dict = {x: lst.count(x) for x in set(lst)}
print(freq_dict)

## 25-32.14: Flatten a nested list
nested_list = [[1, 2, [3, 4]], 5, [6, 7]]
def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list
print(flatten(nested_list))

## 25-32.16: Generate all permutations of a list
import itertools
lst = [1, 2, 3]
print(list(itertools.permutations(lst)))


## 33-38.2: Check if a key exists in a dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
key = "b"
print(key in my_dict)

## 33-38.4: Add a key-value pair if key doesn't exist
new_key, new_value = "d", 4
if new_key not in my_dict:
    my_dict[new_key] = new_value
print(my_dict)

## 33-38.6: Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)

## 33-38.9: Check if all values in a dictionary are equal
values = list(my_dict.values())
print("Empty" if not values else len(set(values)) == 1)

## 33-38.11: Find the largest value in a dictionary
print(max(my_dict.values()) if my_dict else None)

## 33-38.13: Find the smallest value in a dictionary
print(min(my_dict.values()) if my_dict else None)


## 39-44.1: Count the frequency of values in a dictionary
my_dict = {"a": 4, "b": 4, "c": 2, "d": 7, "e": 4, "f": 2, "g": 7, "h": 7}
freq_dict = {}
for value in my_dict.values():
    freq_dict[value] = freq_dict.get(value, 0) + 1
print(freq_dict)

## 39-44.3: Create a dictionary from nested lists
nested_list = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]
dict_from_list = dict(nested_list)
print(dict_from_list)

## 39-44.5: Find the largest sum of values in a dictionary
my_dict = {"a": [1, 2, 3], "b": [4, 0, -4], "c": [3, 5, 9], "d": [45, 12, 100]}
print(max(sum(v) for v in my_dict.values()))

## 39-44.8: Count letter frequency in a string
s = "Hello, World".lower()
letter_count = {char: s.count(char) for char in s if char.isalpha()}
print(letter_count)

## 39-44.10: Sort lists inside a dictionary
my_dict = {"a": [4, 3, 2], "b": [5, 3, 7], "c": [1, 9, 10], "d": [3, 4, 1]}
for key in my_dict:
    my_dict[key].sort()
print(my_dict)

## 39-44.12: Convert dictionary to list of lists
product_info = {"description": "shoe", "price": 4.56, "colors": ["green", "blue", "red"]}
list_of_lists = list(product_info.items())
print(list_of_lists)


## 45-50.2: Check if a number is Positive, Negative, or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

## 45-50.4: Identify vowels, consonants, or other characters
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
for char in s:
    if char.isalpha():
        if char in vowels:
            print(f"{char} is a vowel")
        else:
            print(f"{char} is a consonant")
    else:
        print(f"{char} is not a letter")

## 45-50.6: Find the maximum of three integers
a, b, c = map(int, input("Enter three numbers: ").split())
print("Maximum:", max(a, b, c))

## 45-50.9: Find the smallest of three integers
a, b, c = map(int, input("Enter three numbers: ").split())
print("Smallest:", min(a, b, c))

## 45-50.11: Determine season from a number
season_num = int(input("Enter a season number (1-4): "))
seasons = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
print(seasons.get(season_num, "Please enter a valid number"))

## 45-50.13: Check if three numbers are equal
a, b, c = map(int, input("Enter three numbers: ").split())
if a == b == c:
    print("Equal")
else:
    print("Not Equal")


## 51-56.1: Number of days in a given month
month_days = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31,
              "June": 30, "July": 31, "August": 31, "September": 30, "October": 31,
              "November": 30, "December": 31}
month = input("Enter month name: ").capitalize()
print(f"{month} has: {month_days.get(month, 'Invalid month')} days.")

## 51-56.3: Determine order of three numbers
a, b, c = map(int, input("Enter three numbers: ").split())
if a < b < c:
    print("Increasing Order")
elif a > b > c:
    print("Decreasing Order")
else:
    print("None")

## 51-56.5: Solve a quadratic equation
import math
a, b, c = map(float, input("Enter coefficients a, b, c: ").split())
discriminant = b**2 - 4*a*c
if discriminant < 0:
    print("Complex Roots")
elif discriminant == 0:
    root = -b / (2*a)
    print("One root:", root)
else:
    root1 = (-b - math.sqrt(discriminant)) / (2*a)
    root2 = (-b + math.sqrt(discriminant)) / (2*a)
    print("Roots:", root1, root2)

## 51-56.8: Check for leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

## 51-56.10: Interactive Calculator
print("=== Welcome to your Interactive Python Calculator ===")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Choose an operation:")
print("1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Integer Division\n6 - Modulo")
choice = int(input("Enter the operation number: "))
if choice == 1:
    print("Result:", num1 + num2)
elif choice == 2:
    print("Result:", num1 - num2)
elif choice == 3:
    print("Result:", num1 * num2)
elif choice == 4:
    print("Result:", num1 / num2 if num2 != 0 else "Cannot divide by zero")
elif choice == 5:
    print("Result:", num1 // num2 if num2 != 0 else "Cannot divide by zero")
elif choice == 6:
    print("Result:", num1 % num2 if num2 != 0 else "Cannot divide by zero")
else:
    print("Invalid choice")

## 51-56.12: Rock, Paper, Scissors game
import random
choices = ["Rock", "Paper", "Scissors"]
user_choice = input("Enter Rock, Paper, or Scissors: ").capitalize()
computer_choice = random.choice(choices)
print(f"Computer chose: {computer_choice}")
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "Rock" and computer_choice == "Scissors") or \
     (user_choice == "Paper" and computer_choice == "Rock") or \
     (user_choice == "Scissors" and computer_choice == "Paper"):
    print("You win!")
else:
    print("You lose!")


## 57-63.2: Print first 15 positive integers
for i in range(1, 16):
    print(i)

## 57-63.4: Print integers from n to 1
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(i)

## 57-63.6: Sum of first 100 non-negative integers
print("Sum:", sum(range(1, 101)))

## 57-63.8: Multiplication table
n = int(input("Enter a number: "))
print(f"==== Multiplication Table of {n} ====\n")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

## 57-63.11: Print uppercase alphabet
for i in range(65, 91):
    print(chr(i))

## 57-63.13: Print first 100 even numbers
for i in range(2, 202, 2):
    print(i)

## 57-63.15: Factorial of a number
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)


## 64-71.1: Check if a number is prime
num = int(input("Enter a number: "))
if num < 2:
    print("Not Prime")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

## 64-71.3: Print a triangular pattern
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print("* " * i)

## 64-71.5: Print digits of a number in reverse order
num = input("Enter a number: ")
print(num[::-1])

## 64-71.7: Reverse a string using a loop
s = input("Enter a string: ")
reversed_s = ""
for char in s:
    reversed_s = char + reversed_s
print(reversed_s)

## 64-71.10: Print a pyramid pattern
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

## 64-71.12: Print Floyd's Triangle
n = int(input("Enter number of rows: "))
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

## 64-71.14: Print a triangular pattern with letters
n = int(input("Enter number of rows: "))
for i in range(n):
    print((chr(65 + i) + " ") * (i + 1))

## 64-71.16: Print a diamond pattern
n = int(input("Enter an odd number for diamond height: "))
if n % 2 == 0:
    print("Please enter an odd number.")
else:
    for i in range(1, n + 1, 2):
        print(" " * ((n - i) // 2) + "*" * i)
    for i in range(n - 2, 0, -2):
        print(" " * ((n - i) // 2) + "*" * i)


## 72-76.2: Find sum of a list using recursion
def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sum:", recursive_sum(numbers))

## 72-76.4: Find nth Fibonacci number using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Enter position: "))
print("Fibonacci number:", fibonacci(n))

## 72-76.6: Compute factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
n = int(input("Enter a number: "))
print("Factorial:", factorial(n))

## 72-76.9: Compute sum of digits using recursion
def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)
n = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(n))

## 72-76.11: Compute power using recursion
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)
a, b = map(int, input("Enter base and exponent: ").split())
print("Power:", power(a, b))


## 77-82.1: Find GCD of two numbers using recursion
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
a, b = map(int, input("Enter two numbers: ").split())
print("GCD:", gcd(a, b))

## 77-82.3: Check if a string is a palindrome using recursion
def is_palindrome(s):
    s = s.lower()
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
s = input("Enter a string: ")
print("Palindrome:", is_palindrome(s))

## 77-82.5: Count vowels in a string using recursion
def count_vowels(s):
    vowels = "aeiouAEIOU"
    if not s:
        return 0
    return (1 if s[0] in vowels else 0) + count_vowels(s[1:])
s = input("Enter a string: ")
print("Vowel count:", count_vowels(s))

## 77-82.8: Print pattern using recursion
def print_pattern(n):
    if n > 0:
        print("*" * n)
        print_pattern(n - 1)
n = int(input("Enter number of rows: "))
print_pattern(n)

## 77-82.10: Convert decimal to binary using recursion
def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_to_binary(n // 2) + str(n % 2)
n = int(input("Enter a decimal number: "))
print("Binary:", decimal_to_binary(n))

## 77-82.12: Implement binary search using recursion
def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)
arr = list(map(int, input("Enter sorted list: ").split()))
target = int(input("Enter target value: "))
index = binary_search(arr, target, 0, len(arr) - 1)
print("Index:" if index != -1 else "Not found", index)


## 83-87.2: Read file contents into a list
file_name = input("Enter file name: ")
with open(file_name, "r") as file:
    file_content = file.readlines()
print(file_content)

## 83-87.4: Read and print first n lines of a file
file_name = input("Enter file name: ")
n = int(input("Enter number of lines: "))
with open(file_name, "r") as file:
    lines = file.readlines()
if n > len(lines):
    print(f"Please enter a valid value. The file has {len(lines)} lines.")
else:
    print("".join(lines[:n]))

## 83-87.7: Print last n lines of a file
file_name = input("Enter file name: ")
n = int(input("Enter number of lines: "))
with open(file_name, "r") as file:
    lines = file.readlines()
print("".join(lines[-n:]))

## 83-87.9: Find longest word in a file
file_name = input("Enter file name: ")
with open(file_name, "r") as file:
    words = file.read().split()
longest_word = max(words, key=len)
print("Longest word:", longest_word)

## 83-87.11: Create a word frequency dictionary
file_name = input("Enter file name: ")
with open(file_name, "r") as file:
    words = file.read().split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)


## 88-91.2: Write text to a file
file_name = input("Enter file name: ")
text = input("Enter text to write: ")
with open(file_name, "w") as file:
    file.write(text)
print("Text written successfully.")

## 88-91.5: Append text to a file
file_name = input("Enter file name: ")
text = input("Enter text to append: ")
with open(file_name, "a") as file:
    file.write(text + "\n")
print("Text appended successfully.")

## 88-91.7: Count occurrences of a word in a file
file_name = input("Enter file name: ")
word_to_count = input("Enter word to count: ")
with open(file_name, "r") as file:
    text = file.read()
count = text.split().count(word_to_count)
print(f"'{word_to_count}' appears {count} times in the file.")

## 88-91.10: Copy contents of one file to another
source_file = input("Enter source file name: ")
destination_file = input("Enter destination file name: ")
with open(source_file, "r") as src, open(destination_file, "w") as dest:
    dest.write(src.read())
print("File copied successfully.")


## 92-97.2: Display the current date and time
import datetime
now = datetime.datetime.now()
print("Current Date and Time:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

## 92-97.4: Convert seconds to minutes and hours
seconds = int(input("Enter seconds: "))
minutes = seconds // 60
hours = round(seconds / 3600, 2)
print(f"{seconds} seconds is equivalent to:")
print(f"{minutes} Minutes")
print(f"{hours} Hours")

## 92-97.6 Find the area of a circle from the diameter
diameter = float(input("Enter the diameter of the circle: "))
import math
radius = diameter / 2
area = math.pi * (radius ** 2)
print(f"The area of a circle with diameter {diameter} is {round(area, 2)}")

## 92-97.9 Compute the area of a triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
if base > 0 and height > 0:
    area = (base * height) / 2
    print(f"The area of the triangle is {round(area, 2)}")
else:
    print("Please enter valid values for base and height")

## 92-97.11 Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")

## 92-97.13 Convert Fahrenheit to Celsius
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit} Fahrenheit = {round(celsius, 2)} Celsius")

## 98-101.1 Calculate Body Mass Index (BMI)
height_cm = float(input("Enter your height in centimeters: "))
weight_kg = float(input("Enter your weight in kilograms: "))
height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"
print(f"Your BMI is {round(bmi, 2)} which is considered {category}")

## 98-101.3 Print calendar of a given month and year
import calendar
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))
if 1 <= month <= 12 and year > 0:
    # Print the calendar
    print(calendar.month(year, month))
else:
    print("Please enter a valid month and year")

## 98-101.6 Calculate days between two dates
from datetime import date

date1_input = input("Enter the first date (Year Month Day): ")
date1_parts = date1_input.split()
date1 = date(int(date1_parts[0]), int(date1_parts[1]), int(date1_parts[2]))

date2_input = input("Enter the second date (Year Month Day): ")
date2_parts = date2_input.split()
date2 = date(int(date2_parts[0]), int(date2_parts[1]), int(date2_parts[2]))

if date1 > date2:
    print("Please enter valid dates")
else:
    difference = (date2 - date1).days
    if difference == 0:
        print("The dates are equal")
    elif difference == 1:
        print("There is 1 day between these dates.")
    else:
        print(f"There are {difference} days between these dates.")

## 98-101.8 Check if string starts with 'My' and ends with 'blue'
import re
input_string = input("Enter a string: ")
if re.match(r'^My.*blue$', input_string) and input_string.isalnum():
    print("Match")
else:
    print("No Match")