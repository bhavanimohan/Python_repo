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
    
    

    
# print("----------------------------------------Task - 1----------------------------------------")    
# name = input("Enter employee name : ")
# emp_id = input("Enter the employee ID : ")
# basic= int(input("Enter the amount : "))
# hra = int(input("Enter the HRA : "))
# da = int(input("Enter the DA : "))
# allowances = int(input("Enter Allowacnes - (Press enter to skip) : "))
# years_of_service = int(input("Enter years of service : ")) 
# leave_days = int(input("Enter the no of leaves needed : "))
    

# display_info(name,emp_id,basic,years_of_service,hra,da,leave_days)





# def calculate_ticket_cost(base_price, num_tickets,is_weekend=False):
#     price = 0
#     if is_weekend == True or is_weekend == "1" or is_weekend == "y":
#         for char in range(num_tickets):
#             price += base_price+50
#     else:
#         price = base_price*num_tickets
#     return price

# def apply_group_discount(amount, num_tickets):
#     res = 0
#     if (num_tickets == 1 or num_tickets == 2):
#         res = amount
#     elif (num_tickets>=3 and num_tickets<=5):
#         res = amount - amount*10/100
#     elif (num_tickets>=6):
#         res = amount - amount*15/100
#     return res
        
    
# def apply_membership_discount(amount,is_member=False):
#     result = 0
#     if(is_member == True or is_member == "1" or is_member == "y"):
#         result = amount - amount*5/100
#     else:
#         result = amount
#     return result


# def calculate_food_combo_cost(num_combos,combo_price=250):
#     total = 0
#     if(num_combos == 0):
#         total = 0
#     else:
#         total = num_combos * combo_price    
#     return total
    
# def calculate_gst(amount,gst_rate=18):
#     gst_amount = 0
#     gst_amount = amount * gst_rate / 100
#     return gst_amount
    
# def generate_final_bill(ticket_amount, combo_amount,amount):
    
#     Final_bill = ticket_amount + combo_amount + amount
#     return Final_bill

# def display_invoice(name, num_tickets, ticket_amount, combo_prices):
#     print(f"----- MOVIE TICKET INVOICE -----")
#     print(f"Customer: {name}")
#     print(f"Tickets: {num_tickets}")

#     amount = calculate_ticket_cost(ticket_amount, num_tickets, is_weekend)
#     amount = apply_group_discount(amount, num_tickets)
#     amount = apply_membership_discount(amount, is_member)

#     print(f"Ticket Amount (after discounts): {amount}")

#     combo_amount = calculate_food_combo_cost(combo_prices)
#     print(f"Food Combo Amount: {combo_amount}")

#     gst_amount = calculate_gst(amount + combo_amount)
#     print(f"GST (18%): {gst_amount}")

#     total = generate_final_bill(amount, combo_amount, gst_amount)
#     print(f"Total Payable: {total}")

# print("-------------------------TASK - 2 -------------------------------------------")
# name = input("Enter customer name : ")
# ticket_amount = int(input("Enter base ticket price : "))
# num_tickets = int(input("Enter number of tickets : "))
# is_weekend = input("Is it a weekend booking? (y/n) : ")
# is_member = input("Are you a member? (y/n): ")
# combo_prices = int(input("Enter number of food combos : "))

# display_invoice(name, num_tickets, ticket_amount, combo_prices)