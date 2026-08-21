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

Input = [('Pen', 20), ('Watch', 1500), ('Bag', 450)]
print(list(filter(lambda x : (x[1]<500),Input)))

Input = [(3, 3), (2, 5), (7, 7), (1, 2)]
print(list(filter(lambda x : (x[0] == x[1]),Input )))

Input = [('Apple', 1), ('Mango', 2), ('Orange', 3)]
print(list(filter(lambda x : (x[0][0] in "aeiouAEIOU") , Input)))

Input = [('Mon', 32), ('Tue', 38), ('Wed', 40)]
print(list(filter(lambda x : (x[1] > 35),Input)))



