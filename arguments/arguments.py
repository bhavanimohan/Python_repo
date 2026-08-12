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


# def my_average(*a):
#     print(f"values : {a}")
#     count = countss = 0
#     for char in a:
#         count+=char
#         countss+=1
#     print(count/countss)
# my_average(1,2) 

# def my_sum(*a):
#     count = 0
#     for char in a:
#         count+=char
#     return count

# def my_len(*a):
#     countss = 0
#     for char in a:
#         countss+=1
#     return countss

# def my_average(*a):
#     b = my_sum(*a)
#     c = my_len(*a)
#     print(b/c)
    
# my_average(1,2)

# def my_sort(lst):
#     for i in lst:
#         for j in range((len(lst))-1):
#             if lst[j]<lst[j+1] :
#                 lst[j],lst[j+1] = lst[j+1],lst[j]
#     return lst
# print(my_sort([2,3,5,7,23,2,3,5,6,8,6,77,88,55,67]))

    
# def my_contains(lst,b):
    
#     if b in lst:
#         print("True")
#     else:
#         print("False")
    
# my_contains([1,2,3,4],9)

# def my_map(a, lst):
#     b = []
#     for char in lst:
#         char = char*a
#         b.append(char)
#     return b
# print(my_map(2,[3,4,5]))
        
        
# def my_filter(lst):
#     empty_lst =[]
#     for char in lst:
#         if char%2 == 0:
#             empty_lst.append(char)
            
#     return empty_lst
# print(my_filter([2,3,4,5,6,7,8,9,10]))
        
# def my_zip(lst1,lst2):
#     empty_lst = []
#     for i in range(len(lst1)):
#         empty_lst.append((lst1[i],lst2[i]))
#     return empty_lst
# print(my_zip([1,2,3],["a","b","c"]))

# def my_count(lst,num):
#     count =0
#     for char in lst:
#         if char == num:
#             count+=1
#     return count
# print(my_count([1,2,3,4,3,2,3,2],3))
        
        
# def my_upper(str):
#     res = ""
#     for char in str:
#         if "A"<char<"Z":
#             res+=chr(ord(char)+32)
#         else:
#             res+=char
#     return res
# print(my_upper("HELLO WORLD"))

        
# def my_upper(str):
#     res = ""
#     for char in str:
#         if "a"<char<"z":
#             res+=chr(ord(char)-32)
#         else:
#             res+=char
#     return res
# print(my_upper("hello world"))

def my_index(lst,num):
    count = 0
    for char in lst:
        if char == num:
            count+=1
            break
            
    else:
        return "-1"
            
    return count
print(my_index([2,3,4,5,6,1,2],88))
        