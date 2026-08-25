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