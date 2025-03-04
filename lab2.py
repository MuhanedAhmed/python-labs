# 1. Reverse a String 

# Write a Python program to reverse a string.

print("\n", "="*10, "Question 1", "="*10, "\n")

str = "Mohaned Ahmed Ibrahim"

print(str[::-1])


print("\n", "="*40)

# ======================================================== #

# 2. Check if a String is a Palindrome 

# Write a Python program to check if a string is a palindrome (reads the same backward as forward).

print("\n", "="*10, "Question 2", "="*10, "\n")

str = "MooM"

print(str == str[::-1])


print("\n", "="*40)

# ======================================================== #

# 3.Remove Duplicates from a String 

# Write a Python program to remove duplicate characters from a string. 

print("\n", "="*10, "Question 3", "="*10, "\n")

str = "This is a repeated string !!"

print("-".join((set(str))))


print("\n", "="*40)

# ======================================================== #

# 4.Find the Longest Word in a String 

# Write a Python program to find the longest word in a given string. 

# text = "Python is a great programming language" 

#Output=programming 

print("\n", "="*10, "Question 4", "="*10, "\n")

str = "Python is a great programming language"

print(max(str.split(" ")))


print("\n", "="*40)

# ======================================================== #

# 5.Find Common Elements Between Two Tuples 

# Write a Python program to find common elements between two tuples. 

# ``` python 

# tuple1 = (1, 2, 3) 

# tuple2 = (2, 3, 4) 

# Output: (2, 3) 

print("\n", "="*10, "Question 5", "="*10, "\n")

tuple1 = (1, 2, 3) 

tuple2 = (2, 3, 4)

print(tuple(set(tuple1).intersection(set(tuple2))))


print("\n", "="*40)

# ======================================================== #

# 6.Find the Maximum and Minimum Value in a Dictionary 

# Write a Python program to find the maximum and minimum value in a dictionary. 

# my_dict = {"a": 10, "b": 20, "c": 5}  

# Min= 5  , max=20 

print("\n", "="*10, "Question 6", "="*10, "\n")

my_dict = {"a": 10, "b": 20, "c": 5} 

print(f'Max = {max(my_dict.values())}, Min = {min(my_dict.values())}')


print("\n", "="*40)

# ======================================================== #

# 7- Merge Two Dictionaries 

# Write a Python program to merge two dictionaries. 

# dict1 = {"a": 1, "b": 2} 

# dict2 = {"c": 3, "d": 4} 

# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}  

print("\n", "="*10, "Question 7", "="*10, "\n")

dict1 = {"a": 1, "b": 2} 

dict2 = {"c": 3, "d": 4}

dict1.update(dict2)

print(dict1)


print("\n", "="*40)

# ======================================================== #

# 8- Find Common Keys in Two Dictionaries 

# Write a Python program to find common keys in two dictionaries. 

# dict1 = {"a": 1, "b": 2, "c": 3} 

# dict2 = {"b": 2, "c": 4, "d": 5} 

#Output: {'b', 'c'}   

print("\n", "="*10, "Question 8", "="*10, "\n")

dict1 = {"a": 1, "b": 2, "c": 3}

dict2 = {"b": 2, "c": 4, "d": 5}


print(set(dict1.keys()).intersection(set(dict2.keys())))


print("\n", "="*40)

# ======================================================== #

# 9- takes a string and prints the longest 

# alphabetical ordered substring occured. 

# For example, if the string is 'abdulrahman' then the output is: 

# Longest substring in alphabetical order is: abdu    

print("\n", "="*10, "Question 9", "="*10, "\n")

str = "abdulrahman"

temp = [str[0]]
longest = []

for i in range(0, len(str) -1):
    if str[i + 1] >= str[i]:
        temp.append(str[i + 1])
        if len(temp) > len(longest):
            longest = temp
    else:
        temp = [str[i+1]]

print(''.join(longest))

print("\n", "="*40)