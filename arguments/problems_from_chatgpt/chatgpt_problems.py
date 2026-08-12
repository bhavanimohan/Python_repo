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
def sums(*nums):
    total = 0
    for char in nums:
        total+=char
    return total
def employee_salary(name,*nums):
    print(f"Name : {name}")
    b = sums(*nums)
    print(f"Final salary : {b}")
employee_salary("Bhavani", 30000, 2000, 1500, 1000)