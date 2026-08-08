# Write a program to print numbers from 1 to 10 using a for loop.
# a = int(input("Enter the number: "))
# for char in range(1,a+1):
#     print(char)
    
# Print all even numbers between 1 and 20 (inclusive).
# a = int(input("Enter the number: "))
# for char in range(1,a):
#     print(char)

# Calculate and print the sum of all numbers from 1 to 100.
# a = int(input("Enter the number: "))
# sum = 0
# for char in range(1,a+1):
#     sum+=char
# print(sum)

# Print each character of the string "PYTHON" on a new line.
# a = "PYTHON"
# for char in a:
#     print(char)

# Print the multiplication table of 5 (from 5 x 1 to 5 x 10).
# a = int(input("Enter the number: "))
# for char in range(1,11):
#     print(f"{a} x {char} = {a*char}")

# Count and print the number of vowels in the string "programming".
# a = "programming"
# count = 0
# for char in a:
#     if char in "aeiouAEIOU":
#         count+=1
# print(count)

# Find and print the sum of all elements in the list [4, 8, 15, 16, 23, 42].
# a = [4, 8, 15, 16, 23, 42]
# count = 0
# for char in a:
#     count+=char
# print(count)

# Print numbers from 10 down to 1 (in reverse order).
# a = int(input("Enter the number: "))
# for char in range(a,0,-1):
#     print(char)


# Print the word "Hello" exactly 5 times, once per line.
# a = "Hello"
# for char in range(5):
#     print(a)

# Find and print the largest number in the list [12, 45, 3, 67, 29] without using max().
# a = [12, 45, 3, 67, 29]
# count =0
# for char in a:
#     if(char>count):
#         count = char
# print(count)


# Find and print the second largest number in the list [12, 45, 3, 67, 29] without using max().
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

# Write a program that checks whether a given number is prime using a for loop.
# a = int(input("Enter the number: "))
# count =0
# for char in range(2,a):
#     if(a %char == 0):
#         count +=1
# if (count!= 0):
#     print("Not a prime number")
# else:
#     print("Prime numberr")
    
    
# Print the first n terms of the Fibonacci series (take n as an input, e.g. n = 10).
# n = int(input("Enter the number : "))
# a =0
# b =1
# for char in range(1,n+1):
#     print(a)
#     c = a+b
#     a = b
#     b =c

# Find the factorial of a given number using a for loop (e.g. factorial of 6).
# a = int(input("Enter the number : "))
# count = 1
# for char in range(1,a+1):
#     count*=char
# print(count)

    
# Count how many times each character appears in the string "success" and store the result in a dictionary.
# a = input("Enter something : ")
# b = []
# for char in a:
#     print(char, ":", a.count(char))
#     b.append(char)

# Print a right-angled triangle pattern of stars (*) with 5 rows, e.g.:
# a = int(input("Enter the number : "))
# for char in range(1,a+1):
#     print("*" * char)

# Find the sum of the digits of a given number (e.g. 4827 -> 4+8+2+7 = 21).
# a = int(input("Enter the number : "))
# count = 0
# while(a>0):
#     count = count+a%10
#     a//=10
# print(count)

# Reverse a list, e.g. [1, 2, 3, 4, 5], without using the built-in reverse() or slicing.
# a = [1, 2, 3, 4, 5]
# b = []
# for char in a:
#     b=[char]+b
# print(b)

# Find the second largest number in the list [23, 45, 12, 67, 34, 67, 8].


# a = [23, 45, 12, 67, 34, 67, 8]
# first = -1
# second = -1

# for char in a:
#     if(char > first):
#         second = first
#         first = char

#     if(char>second and char != first):
#         second = char
# print(second)

# #Print all prime numbers between 1 and 50.
# a = int(input("Enter the number : "))

# count= []
# b= 0
# for char in range(1,a+1):
#     if(a%char == 0):
#         count.append(char)
        
# print(count)

# #19. Print all prime numbers between 1 and 50.
# print("-----Question 19 -----")
# for i in range(1,51):
#     flag=True
#     for j in range(2,i):
#         if i%j==0:
#             flag=False
#     if flag:
#         print(i)

# #20. Count the number of even and odd numbers separately in the list [3, 8, 12, 5, 19, 22, 7].
# print("-----Question 20 -----")
# list_1=[3,8,12,5,19,22,7]
# odd_cnt=0
# even_cnt=0
# for i in list_1:
#     if i%2==0:
#         even_cnt+=1
#     else:
#         odd_cnt+=1
# print("Total even numbers are :",even_cnt)
# print("Total odd numbers are :",odd_cnt)

# #21. Convert a list of Celsius temperatures [0, 20, 37, 100] to Fahrenheit and print the results.

# print("-----Question 21 -----")
# list_1=[0,20,37,100]
# for i in list_1:
#     a=int((i* 9/5 )+32)
#     print(f"{i} Celsius = {a} Fahrenheit")


# #22. Find and print the common elements between two lists: [2, 4, 6, 8, 10] and [3, 6, 9, 12, 8].
# print("-----Question 22 -----")
# list_1=[2,4,6,8,10]
# list_2=[3,6,8,9,12]
# for i in list_1:
#     if i in list_2:
#         print(i)

# #23. Check whether a given string, e.g. "madam", is a palindrome.
# print("-----Question 23 -----")
# string=input("Enter a String :")
# temp=string[::-1]
# if string==temp:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# #24. Print multiplication tables for all numbers from 1 to 10 (use a nested for loop).
# print("-----Question 24 -----")
# for i in range(1,11):
#     print(f"***Multiple of {i}***")
#     for j in range(1,11):
#         print(f"{i} X {j} = {i*j}")

# #25. Find the average of the numbers in the list [12, 15, 20, 24, 30, 18].
# print("-----Question 25 -----")
# list_1=[12,15,20,24,30,18]
# sum=0
# n=len(list_1)
# for i in list_1:
#     sum+=i
# print("Average of the no. is :",sum/n)


# #26. Print a number pyramid pattern with 5 rows, e.g.
# print("-----Question 26 -----")
# n=int(input("Enter a Number :"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# # 27. Given the list [10, 15, 3, 7, 8, 12] and a target sum of 18, find and print all pairs of numbers that add up to the target (using nested for loops).
# print("-----Question 27 -----")
# list_1=[10,15,3,7,12]
# target=int(input("Enter a target number :"))
# result=[]
# for i in range(len(list_1)):
#     for j in range(i,len(list_1)):
#         Sum=list_1[i]+list_1[j]
#         if i!=j and Sum==target:
#             a=[list_1[i],list_1[j]]
#             result.append(a)
# print(result)

# #30. Implement Bubble Sort on the list [29, 10, 14, 37, 13]
# print("-----Question 30 -----")
# list_1=[29, 10, 14, 37, 13]
# for i in range(len(list_1)):
#     for j in range(1,len(list_1)-i):
#         if list_1[j-1]>list_1[j]:
#             list_1[j-1],list_1[j]=list_1[j],list_1[j-1]
#     print(list_1)
    
    
    
    
# a = int(input("Enter the number : "))
# count = 0
# while(a>0):
#     a%10
#     a//=10
#     count+=1
# print(count)