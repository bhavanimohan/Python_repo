numbers = [x for x in range(1, 11)]
print(numbers)

numbers = [x for x in range(1, 21)]
print(numbers)

squares = [x**2 for x in range(1, 11)]
print(squares)

cubes = [x**3 for x in range(1, 11)]
print(cubes)

doubled = [x * 2 for x in range(1, 11)]
print(doubled)

reverse_nums = [x for x in range(10, 0, -1)]
print(reverse_nums)

multiples = [5 * x for x in range(1, 11)]
print(multiples)

words = ["python", "java", "react", "django"]
lengths = [len(w) for w in words]
print(lengths)

words = ["python", "java", "react", "django"]
upper_words = [w.upper() for w in words]
print(upper_words)

words = ["apple", "banana", "mango", "orange"]
first_chars = [w[0] for w in words]
print(first_chars)

evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

odds = [x for x in range(1, 21) if x % 2 != 0]
print(odds)

div_by_5 = [x for x in range(1, 51) if x % 5 == 0]
print(div_by_5)

nums = [5, 12, 8, 20, 3, 15, 7, 25]
result = [x for x in nums if x > 10]
print(result)

names = ["Ram", "Suresh", "John", "Prakash", "Raj"]
result = [n for n in names if len(n) > 4]
print(result)

result = [x**2 for x in range(1, 21) if x % 2 == 0]
print(result)

result = [x**3 for x in range(1, 11) if x % 2 != 0]
print(result)

nums = [2, 5, 8, 10, 3, 12, 7]
result = [x * 2 for x in nums if x > 5]
print(result)