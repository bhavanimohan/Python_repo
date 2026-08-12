# def details(name,age,course):
#     print(f"Name : {name}")
#     print(f"Age : {age}")
#     print(f"Course : {course}")
# details("suresh", 22,"Python")
#positional arguments were used according to the use-case.

# def details(name,age,course):
#     print(f"Name : {name}")
#     print(f"Age : {age}")
#     print(f"Course : {course}")
# details(name = "nani",age = 23,course="Python")
#these are called as key-value pair arguments 



# def details(name = "amul"):
#     print(f"Name : {name}")
#     # print(f"Age : {age}")
#     # print(f"Course : {course}")
# details()
#these are the default values that are automatically takes name as amul if don't mention any name in the function call.

# def my_average(*a):
#     print(f"values : {a}")
#     sums = sum(a)
#     lens = len(a)
#     print(sums/lens)


  
# my_average(1,2)


def my_average(*a):
    print(f"values : {a}")
    count = 0
    countss =0
    for char in a:
        count+=char
        countss+=1
    print(count/countss)
        


  
my_average(1,2)