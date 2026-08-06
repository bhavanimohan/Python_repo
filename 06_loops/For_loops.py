# #Basic For Loops
# a=input()
# b = int(input())
# for char in range(b):
#     print(a)
    
# #For Loops in List 
# a=["apple","mango","grapes"] 
# for char in a:
#     print(char)
    
# #For Loops using conditional statements
# a = int(input())
# for char in range(a):
#     if char%2==0:
#         print(char)
        
# a = int(input())
# b=[]
# for char in range(1,a):
#     if char%5==0:
#         b+=[char]
# print(b)

# a = int(input())
# b=[]
# for char in range(1,a):
#     if char%5==0:
#         b.append(char)
# print(b)
        
        
# a = int(input())
# b = []
# for char in range(1,a):
#     if( char % 3==0 and char %5 ==0):
#         b.append("FizzBuzz")
#     elif (char % 5 ==0):
#         b.append("Buzz")
#     elif(char %3==0):
#         b.append("Fizz")
#     else:
#         b.append(char)
        
# print(b)

# a = int(input())
# list_3 = []
# list_5 = []
# list_Both = []
# for char in range(1,a):
#     if char % 3 == 0 and char % 5 == 0:
#         list_Both.append(char)
#         list_3.append(char)
#         list_5.append(char)
        
#     elif char % 3 == 0:
#         list_3.append(char)
#     elif char % 5 == 0:
#         list_5.append(char)
# print(list_Both)
# print(list_3)
# print(list_5)

# a = int(input())
# list_3 = []
# list_5 = []
# list_Both = []
# for char in range(1,a):
#     if char % 3 == 0 and char % 5 == 0:
#         list_Both.append(char)
        
        
#     if char % 3 == 0:
#         list_3.append(char)
#     if char % 5 == 0:
#         list_5.append(char)
# print(list_Both)
# print(list_3)
# print(list_5)
 
 
#  #from 1 to 10       
# a=int(input())
# for char in range(1,a):
#     print(char)

# #even numbers    
# a=int(input())
# for char in range(1,a):
#     if char % 2 == 0:
        
#         print(char)
     
# #odd numbers
# a=int(input())
# for char in range(1,a):
#     if char % 2 != 0:
        
#         print(char)

# #sum of digits
# a=int(input())
# count = 0
# for char in range(1,a):
#     count+=char
# print(count)

# #factorial
# a=int(input())
# count = 1
# for char in range(1,a+1):
#     count*=char
# print(count)

# #count of 1 and N are divisible by 3 and 5.
# a = int(input())
# count = 0
# for char in range(1,a):
#     if char % 3 == 0 and char % 5 == 0:
#         count+=1
# print(count)

#Reverse the digits of a given number.
# a = int(input())
# count = ""
# while(a>0):
#     b=a%10
#     count+=str(b)
#     a=a//10
# print(count)

#Find the sum of digits of a number.
# a=int(input())
# count = 0
# while(a>0):
#     b=a%10
#     count+=b
#     a//=10
# print(count)

#Check whether a number is Palindrome.
# a= input()
# count=""
# for char in a:
#     count=char+count
# if(a == count):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")
    
    
#Check whether a number is Armstrong.
# a = input()
# b = len(a)
# first=int(a[0])**2
# second = int(a[1])**2
# third = int(a[2])**2
# if a == first+second+third:
#     print("Armstrong")
# else:
#     print("Not a Armstrong")

#Print the multiplication table of a given number.
# a = int(input())
# for char in range(1,11):
#     print(f"{a} * {char} = {a*char}")
    
#Print multiplication tables from 1 to 10.
# a = int(input())
# for char in range(1,a+1):
#     for chars in range(1,11):
#         print(f"{char} * {chars} = {chars*char}")


#smaller and bigger number     
# a = int(input())
# small =[]
# bigger=[]
# for i in range(1,a+1):
#     if(i<=5):
#         small.append(i)
#     else:
#         bigger.append(i)
# print(small)
# print(bigger)

#Print all prime numbers between 1 and N.
a = int(input())


for i in range(2,a+1):
    is_prime = True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            is_prime = False
            break
    
    -if is_prime:
        print("Prime")
    else:
        print("Not a Prime")
        
        
n = int(input())

if n <= 1:
    print("Not Prime")
else:
    prime = True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime")
    else:
        print("Not Prime")