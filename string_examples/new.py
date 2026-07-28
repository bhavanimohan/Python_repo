
a = "mohan"
# print(a[:-4:-1])
# print(a[:-6:-2])
# print(a[::])
# print(a[::])
a = "   Bhavani Mohan   "
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(len(a))
# print(a.strip()) # removes leading and trailing whitespace
# print(len(a.strip()))
# print(a.replace("Mohan", "Kumar"))
# print(a.title()) # title() method returns a string where the first character of each word is capitalized and all other characters are in lowercase.

# print(a.count("a")) #count() method returns the number of occurrences of a specified substring in the string. In this case, it counts the number of times the letter "a" appears in the string.
# print(a.find("i"))  #find() method returns the index of the first occurrence of the specified substring. If the substring is not found, it returns -1.
# print(a.index("i"))  #index() method returns the index of the first occurrence of the specified substring. If the substring is not found, it raises a ValueError.   
# print(a.startswith("Bha"))  #startswith() method checks if the string starts with the specified prefix. It returns True if the string starts with the prefix, and False otherwise.
# print(a.endswith("Mohan"))  #endswith() method checks if the string ends with the specified suffix. It returns True if the string ends with the suffix, and False otherwise.
# print(len(a.lstrip()))  #lstrip() method removes leading whitespace from the string.
# print(len(a.rstrip()))  #rstrip() method removes trailing whitespace from the string.
# print(len(a.strip()))   #strip() method removes both leading and trailing whitespace from the string.

print(a.split(" ")) #split() method splits the string into a list of substrings, using the specified separator (in this case, a space). The result is a list containing the individual words in the string.
 
print(a.isupper()) #isupper() method checks if all the characters in the string are uppercase letters. It returns True if all characters are uppercase, and False otherwise.
print(a.islower()) #islower() method checks if all the characters in the string are lowercase letters. It returns True if all characters are lowercase, and False otherwise.
a = "abc"
print(a.isalpha()) #isalpha() method checks if all the characters in the string are alphabetic letters. It returns True if all characters are alphabetic, and False otherwise.

a = "abc123"
print(a.isalnum()) #isalnum() method checks if all the characters in the string are alphanumeric (letters and numbers). It returns True if all characters are alphanumeric, and False otherwise.

print(a.isdigit()) #isdigit() method checks if all the characters in the string are digits. It returns True if all characters are digits, and False otherwise.


a = "   Bhavani Mohan   "
print(a.split(" ", 1)) #splits the string into a list of substrings, using the specified separator (in this case, a space) and a maximum number of splits (in this case, 1). The result is a list containing two elements: the first element is the substring before the first space, and the second element is the substring after the first space.


print(a.split(" ",2))

print(a.split(" ", 3))


a = ["my", "name", "is", "mohan"]  #join() method is used to join the elements of a list into a single string, with a specified separator between each element. In this case, the separator is "-->".
print("-->".join(a))

a = ["my", "name", "is", "mohan"]
b = "".join(a)[8:14].upper()  #join() method is used to join the elements of a list into a single string, with a specified separator between each element. In this case, the separator is a space.

print(b)  #join() method is used to join the elements of a list into a single string, with a specified separator between each element. In this case, the separator is a space.
b = "nani"
print(b.swapcase())