# a = ["nani","rajesh","jai","suresh","naresh"]
# b = list(filter(lambda x : len(x) > 4 , a))
# print(b)

# names = ["nani","aravind","ganesh","rajesh","jai","abhi","mahesh","avinash"]
# print(list(filter(lambda x : x.startswith("a") ,names)))

# names = ["nani","aravind","ganesh","rajesh","jai","abhi","mahesh","avinash"]
# print(list(filter(lambda x : x.endswith("sh") ,names)))
# a = [1,-8,-4,7,8,5,-10,-6]
# print(list(filter(lambda x : x>0 ,a )))
# print(list(filter(lambda x : x<0 ,a )))


# a = [1,-8,-4,7,8,5,-10,-6]
# print(list(filter(lambda x : x>0 ,a )),list(filter(lambda x : x<0 ,a )))


# print("----------------------------- REDUCE -------------------------------")
from functools import reduce
nums = [1,2,3,4,5]
res = reduce(lambda a, b: a if(a>b) else b , nums)
print(res)