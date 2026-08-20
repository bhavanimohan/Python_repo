print("-------------------------------Part A — map() with lambda-------------------------------------")
nums = [1, 2, 3, 4, 5]
a = list(map(lambda x : x **2,nums))
print(a)

nums = [1, 2, 3, 4, 5]
a = list(map(lambda x : x **3,nums))
print(a)

nums = [1, 2, 3, 4, 5]
a = list(map(lambda x : x+10,nums))
print(a)

nums = [1, 2, 3, 4, 5]
a = list(map(lambda x : x *5,nums))
print(a)

names = ["amit", "riya", "kabir"]
a = list(map(lambda x : x.upper(),names))
print(a)

names = ["AMIT", "RIYA", "KABIR"]
a = list(map(lambda x : x.lower(),names))
print(a)

words = ["hello", "world", "python"]
a = list(map(lambda x : len(x),words))
print(a)

nums = [1, 2, 3]
a = list(map(lambda x : str(x),nums))
print(a)

celsius = [0, 20, 37, 100]
a = list(map(lambda x : (x*(9/5))+32,celsius))
print(a)

prices = [100, 250, 500]
a = list(map(lambda x :x - x * 10/100,prices))
print(a)

nums = [3, 4, 7, 10]
a = list(map(lambda x : "Even" if x % 2 == 0 else "Odd",nums))
print(a)

marks = [55, 60, 45]
a = list(map(lambda x : x +5,marks))
print(a)

names = ["Dev", "Meera"]
a = list(map(lambda x  : "Hello "+ x,names))
print(a)

nums = [10, 14, 20]
a = list(map(lambda x : x % 3 , nums))
print(a)

ages = [20, 25, 30]
a = list(map(lambda x : x + 1,ages))
print(a)

salaries = [30000, 50000]
a = list(map(lambda x : x + x * 15/100,salaries))
print(a)

nums = [-3, 4, -7, 8]
a = list(map(lambda x : abs(x),nums))
print(a)

words = ["python", "java"]
a = list(map(lambda x : x.title(),words ))
print(a)


listA = [1, 2, 3] 
listB = [10, 20, 30]
a = list(map(lambda x ,y: x + y ,listA,listB))
print(a)

marks = [35, 40, 55, 20]
a = list(map(lambda x : "Pass" if x >= 40 else "Fail",marks))
print(a)


print("----------------------Part B — map() with tuples and dictionaries---------------------------------")


students = [("Amit", 21), ("Riya", 19), ("Kabir", 23), ("Sara", 20)]


orders = [("Pen", 5, 10), ("Book", 2, 250), ("Bag", 1, 800)]
a = list(map(lambda x  : (x[0],x[1]*x[2] ),orders ))
print(a)


coordinates = [(2, 3), (-1, 5), (0, 0), (4, -7)]
a = list(map(lambda x : str(x) , coordinates))
print(a)


names = ["Dev", "Meera", "Ishaan"] 
scores = [88, 92, 76]
a = list(map(lambda x ,y: {'name ': x, 'Score' : y},names,scores))
print(a)

employees = [    
             {"name": "Neha", "dept": "HR", "salary": 45000},    
             {"name": "Arjun", "dept": "IT", "salary": 62000},    
             {"name": "Priya", "dept": "IT", "salary": 58000}, 
             ]
a = list(map(lambda x : x["name"] , employees))
print(a)


students = [("Amit", 21), ("Riya", 19), ("Kabir", 23), ("Sara", 20)]
a = list(map(lambda x : x[0] , students))
print(a)


products = [    
            {"item": "Laptop", "price": 50000},    
            {"item": "Mouse", "price": 500},    
            {"item": "Keyboard", "price": 1200},
            
            
]

def new(x):
    x["gst"] = (x["price"] * 0.18)
    return x
    

a = list(map( new ,products))
print(a)