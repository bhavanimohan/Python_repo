# nums = [1, 2, 3, 4, 5]
# a = list(map(lambda x : x **2,nums))
# print(a)

# nums = [1, 2, 3, 4, 5]
# a = list(map(lambda x : x **3,nums))
# print(a)

# nums = [1, 2, 3, 4, 5]
# a = list(map(lambda x : x+10,nums))
# print(a)

# nums = [1, 2, 3, 4, 5]
# a = list(map(lambda x : x *5,nums))
# print(a)

# names = ["amit", "riya", "kabir"]
# a = list(map(lambda x : x.upper(),names))
# print(a)

# names = ["AMIT", "RIYA", "KABIR"]
# a = list(map(lambda x : x.lower(),names))
# print(a)

# words = ["hello", "world", "python"]
# a = list(map(lambda x : len(x),words))
# print(a)

nums = [1, 2, 3]
a = list(map(lambda x : str(x),nums))
print(a)

celsius = [0, 20, 37, 100]
a = list(map(lambda x : (x*(9/5))+32,celsius))
print(a)