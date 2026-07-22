a = {2,3,5,6,7,2,3,5,6,7,"python",None,True}
a.add("programming language")
print(a)

a = {2,3,5,6,7,2,3,5,6,7,"python",None,True}

a.update({"Nani"})
          
print(a)

a ={2,3,5}
b={7,3,5,8,9}
a.union(b)
print(a|b)

a ={2,3,5}
b={7,3,5,8,9}
a.intersection(b)
print(a & b)

a ={2,3,5}
b={7,3,5,8,9}
a.difference(b)
print(a -b)

a ={2,3,5}
b={7,3,5,8,9}
a.symmetric_difference(b)
print(a^b)

a ={2,3,5}
b={7,3,5,8,9}

print(a.isdisjoint(b))


a ={2,3,5}
b={7,3,5,8,9}
print(a.issubset(b))

a ={2,3,5}
b={7,3,5,8,9}
print(a.issuperset(b))

a = {"nani":60,"hari":90}
print(a["nani"],a["hari"])
print(a["nani"])
print(a.keys())
print(a.values())
print(a.items())

a = frozenset([2,3,4,5,5])
print(a)


a = "   Bhavani Mohan   "
print(a.strip())
print(a.upper())

a= {"nani","sai","mom"}
print(a.popitem("nani"))
# #TUPLE

# a=("nani","sai","balaram")
# print(a.count("balaram"))

# a = ("nani","sai")
# print(a.index("sai"))

# #sets

# a={"nani","sai","balaram",2,3,4,5,6,8}
# b =a.add("hari")
# print(a)

# a={"nani","sai","balaram",2,3,4,5,6,8}
# b =a.add((3,4,5))
# print(a)

# # a={"nani","sai","balaram",2,3,4,5,6,8}
# # b =a.add([3,4,6]) 
# # print(a)

# a={"nani","sai","balaram",2,3,4,5,6,8}
# a.update({"shannu"})
# print(a)

# a={"nani","sai","balaram",2,3,4,5,6,8}
# a.remove("sai")
# print(a)

# a={"nani","sai","balaram",2,3,4,5,6,8}
# a.discard("babu")
# print(a)

# a={"nani","sai","balaram",2,3,4,5,6,8}
# a.pop()
# print(a)

# a={"nani","sai","balaram",2,3,4,5,6,8}
# a.clear()
# print(a)

# a={"nani","sai","balaram",2,3,4,5,6,8}
# b=a.copy(b)
# print(a)

# a={2,3,4,5,6,8}
# b = {2,3,4,55,8,9,0,5}
# a.union(b)
# print(a)

# a={2,3,4,5,6,8}
# b = {2,3,4,55,8,9,0,5}
# a.intersection(b)
# print(a|b)

# a={2,3,4,5,6,8}
# b = {2,3,4,55,8,9,0,5}
# a.difference(b)
# print(a-b)

# a={2,3,4,5,6,8}
# b = {2,3,4,55,8,9,0,5}
# a.symmetric_difference(b)
# print(a^b)

# a={2,3,4,5,6,8}
# b = {2,3,4,55,8,9,0,5}
# print(a.isdisjoint(b))

# a={2,3,4,5,6,8}
# b = {2,3,4,55,8,9,0,5}
# print(a.issubset(b))

# a={2,3,4,5,6,8}
# b = {2,3,4,55,8,9,0,5}
# print(a.issuperset(b))


#DICT

a={"nani":88,"sai":99,"hari":90,"anu":98,"balaram":99}
# a.pop("sai")
# print(a)

# a.popitem()
# print(a)

# print(a.keys())
# print(a.values())
# print(a.items())

# del a["nani"]
# print(a)

# print(a.clear())

# b=a.copy()
# print(b)


print(a.get("sai"))

print(a.fromkeys("anu",3))
a.update({"anu":5})
print(a)

a.setdefault("phone no",23)
print(a)

