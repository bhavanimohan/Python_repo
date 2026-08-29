#============================LEVEL - ONE ===================================
# Create a function greet(name, age) that prints:
# Hello Bhavani, you are 23 years old.
# Call the function using positional arguments.

# def greet(name,age):
#     print(f"hello this is {name} and I'm {age} year's old")
# greet("nani",22)

#Add Two Numbers
# def addiion(num1,num2):
#     print(f" {num1} + {num2} = {num1+num2}")
# addiion(10,20)

#Student Details
# def names(name,age,course):
#     print(f"Name : {name}")
#     print(f"Age : {age}")
#     print(f"Course : {course}")
# names("Bhavani Mohan", 22, "Software Engineering")

#Rectangle Area
# def rectangle(length,width):
#     print(f"Area of Rectanlge : {length * width}")
# rectangle(50,5)

#Simple Interest
# def interest(p,r,t):
#     print((p*r*t)/100)
# interest(100,200,300)

#==================================LEVEL - TWO ===========================================

#Employee Details
# def empployee(name,age,salary):
#     print(f"Name : {name}")
#     print(f"Age : {age}")
#     print(f"Salary : {salary}")
# empployee("Nani" , 22 , 60000)

#Calculate Bill
# def price_amount(quantity, amount):
#     print(f"Select Quantity : {quantity}  | Your Bill is Around : {amount * quantity}")
# price_amount(2,799)

#Student Marks
# def marks(name, maths, science, english):
#     print(f"""Name : {name}
#              Maths : {maths}
#            Science : {science}
#            English : {english}""")
# marks("Nani",90,92,99)

#Login Details
# def user_login(username,password):
#     print(f"User_Name : {username}")
#     print(f"Password : {password}")
# user_login("Bhavani@2003","Nani@2003")


#=============================  Level 3 — Default Arguments   ==============================
# def greet(name, message="Good Morning"):
#     print(message,name)
# greet("Bhavani")

#Country
# def person(name, country="India"):
#     print(name,country)
# person("I'm from")

#Shopping bill
# def bill(price, quantity=1):
#     print(f"Quanity : {quantity}")
#     print(f"Price : {quantity * price}")
# bill(320,3)

# Power
# def power(number, exponent):
#     print(f"Number : {number}")
#     print(f"Exponent : {exponent}")
#     print(f"Final Result : {number ** exponent}")
# power(5,2)

# Student Information
# def students_info(name, course = "Software Engineering" ,year = 2026):
    
#     print(f"Name : {name} == ",course, year)
# students_info("Bhavani")

# students_info("Bhavani", "VIT - AP")

#================================  Level 4 — Variable-Length Arguments *args =======================
# def add(*numbers):
#     total = 0
#     for char in numbers:
#         total+=char
#     return total
# print(add(1,2,3,4,5,6,7,8))
# print(add(10, 20, 30, 40))

#Find count of numbers ⭐
# def count_num(*lst):
#     count =0
#     for char in lst:
#         count+=1
#     return count
# print(count_num(2,3,4,5,6,7,8,9,5,4,3,3,2,2))

# Find Maximum ⭐
# def max_count(*num):
#     first = -1
#     for char in num:
#         if char>first:
#             first = char
#     return first
# print(max_count(2,3,4,99,7,5,4,3,6,77))
    
# Calculate Average
# def avg(*num):
#     total = count = 0
#     for char in num:
#         total+=char
#         count+=1
#     print(total/count)
# avg(1,2,3,4,5,6)

#Even Numbers ⭐
# def even_num(*num):
#     count = []
#     for char in num:
#         if char % 2 == 0:
#             count.append(char)
#     return count

# print(even_num(1,2,3,4,5,6,7,8))


#=========================== LEVEL _ FIVE Mixed Arguments    ==============================
# def sums(*nums):
#     total = 0
#     for char in nums:
#         total+=char
#     return total

# def avg(*nums):
#     count = 0
#     for char in nums:
#         count+=1
#     return count

# def students(name,*nums):
#     b = sums(*nums)
#     c = avg(*nums)
#     avg_is = b/c
#     print(f"Name : {name}")
#     print(f"Total : {b}")
#     print(f"Average : {avg_is}")

# students("Bhavani Mohan" ,80, 90, 85, 75)
            
#Shopping Cart ⭐⭐
# def sums(*nums):
#     total = 0
#     for char in nums:
#         total+=char
#     return total
    
# def shopping_cart(name,*nums):
    
#     print(f"Name : {name}")
#     b = sums(*nums)
#     print(f"Total : {b}")
# shopping_cart("Bhavani", 100, 250, 50, 300)
    
#Employee Salary ⭐⭐
# def sums(*nums):
#     total = 0
#     for char in nums:
#         total+=char
#     return total
# def employee_salary(name,*nums):
#     print(f"Name : {name}")
#     b = sums(*nums)
#     print(f"Final salary : {b}")
# employee_salary("Bhavani", 30000, 2000, 1500, 1000)

#=========================Level 6 — Challenge Problems==============================

# def calculator(operation, *numbers):
#     if operation == "+":
#         count = 0
#         for char in numbers:
#             count+=char
#         return count
#     elif operation == "-":
#         count = 0
#         for char in numbers:
#             count=char-count
#         return count
#     elif operation == "*":
#         count = 1
#         for char in numbers:
#             count=char*count
#         return count
#     else:
#         count = 1        
#         for char in numbers:
#             count= char/count
#         return count
# print(calculator("/",2,3,4))

            
#Personal Introduction ⭐⭐⭐
# def introduce(name, age, city="Hyderabad", *skills):
#     print(f"Name : {name}")
#     print(f"Age : {age}")
#     print(f"City : {city}")
#     print(f"Skills : {skills}")
    
# introduce("Nani", 22, "Vijayawada", "HTML","CSS")


#Marks Analyzer ⭐⭐⭐

# def my_total(*marks):
#     total = 0
#     for char in marks:
#         total+=char
#     return total

# def my_count(*marks):
#     count = 0
#     for char in marks:
#         count+=1
#     return count

# def my_average(*marks):
#     b = my_total(*marks)
#     c = my_count(*marks)
#     res = (b/c)
#     return res

# def highest_mark(*marks):
#     first_max = 0
#     for char in marks:
#         if char>first_max:
#             first_max= char
#     return first_max


# def lowest_max(*marks):
#     lowest_maxs = marks[0]
#     for char in marks:
#         if lowest_maxs>char:
#             lowest_maxs = char
#     return lowest_maxs
    

# def grade_marks(*marks):
    
#     avg_marks= my_average(*marks)
    
#     if(avg_marks >= 91):
#         return "Excellent"
#     elif (avg_marks>81 and avg_marks<90):
#         return "A"
#     elif (avg_marks>71 and avg_marks<80):
#         return "B"
#     elif (avg_marks>61 and avg_marks <70):
#         return "C"
#     else:
#         return "D"


    

# def marks_analyzer(student_name, *marks):
#     print(f"Name : {student_name}")
    
#     tol= my_total(*marks)
#     print(f"Total Marks  : {tol}")
    
#     avg = my_average(*marks)
#     print(f"Average : {avg}")
    
#     high = highest_mark(*marks)
#     print(f"Highest Marks : {high}")
    
#     low = lowest_max(*marks)
#     print(f"Lowest Marks : {low}")
    
#     number = my_count(*marks)
#     print(f"No of Subjects : {number}")
    
#     Grades = grade_marks(*marks)
#     print(f"Grade : {Grades}")
    
# marks_analyzer("Bhavani", 85, 90, 78, 92, 88)

def remove_duplicates(numbers):
    empty_list = []

    for i in numbers:
        if i not in empty_list:
            empty_list.append(i)

    return empty_list

print(remove_duplicates([2, 3, 4, 2, 3, 4, 5, 6, 7]))

def remove_duplicates(numbers):
    result = []

    for num in numbers:
        if num not in result:
            result.append(num)

    return result

print(remove_duplicates([2, 3, 4, 2, 3, 4, 5, 6, 7]))