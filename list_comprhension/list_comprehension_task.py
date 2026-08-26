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

words = ["python", "java", "react", "javascript", "html", "css"]
result = [w.upper() for w in words if len(w) > 4]
print(result)

students = [
{"name": "Ram", "marks": 80},
{"name": "Sam", "marks": 35},
{"name": "Raj", "marks": 90},
{"name": "John", "marks": 45}
]
names = [s["name"] for s in students]
print(names)

marks = [s["marks"] for s in students]
print(marks)

passed = [s["name"] for s in students if s["marks"] >= 40]
print(passed)

top_students = [s["name"] for s in students if s["marks"] > 75]
print(top_students)

failed = [s["name"] for s in students if s["marks"] < 40]
print(failed)

formatted = [f'{s["name"]} - {s["marks"]}' for s in students]
print(formatted)

r_marks = [s["marks"] for s in students if s["name"].startswith("R")]
print(r_marks)

result = [x**2 for x in range(1, 51) if x % 2 == 0 and x > 20]
print(result)

words = ["python", "java", "react", "javascript", "html", "css"]
result = [w.upper() for w in words if len(w) > 5]
print(result)

students = [
{"name": "Ram", "marks": 85},
{"name": "Sam", "marks": 35},
{"name": "Raj", "marks": 72},
{"name": "John", "marks": 28},
{"name": "Kiran", "marks": 90}
]
result = [s for s in students if s["marks"] >= 60]
print(result)

data = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]
]
result = [x for row in data for x in row if x % 2 == 0]
print(result)

students = [
{"name": "Ram", "marks": [80, 75, 90]},
{"name": "Sam", "marks": [35, 40, 45]},
{"name": "Raj", "marks": [90, 85, 95]}
]
totals = [sum(s["marks"]) for s in students]
print(totals)

all_marks = [m for s in students for m in s["marks"]]
print(all_marks)

high_marks = [m for s in students for m in s["marks"] if m > 70]
print(high_marks)

top_names = [s["name"] for s in students if sum(s["marks"]) > 200]
print(top_names)

max_marks = [max(s["marks"]) for s in students]
print(max_marks)

result = ["Pass" if sum(s["marks"]) >= 200 else "Fail" for s in students]
print(result)

print("------------------------------------ SET ---------------------------")
res = {num**2 for num in range(1,11)}
print(res)

res = {num for num in range(1,21 )if num % 2 == 0}
print(res)

num = [1,2,2,3,4,4,5,1]
res  = {i for i in num}
print(res)

n = "comprehension"
res = {i for i in n if i in "aeiou"}
print(res)

n = ["apple","banana", "cherry", "apple", "avocado"]
res = {i[0] for i in n}
print(res)

sq = {i**2 for i in range(-5,6)}
print(sq)

res = {i % 3 for i in range(1,21) }
print(res)

a =[1, 2, 3, 4, 5] 
b =[4, 5, 6, 7,8]

c = {i for i in a for j in b if i == j}
print(c)


num = ["cat", "dog", "apple","banana", "fig"]
res = {len(i) for i in num}
print(res)

num = [8, 12, 15, 16, 20, 21, 24]
res = {i for i in num if i % 4 == 0}
print(res)

res = {i : i**2 for i in range(1,6)}
print(res)

res = {i : i**3 for i in range(1,11)}
print(res)

names = ["python", "java","react"]
res = {i : len(i) for i in names}
print(res)

res = {i: "Even" if i % 2 == 0 else "Odd" for i in range(1,11)}

print(res)


keys = ["a", "b", "c"]
values =[1, 2, 3]
res = {i : j for i in keys for j in values}
print(res)

prices = {"apple": 40, "banana": 60, "mango": 90, "grape": 30}
res = {i: prices[i] for i in prices if   prices[i]> 50}
print(res)

num= {"a": 1, "b": 2, "c": 3}
res = {values : keys  for keys,values in num.items()}
print(res)

num = "abc"
res = {i : ord((i)) for i in num}
print(res)

res = { i : i **2  for i in range(1,11) if i % 2 == 0}
print(res)

pairs = [("a", 1), ("b", 2), ("c", 3)]

result = {key: value for key, value in pairs}

print(result)

original = {"x": 10, "y": 20, "z": 30}
res = {key: values * 2 for key,values in original.items()}
print(res)

marks = {"Ram": 80, "Sam": 35, "Raj": 90, "John": 45}
res = {i : "pass" if marks[i] > 50 else "fail" for i in marks}
print(res)

num =  ["cat","dog", "fish"]
res = {i : i.upper() for  i in num}
print(res)

words = ["apple", "sky", "orange", "gym"]
result = {word: sum(1 for char in word if char in "aeiou") for word in words}
print(result)

nums = {"a": 1, "b": 2, "c": 3, "d": 4}
res = {i:nums[i] for i in nums if nums[i] % 2 == 0}
print(res)

