# Input= [(2, 'a'), (3, 'b'), (4, 'c'), (5, 'd')]
# print(list(filter(lambda x : x[0] % 2 ==0 , Input)))

# Input= [('Ravi', 20), ('Anu', 15), ('Kiran', 19)]
# print(list(filter(lambda x : x[1]>18 , Input)))

# Input= [('Asha', 35), ('Ravi', 55), ('Sana', 40)]
# print(list(filter(lambda x : x[1]>=40 ,  Input)))

# Input = [(4, 5), (6, 7), (2, 3)]
# print(list(filter(lambda x:(x[0] + x[1] >10) , Input)))

# Input = [(2, 3), (-1, 4), (5, -2), (3, 6)]
# print(list(filter(lambda x : (x[0] > 0 and x[1]> 0),Input)))

# Input = [(1, 2), (-3, 4), (5, -6), (7, 8)]
# print(list(filter(lambda x : (x[0] > 0 and x[1]> 0),Input)))

# Input = [('Pen', 20), ('Watch', 1500), ('Bag', 450)]
# print(list(filter(lambda x : (x[1]<500),Input)))

# Input = [(3, 3), (2, 5), (7, 7), (1, 2)]
# print(list(filter(lambda x : (x[0] == x[1]),Input )))

# Input = [('Apple', 1), ('Mango', 2), ('Orange', 3)]
# print(list(filter(lambda x : (x[0][0] in "aeiouAEIOU") , Input)))

# Input = [('Mon', 32), ('Tue', 38), ('Wed', 40)]
# print(list(filter(lambda x : (x[1] > 35),Input)))

# Input = [('cat', 1), ('bird', 2), ('ant', 3), ('fish', 4)]
# print(list(filter(lambda x : len(x[0]) % 2 ==0 ,Input)))

# Input = [(1, 10), (2, 7), (3, 15), (4, 8)]
# print(list(filter(lambda x : (x[0] % 5 ==0) or (x[1] % 5 == 0) , Input )))

# Input = [(5, 2), (1, 4), (7, 7), (2, 9)]
# print(list(filter(lambda x : (x[0] < x[1]), Input)))

# Input = [('Banana', 1), ('Sky', 2), ('Grape', 3)]
# print(list(filter(lambda x : "a" in x[0],Input)))

# Input = [(2, 'a'), (4, 'b'), (7, 'c'), (9, 'd'), (11, 'e')]
# def is_prime(x):
#     count = True
#     for i in range(2,int(x[0])):
#         if x[0] % i == 0:
#             count = False
#     return count


# print(list(filter(lambda x : is_prime(x),Input)))

# Input= [{'name': 'Ravi', 'salary': 60000},
# {'name': 'Anu', 'salary': 40000}
# ]

# print(list(filter(lambda x : x["salary"]>50000 ,Input)))

# Input = [{'user': 'a', 'active': True}, {'user': 'b', 'active': False}]
# print(list(filter(lambda x : x["active"] == True , Input)))

# Input = [{'name': 'Asha', 'marks': 35}, {'name': 'Ravi', 'marks': 55}]
# print(list(filter(lambda x : x["marks"] >= 40 , Input)))

# Input = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(list(filter(lambda x : x[1] % 2 ,Input.items())))

Input = {'sun': 1, 'moon': 2, 'star': 3, 'sky': 4}
print(list(filter(lambda x :  x[0].startswith("s"),Input.items())))

Input = {'pen': 20, 'watch': 1500, 'bag': 450, 'pencil': 5}
print(list(filter(lambda x : x[1] > 100 ,Input.items())))

Input = [{'name': 'A', 'age': 20, 'city': 'Delhi'},
{'name': 'B', 'age': 17, 'city': 'Delhi'},
{'name': 'C', 'age': 22, 'city': 'Pune'}]
# Expected Output: [{'name': 'A', 'age': 20, 'city': 'Delhi'}]

print(list(filter(lambda x : x["age"] > 18 and x["city"] == "Delhi",Input )))

Input = {'a': 1, 'b': None, 'c': 3, 'd': None}
print(list(filter(lambda x : x[1] != None , Input.items())))

Input  = {'a': 'hello', 'b': 5, 'c': 'world', 'd': 3.5}
print(list(filter(lambda x : isinstance(x[1] , str), Input.items())))