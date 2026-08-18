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


def second_largest(numbers):
    first = 0
    second = 0
    for char in numbers:
        if char>first:
            second = first
            first = char
        if char>second and char!= first:
            second = char
    return second
print(second_largest([1,2,3,4,5]))