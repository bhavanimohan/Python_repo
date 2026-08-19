
# def factorial(num):
#     count = 1
#     while(num>0):
#         count*=num
#         num-=1
#     return count
# print(factorial(5))


# def factorial(num):
#     if num == 0 :
#         return 1
#     return num * factorial(num-1)
# print(factorial(5))

# def factorial(num):
#     count = 1
#     if num == 0:
#         return 1
#     count=num*factorial(num-1)
#     return count
# print(factorial(5))

a = lambda x: 'Even' if x % 2 == 0 else 'Odd'
print(a(6))