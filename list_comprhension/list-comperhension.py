#List comperhension

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


# res = [i for i in range(1,11) if i % 2 == 0 ]
# print(res)

# res = [i for i in range(1,11) if i % 2 != 0]
# print(res)

# res = [i for i in range(1,100) if i % 3 == 0]
# print(res)

# res = [i for i in range(1,100) if i % 5 == 0]
# print(res)

# res = [i for i in range(1,100) if (i % 3 == 0 and i % 5 == 0)]
# print(res)

# numbers = [2,3,4,66,77,88,999,22,33,55,66]
# res = [i for i in numbers if (i>10)]
# print(res)

# num = 5
# res = [i for i in range(1,10) if num % i == 0]

# nums = [2,3,6,8,9,1]
# result = ["Even" if i % 2 == 0  else "Odd" for i in nums ]
# print(result)


# nums = [2,3,4,-4,-5,-6,-7,-8,2,4]
# res = ["Positive" if i > 0 else "Negative" for i in nums]
# print(res)

# marks=[60,76,23,45,78,89,12,99,32]
# res =  ["pass" if i>50 else "fail" for i in marks]
# print(res)


# names = ["harish","balaram","anil","vishnu","ameya","pichidhi","mottu","sontash"]
# res = [i for i in names if len(i) > 5]
# print(res)

# nums = [[1,3,2],[3,4,5],[4,2,9]]
# res = [j 
#        for i in nums for j in i if j% 2 == 0]
# print(res)

#dictionary comperhension started

res = [1,2,3,4,5]
result = {i:i**3 for i in res}
print(result)

techs = ["python","react","java","js","html"]
res = {i: len(i) for i in techs}
print(res)

res = {i:i**2 for i in range(20,31) if i%2==0}
print(res)

nums = [60,70,80,90,20,30,40,10,50]
res = {i : i + 5 for i in nums if i>50}

print(res)

nums = [1,2,4,6,8,9]
res = {i :"even" if i % 2 == 0 else "odd" for i in nums}
print(res)