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
print(a.pop({"nani"}))