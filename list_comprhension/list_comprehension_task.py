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

words = ["cat", "python", "java", "javascript", "dog"]
result = [len(w) for w in words if len(w) > 4]
print(result)

result = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print(result)

result = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print(result)

nums = [10, -5, 8, -2, -7, 15]
result = ["Positive" if x > 0 else "Negative" for x in nums]
print(result)

marks = [45, 78, 32, 90, 25, 67]
result = ["Pass" if m >= 40 else "Fail" for m in marks]
print(result)

nums = [12, 7, 9, 20, 33, 44]
result = ["Even" if x % 2 == 0 else "Odd" for x in nums]
print(result)

nested = [[1, 2], [3, 4], [5, 6]]
flat = [x for sub in nested for x in sub]
print(flat)

nested = [[10, 20, 30], [40, 50], [60, 70, 80]]
flat = [x for sub in nested for x in sub]
print(flat)

nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [x for sub in nested for x in sub if x % 2 == 0]
print(result)

nested = [[1, 2], [3, 4], [5, 6]]
result = [x**2 for sub in nested for x in sub]
print(result)

result = [(x, y) for x in [1, 2, 3] for y in ["A", "B"]]
print(result)

students = ["Ram", "Sam"]
courses = ["Python", "Java", "React"]
result = [(s, c) for s in students for c in courses]
print(result)

result = [x for x in range(1, 60) if x > 10 and x < 50]
print(result)

words = ["apple", "ant", "animal", "ball", "angle", "cat"]
result = [w for w in words if w.startswith("a") and len(w) > 3]
print(result)