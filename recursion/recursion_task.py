a = lambda x: 'Even' if x % 2 == 0 else 'Odd'
print(a(6))

a = lambda x : "Positive" if x>0 else "Negative" if x<0 else "Zero"
print(a(6))

a = lambda x : x**2
print(a(3))

a = lambda x : x**3
print(a(3))

a = lambda a , b : a+b
print(a(4,5))

a = lambda a, b : a if (a>b) else b
print(a(5,7))

a = lambda a : len(a)
print(a("Bhavani Mohan"))

a = lambda a : "True" if a == a[::-1] else "False"
print(a("mom"))

a = lambda a : "Vowel" if a in 'aeiouAEIOU' else "Consonant"
print(a("e"))

a = lambda x :  (x * 9/5) + 32 
print(a(100))

a = lambda numbers : list(filter(lambda x: x % 2 == 0, numbers))
print(a([1,2,3,4,5,6]))


a = lambda numbers : list(map(lambda x: x ** 2, numbers))
print(a([1,2,3,4]))

from functools import reduce;
a = lambda numbers : reduce(lambda a, b: a + b, numbers)
print(a([1, 2, 3, 4, 5]))

a = lambda  data : sorted(data, key=lambda item: item[1])
print(a([('A', 88), ('B', 45), ('C', 67)]))

a =  lambda x : "True" if (x % 3 == 0 and x % 5 == 0) else "False"
print(a(30))
