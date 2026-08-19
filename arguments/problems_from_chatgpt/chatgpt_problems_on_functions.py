# def primes_in_range(start, end):
#     empty_list = []
    
#     for char in range(start,end+1):
#         count = 0
#         for charss in range(1,char+1):
#             if char % charss == 0:
#                 count +=1
#         if count ==2 :
#             empty_list.append(char)
#     return empty_list
     
# print(primes_in_range(10,30))


# def count_characters(text):
#     captial = small = num = special = 0

#     for char in text:
#         if char.isupper():
#             captial += 1
#         elif char.islower():
#             small += 1
#         elif char.isdigit():
#             num += 1
#         else:
#             special += 1

#     return captial, small, num, special


# captial, small, num, special = count_characters("Hello@123")

# print(f"Capital: {captial}")
# print(f"Small: {small}")
# print(f"Number: {num}")
# print(f"Special: {special}")


# def second_largest(numbers):
#     first = 0
#     second = 0
#     for char in numbers:
#         if char>first:
#             second = first
#             first = char
#         if char>second and char!= first:
#             second = char
#     return second
# print(second_largest([1,2,3,4,5]))

# def remove_duplicates(*numbers):
#     empty_list = []
#     for char in numbers:
#         if char not in empty_list:
#             empty_list.append(char)
        
#     return empty_list
# print(remove_duplicates(1,2,3,1,2,3,4,5,6))

# def analyze_number(n):
#     res = ""
#     if n > 0 and n % 2 == 0:
#         res = "Positive Even"
#     elif n>0 and n%2 != 0:
#         res = "Positive Odd"
#     elif n<0 and n % 2 == 0:
#         res = "Negative Even"
#     elif n<0 and n%2!= 0:
#         res = "Negative Odd"
#     else:
#         res = "Zero"
#     return res
# print(analyze_number(-7))


# def frequency(numbers):
#     count = {}
#     for char in numbers:
#         if char not in count:
#             count[char] = numbers.count(char)
#     return count
# print(frequency([1,2,3,4,5,3,2,1,1,2,3]))

#yesturday's class lamda just a re-cap
sums = lambda a,b : a+b
print(sums(2,3))
#if else condtional statements checking 
even = lambda a : "Even" if a % 2 == 0 else "Odd"
print(even(9))