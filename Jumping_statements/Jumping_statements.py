a = int(input("Enter the number : "))
for char in range(1,a+1):
    print(char)
    if char == 4:
        break
    
a = int(input("Enter the number : "))
for char in range(1,a+1):
    
    if char == 4:
        print(char)
        break

a = int(input("Enter the number : "))
for char in range(1,a+1):
    print(char)
    if char == 4:
        continue
    print(f"faaahh {char}")
       
       
       
a = int(input("Enter the number : "))
for char in range(1,a+1):
    print(char)
    if char == 4:
        pass

for char in range(1,5+1):
    print(char)
    
else:
    print("Hello guru")
lst = [1,2,5,6,79,4,3,7]
a = int(input("Enter the number : "))
for char in lst:
    if(char == a):
        print("Numberr founddddd")
        break
else:
    print("num is not found")
    
a = ["Frutis", "Banana","Grapes"]
count = 0
for char in a:
    print(f"({count}, {char})")
    count+=1
    

a = ["Frutis", "Banana","Grapes"]
for char in range(len(a)):
    print(f"({char}, {a[char]})")
    

a = ["Frutis", "Banana","Grapes"]
for char in a:
    print(f"({a.index(char)}, {char})")

a = ["Frutis", "Banana","Grapes","Apple","Carrot"]
for char in enumerate(a):
    print(char)
n_list = [[1,2],[3,4],10,[5,6]]
num = []
for char in n_list:
    if isinstance(char,int):
        num.append(char)
        continue
    for charss in char:
        num+=[charss]
        
print(num)
   
n_list = [[1,2],[3,4],10,[5,6]]
num = []
for char in n_list:
    if isinstance(char,int):
        num+=[char]
        continue
    for charss in char:
        num+=[charss]
        
print(num)
    
    
n_list = [[1,2],[3,4],10,[5,6],27]
num = []
for char in n_list:
    if type(num) ==:
        num+=[char]
        continue
    for charss in char:
        num+=[charss]
        
print(num)