# a = lambda x: 'Even' if x % 2 == 0 else 'Odd'
# print(a(6))

# a = lambda x : "Positive" if x>0 else "Negative" if x<0 else "Zero"
# print(a(6))

# a = lambda x : x**2
# print(a(3))

# a = lambda x : x**3
# print(a(3))

# a = lambda a , b : a+b
# print(a(4,5))

# a = lambda a, b : a if (a>b) else b
# print(a(5,7))

# a = lambda a : len(a)
# print(a("Bhavani Mohan"))

# a = lambda a : "True" if a == a[::-1] else "False"
# print(a("mom"))

# a = lambda a : "Vowel" if a in 'aeiouAEIOU' else "Consonant"
# print(a("e"))

# a = lambda x :  (x * 9/5) + 32 
# print(a(100))

# a = lambda numbers : list(filter(lambda x: x % 2 == 0, numbers))
# print(a([1,2,3,4,5,6]))


# a = lambda numbers : list(map(lambda x: x ** 2, numbers))
# print(a([1,2,3,4]))

# from functools import reduce;
# a = lambda numbers : reduce(lambda a, b: a + b, numbers)
# print(a([1, 2, 3, 4, 5]))

# a = lambda  data : sorted(data, key=lambda item: item[1])
# print(a([('A', 88), ('B', 45), ('C', 67)]))

# a =  lambda x : "True" if (x % 3 == 0 and x % 5 == 0) else "False"
# print(a(30))


#----------------------session - B----------------------------

# def  sum_natural(n):
#     count=0
#     if n ==0:
#         return 0
#     count = n + sum_natural(n - 1)
#     return count
# print(sum_natural(5))

# def fibonacci(n):
#     count =0
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     count = fibonacci(n-1) + fibonacci(n-2)
#     return count
# print(fibonacci(6))

# def sum_of_digits(n):
#     count =0
#     if n<10:
#         return n
#     count+=n%10 +sum_of_digits(n//10)
#     return count
# print(sum_of_digits(1234))

# def power(base, exp):
#     count =0
#     if exp ==0:
#         return 1
#     count =  base * power(base, exp - 1)
#     return count
# print(power(2,5))

def reverse_string(s):
    if s == "":
        return s
    return reverse_string(s[1:]) + s[0]
     
print(reverse_string("HELLO"))