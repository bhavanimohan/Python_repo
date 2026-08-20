# def sums(a,b):
#     return a+b
# def sub(a,b):
#     return a -b
# def mult(a,b):
#     return a*b
# def div(a,b):
#     return a/b

# operator_function = {
#     "+": sums,
#     "-":sub,
#     "*":mult,
#     "/":div
    
# }



# num1 = int(input("Enter the number : "))
# num2 = int(input("Enter the number : "))
# op_function = input("Enter the opeartor function : ")
# def calculator(num1,num2,operator_functions):
#     print(operator_functions(num1,num2))
    
# calculator(num1,num2,operator_function[op_function])
    
    
# calculator(num1,num2,lambda a,b :a+b)
# calculator(num1,num2,lambda a,b :a-b)
# calculator(num1,num2,lambda a,b :a*b)
# calculator(num1,num2,lambda a,b :a/b)

# def sq(x):
#     return x ** 2

# number=[1,2,3,4,5,6]
# res = map(sq,number)
# print(list(res))
numbers = [1,2,3,4,5]
a = list(map(lambda x : x+5 ,numbers))
print(a)

names = ["anu","nani","sunny"]
a = list(map(lambda x : x.upper(),names))
print(a)

def convt_upper(names):
    return names.upper()

names = ["anu","nani"]
res = list(map(convt_upper,names))
print(res)