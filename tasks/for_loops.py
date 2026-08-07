#1. Write a program to print numbers from 1 to 10 using a while loop
# a = int(input("Enter the numberr : "))
# for char in range(1,a+1):
#     print(char)

# Print all even numbers between 1 and 20 (inclusive) using a while loop.
# a = int(input("Enter the numberr : "))
# count =1
# while(a>0):
#     print(count)
#     count+=1
#     a-=1
    
#Calculate and print the sum of all numbers from 1 to 50 using a while loop
# a = int(input("Enter the number : "))
# count = 0
# while(a>0):
#     a-=1
#     count+=a
    
# print(count)

#Print each character of the string "PYTHON" on a new line using a while loop
# a = input("Enter the text : ")
# count =0

# while count<len(a):
#     print(a[count])
#     count+=1

# Print the multiplication table of 7 (from 7 x 1 to 7 x 10) using a while loop.
# a = int(input("Enter the number : "))
# count = 1
# while(count<11):
#     print(f"{count} * {a} = {count * a}")
#     count+=1

# Print the word "Hello" exactly 5 times, once per line, using a while loop.
# a = input("Enter the text : ")
# b = int(input("Enter the nunmber : "))

# count = 0
# while(count<b):
#     print(a * 1)
#     count+=1
    
# Find the factorial of a given number using a while loop (e.g. factorial of 5).

# a = int(input("Enter the number : "))
# count = 1
# while(a>0):
#     count*=a
#     a-=1
# print(count)

# Print numbers from 10 down to 1 (in reverse order) using a while loop.
# a = int(input("Enter the number : "))
# count = 0
# while(a>0):
#     print(a)
#     a-=1
    
    
# Count and print the number of digits in a given number (e.g. 34521 has 5 digits) using a while loop
# a = int(input("Enter the number : "))
# count =0
# while(a>0):
#     a%10
#     a//=10
#     count+=1
# print(count)

# Use a while loop with a break statement to stop printing numbers from 1 to 10 as soon as the number 7
# is reached.

# a = int(input("Enter the number : "))
# countss = int(input("Enter the number that you want to change : "))
# count =1
# while(a>0):
#     if(count == countss):
#         break
#     a-=1
    
    
#     print(count)
#     count +=1

#  Use a continue statement inside a while loop to print only the odd numbers from 1 to 20.
# a = int(input("Enter the number : "))
# count = 0
# while(count<a):
#     if(count % 2 == 0):
        
#         count+=1
#         continue
        
    
#     print(count)
#     count+=1
        
        
# Write a while loop that prints numbers from 1 to 20 but skips (using continue) any number that is a
# multiple of 3.

# a = int(input("Enter the number : "))
# count =1
# while(count<a):
#     if(count % 3 == 0):
#         count+=1
#         continue
#     print(count)
#     count+=1

        
#Reverse a given number using a while loop, e.g. 1234 → 4321 (without converting it to a string)
# a = int(input("Enter the number : "))

# count = 0
# while(a>0):
#     count=count*10+a%10
#     a//=10
# print(count)

# Check whether a given number is an Armstrong number using a while loop (e.g. 153 = 1³ + 5³ + 3³)
# a = int(input("Enter the number : "))
# b = a
# count = 0
# while(a>0):
#     c=a%10
#     count=count+c**3
#     a//=10
    
# print(count)
# if(b == count):
#     print("Armstrong Number")
# else:
#     print("Not a Armstrong Number")

#  Find the digital root of a number (repeatedly sum its digits until a single digit remains) using a while loop,
# e.g. 9875 → 29 → 11 → 2.

# a = int(input("Enter the number : "))

# while(a>10):
#     count= 0
#     while(a>0):
        
#         b = a%10
#         count+=b
#         a//=10
#     a=count
# print(a)

# Use a while loop with break to find the first number between 1 and 1000 that is divisible by both 7 and 5.

# a= int(input("Enter the number : "))
# count =1
# while(a>0):
#     if(count % 5 == 0 and count % 7 == 0):
#         print(count)
#         break
#     count+=1
    
    
# Simulate a number-guessing game: given the guesses [34, 60, 45, 50] and the secret number 45, use a
# while loop with break to stop as soon as the correct guess is found, printing how many attempts it took   

# a = [34, 60, 45, 50]
# b = int(input("Enter the number : "))
# count = 0
# while(count<len(a)):
#     if(a[count]  == b):
#         break
#     count+=1
# print(count)

# Print the first n terms of the Fibonacci series using a while loop (take n = 10).
# a = int(input("Enter the number : "))
# first = 0
# second =1
# b = []
# while(a>0):
#     b.append(first)
#     third = first +second
#     first = second
#     second = third
#     a-=1
    
#print(b)

# Use a while–else loop to check whether a given number is prime, printing "Prime number" from the else
# block only if the loop completes without finding a factor (no break triggered).
# a = int(input("Enter the number : "))
# count = countss = 0 
# while(count<a):
#     count+=1
#     if(a % count == 0 ):
#         countss+=1
        
# if(countss==2):
#     print("Prime Number")
# else:
#     print("Not a Prime Number")

# Given the list [12, 45, 3, 67, 29, 90, 8], use a while loop with an index variable to find the first number
# greater than 50, print it, and then break out of the loop.

# a = [12, 45, 3, 67, 29, 90, 8]
# b = int(input("Enter the number : "))
# count = 0
# flag = True
# while flag:
#     if(a[count] > b):
#         print(count)
#         break
#     count+=1
    
    
# Use a continue statement inside a while loop to print only the consonants of the string "programming"
# (skip the vowels).

# a = input("Enter the name : ").lower()
# count = 0
# while(count<len(a)):
#     if(a[count] in "aeiou"):
#         count+=1
#         continue
#     else:
#         print(a[count])
#         count+=1
        
# Implement a countdown timer from 10 to 1 using a while loop that prints "Liftoff!" once the countdown
# reaches 0.
a = int(input("Enter the number : "))
count = 0
while(a>0):
    if(a>0):
        print(a)
        a-=1
else:
    print("Liftoff!!!!")
    
