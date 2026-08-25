nums = [i for i in range(1,11)]
print(nums)

sq = [i**2 for i in range(1,5)]
print(sq)

names = ["nani","anu","sai","hari"]
res = [len(i) for i in names ]
print(res)

res = [i.upper() for i in names]
print(res)

res = [i.lower() for i in names]
print(res)

res = [i[0] for i in names]
print(res)

res = [i.title() for i in names]
print(res)

res = [i[-1] for i in names]
print(res)

numss = [1,2,3,4,5,6]
res = [i+10 for i in numss]
print(res)


res = [i for i in range(10,0,-1)]
print(res)

sq = [i**3 for i in range(10,20)]
print(sq)