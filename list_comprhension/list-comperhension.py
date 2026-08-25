# nums = [i for i in range(1,11)]
# print(nums)

# sq = [i**2 for i in range(1,5)]
# print(sq)

# names = ["nani","anu","sai","hari"]
# res = [len(i) for i in names ]
# print(res)

# res = [i.upper() for i in names]
# print(res)

# res = [i.lower() for i in names]
# print(res)

# res = [i[0] for i in names]
# print(res)

# res = [i.title() for i in names]
# print(res)

# res = [i[-1] for i in names]
# print(res)

# numss = [1,2,3,4,5,6]
# res = [i+10 for i in numss]
# print(res)


# res = [i for i in range(10,0,-1)]
# print(res)

# sq = [i**3 for i in range(10,20)]
# print(sq)


res = [i for i in range(1,11) if i % 2 == 0 ]
print(res)

res = [i for i in range(1,11) if i % 2 != 0]
print(res)

res = [i for i in range(1,100) if i % 3 == 0]
print(res)

res = [i for i in range(1,100) if i % 5 == 0]
print(res)

res = [i for i in range(1,100) if (i % 3 == 0 and i % 5 == 0)]
print(res)

numbers = [2,3,4,66,77,88,999,22,33,55,66]
res = [i for i in numbers if (i>10)]
print(res)

num = 5
res = [i for i in range(1,10) if num % i == 0]

nums = [2,3,6,8,9,1]
res =["even","odd","even","even","even","odd","odd"]
result = ["Even" if i % 2 == 0  else "Odd"for i in nums ]
print(result)
