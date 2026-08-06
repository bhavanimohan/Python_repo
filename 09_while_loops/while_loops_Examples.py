#printing from 1 to 10 using while loop
# a = int(input("Enter the number : "))
# i =1
# while(i<=a):
#     print(i)
#     i+=1
#printing from 10 to 1 using while loop

# a = int(input("Enter the number : "))
# b = []
# while(a>0):
#     b.append(a)
    
#     a-=1
# print(b)

# a = int(input("Enter the number where to start the loop : "))
# b = int(input("Enter the number where to stop the loop : "))
# c = []
# while(a<b):
#     if(a%5==0):
#         c.append(a)
        
#     a+=1
# print(c)

#one more way to write the program is 
a = int(input("Enter the number where to start the loop : "))
b = int(input("Enter the number where to stop the loop : "))
while(a<b and a%5==0):
    print(a)
    a+=1