# a =[[3,5,3,2,5,3],[7,5,6,3,2]]
# print(a[0][0])
# print(a[1][1])

a=["hello","world","python"]

a.extend(["hari"])
print(a)

# a.index("hello") #this method returns the index of the first occurrence of the specified value
print(a.index("hello"))

a.append("programming") #this method adds a single element to the end of the list01
print(a)

a.extend(["java","c++"]) #this method adds the specified list elements (or any iterable) to the end of the current list
print(a)

a.insert(1,"javascript") #this method inserts the specified value at the specified position
print(a)

a.remove("python") #this method removes the first occurrence of the specified value
print(a)

a.pop(1) #this method removes the element at the specified position
print(a)

# a.clear() #this method removes all the elements from the list
print(a.clear())

b=a.copy() #this method returns a shallow copy of the list
print(b)


c=[3,5,2,1,4]
# a.reverse() #this method reverses the list
print(c.reverse())
print(c)

c=[3,5,2,1,4]
# a.sort() #this method sorts the list in ascending order
print(c.sort(reverse=True))
print(c)

# print(a.count(3))  
# print(a[4])

# b = "nani"
# print(b.swapcase())
