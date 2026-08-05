#Write a program to print numbers from 1 to 10 using a for loop.
# a = int(input("Enter the number: "))
# for char in range(1,a+1):
#     print(char)
    
#Print all even numbers between 1 and 20 (inclusive).
# a = int(input("Enter the number: "))
# for char in range(1,a):
#     print(char)

#Calculate and print the sum of all numbers from 1 to 100.
# a = int(input("Enter the number: "))
# sum = 0
# for char in range(1,a+1):
#     sum+=char
# print(sum)

#Print each character of the string "PYTHON" on a new line.
# a = "PYTHON"
# for char in a:
#     print(char)

#Print the multiplication table of 5 (from 5 x 1 to 5 x 10).
# a = int(input("Enter the number: "))
# for char in range(1,11):
#     print(f"{a} x {char} = {a*char}")

#Count and print the number of vowels in the string "programming".
# a = "programming"
# count = 0
# for char in a:
#     if char in "aeiouAEIOU":
#         count+=1
# print(count)

#Find and print the sum of all elements in the list [4, 8, 15, 16, 23, 42].
# a = [4, 8, 15, 16, 23, 42]
# count = 0
# for char in a:
#     count+=char
# print(count)

#Print numbers from 10 down to 1 (in reverse order).
# a = int(input("Enter the number: "))
# for char in range(a,0,-1):
#     print(char)


# Print the word "Hello" exactly 5 times, once per line.
# a = "Hello"
# for char in range(5):
#     print(a)

#Find and print the largest number in the list [12, 45, 3, 67, 29] without using max().
# a = [12, 45, 3, 67, 29]
# count =0
# for char in a:
#     if(char>count):
#         count = char
# print(count)


#Find and print the second largest number in the list [12, 45, 3, 67, 29] without using max().
# a = [12, 45, 3, 67, 29, 55]
# first =0
# second = 0
# third = 0
# for char in a:
#     if(char>first):
#         third = second
#         second = first
#         first = char
#     elif(char>second and char != first):
#         third=second
#         second = char
#     elif (char>third and char!= second and char!= first):
#         third =char
# print(first)
# print(second)
# print(third)

# a = [12, 45, 3, 67, 29, 55]
# first = second = third = float('-inf')

# for char in a:
#     if char > first:
#         third = second
#         second = first
#         first = char
#     elif char > second and char != first:
#         third = second
#         second = char
#     elif char > third and char != second and char != first:
#         third = char

#     print(third)


#Write a program that checks whether a given number is prime using a for loop.
# a = int(input("Enter the number: "))
# count =0
# for char in range(2,a):
#     if(a %char == 0):
#         count +=1
# if (count!= 0):
#     print("Not a prime number")
# else:
#     print("Prime numberr")
    
    
#Print the first n terms of the Fibonacci series (take n as an input, e.g. n = 10).
# n = int(input("Enter the number : "))
# a =0
# b =1
# for char in range(1,n+1):
#     print(a)
#     c = a+b
#     a = b
#     b =c

#Find the factorial of a given number using a for loop (e.g. factorial of 6).
# a = int(input("Enter the number : "))
# count = 1
# for char in range(1,a+1):
#     count*=char
# print(count)

    
#Count how many times each character appears in the string "success" and store the result in a dictionary.
# a = input("Enter something : ")
# b = []
# for char in a:
#     print(char, ":", a.count(char))
#     b.append(char)