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


    