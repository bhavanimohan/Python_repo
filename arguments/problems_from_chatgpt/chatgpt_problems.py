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

# def calculate_gross_salary(basic,hra,da,allowances):
#     gross_salary = basic + hra+ da+ allowances
#     return gross_salary

# def calculate_bonus(years_of_service, gross_salary):
#     bonus = 0
#     if(years_of_service>=10):
#         bonus = gross_salary * 15/100
#     elif years_of_service >=5 and years_of_service<=9:
#         bonus = gross_salary * 10/100
#     elif years_of_service>=1 and years_of_service <= 4:
#         bonus = gross_salary * 5/100
#     else:
#         bonus = 0
#     return bonus 
    
# def calculate_tax(gross_salary):
#     tax = 0
#     if gross_salary <=25000:
#         tax = 0
#     elif gross_salary >= 25001 and gross_salary <=50000:
#         tax = (gross_salary *5/100)
#     elif gross_salary >=50001 and gross_salary<=100000:
#         tax = (gross_salary * 10/100)
#     else:
#         tax = (gross_salary * 20/100)
#     return tax
        
        
        

    
# def calculate_net_salary(gross_salary, bonus, tax):
#     leave = calculate_leave_deduction(gross_salary, leave_days)
    
#     net_salary = gross_salary + bonus - tax -leave
#     return net_salary
    
# def calculate_leave_deduction(gross_salary, leave_days):
#     leave_amount_deduction = 0
#     for char in range(1,leave_days):
#         if char<=2 :
#             leave_amount_deduction+= 0
#         else:
#             leave_amount_deduction += gross_salary/30
#     return leave_amount_deduction
        

        
    
# def display_info(name,emp_id,gross_salary,years_of_service,hra,da,leave_days):
#     print("-------------------- PAYSLIP----------------")
#     print(f"Name : {name}")
#     print(f"Emp_ID : {emp_id}")
#     gross_salary = calculate_gross_salary(basic,hra,da,allowances)
#     print(f"Gross Salary : {gross_salary}")
#     bonus = calculate_bonus(years_of_service, gross_salary)
    
#     print(f"Bonus : {bonus}")
#     tax = calculate_tax(gross_salary)
#     print(f"Tax : {tax}")
#     total_net = calculate_net_salary(gross_salary, bonus,tax)
#     print(f"Net Salary: {total_net}")
#     leave_day = calculate_leave_deduction(gross_salary, leave_days)
#     print(f"Leave amount deducted : {leave_day}")
    
    
# name = input("Enter employee name : ")
# emp_id = input("Enter the employee ID : ")
# basic= int(input("Enter the amount : "))
# hra = int(input("Enter the HRA : "))
# da = int(input("Enter the DA : "))
# allowances = int(input("Enter Allowacnes - (Press enter to skip) : "))
# years_of_service = int(input("Enter years of service : ")) 
# leave_days = int(input("Enter the no of leaves needed : "))
    

# display_info(name,emp_id,basic,years_of_service,hra,da,leave_days)





def calculate_ticket_cost(base_price, num_tickets,is_weekend=False):
    price = 0
    if is_weekend == True or is_weekend == "1" or is_weekend == "y":
        for char in range(num_tickets):
            price += base_price+50
    else:
        price = base_price*num_tickets
    return price

def apply_group_discount(amount, num_tickets):
    res = 0
    if (num_tickets == 1 or num_tickets == 2):
        res = amount
    elif (num_tickets>=3 and num_tickets<=5):
        res = amount - amount*10/100
    elif (num_tickets>=6):
        res = amount - amount*15/100
    return res
        
    
def apply_membership_discount(amount,is_member=False):
    result = 0
    if(is_member == True or is_member == "1" or is_member == "y"):
        result = amount - amount*5/100
    else:
        result = amount
    return result


def calculate_food_combo_cost(num_combos,combo_price=250):
    total = 0
    if(num_combos == 0):
        total = 0
    else:
        total = num_combos * combo_price    
    return total
    
def calculate_gst(amount,gst_rate=18):
    gst_amount = 0
    gst_amount = amount * gst_rate / 100
    return gst_amount
    
def generate_final_bill(ticket_amount, combo_amount,amount):
    
    Final_bill = ticket_amount + combo_amount + amount
    return Final_bill

def display_invoice(name, num_tickets, ticket_amount, combo_prices):
    print(f"----- MOVIE TICKET INVOICE -----")
    print(f"Customer: {name}")
    print(f"Tickets: {num_tickets}")

    amount = calculate_ticket_cost(ticket_amount, num_tickets, is_weekend)
    amount = apply_group_discount(amount, num_tickets)
    amount = apply_membership_discount(amount, is_member)

    print(f"Ticket Amount (after discounts): {amount}")

    combo_amount = calculate_food_combo_cost(combo_prices)
    print(f"Food Combo Amount: {combo_amount}")

    gst_amount = calculate_gst(amount + combo_amount)
    print(f"GST (18%): {gst_amount}")

    total = generate_final_bill(amount, combo_amount, gst_amount)
    print(f"Total Payable: {total}")


name = input("Enter customer name : ")
ticket_amount = int(input("Enter base ticket price : "))
num_tickets = int(input("Enter number of tickets : "))
is_weekend = input("Is it a weekend booking? (y/n) : ")
is_member = input("Are you a member? (y/n): ")
combo_prices = int(input("Enter number of food combos : "))

display_invoice(name, num_tickets, ticket_amount, combo_prices)