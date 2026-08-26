# menu_item = {
#     "briyani" :170,
#     "mutton briyani" :210,
#     "coke" : 50,
#     "meals":120
# }

# try:
#     name = input("Enter dish name  : ")
#     quantity  = int(input("Enter the quantity : "))
#     amount = int(input("Enter the amount : "))
#     item = menu_item[name]
#     total = item * quantity
#     discount = total / quantity
#     actual_amount = total - discount
#     return_amount = amount - total
    
    
    

    
# except KeyError:
#     print("Enter a valid item from the menu.")
# except ZeroDivisionError:
#     print("Quantity shouldn't be Zero so minimun you need to add one.")
# except ValueError:
#     print("Enter the a valid number.")
# except NameError:
#     print("Enter the valid name or valid number.")    
# except Exception:
#     print("something happened go back to your code and check it.")

    
        
    
    
    
    
# else:
#     print(f"Item you selected from the memu : {name}")
#     print(f"The quantity you selected : {quantity}")
#     print(f"Amount you given to waiter : {amount}")
#     print(f"Total amount you need to pay : {total}")
#     print(f"The discount you got on this item : {discount}")
#     print(f"Return amount you got : {return_amount}")
#     print(f"-------------------Payment successful : {actual_amount}-----------")
#     print("---------------------------------Happpy shooppingggggg................")
    
    
# finally:
#     print("------------------------------------------Visit Again .... ")
   
   
    
# Write a program that asks the user to enter two numbers and divides the first number 
# by the second. Handle ZeroDivisionError

# try:
#     name = input("Enter the valid name : ")
#     amount = int(input("Enter a number :"))
#     quantity = int(input("Enter the quantity : "))
#     res = amount / quantity
#     print(res)
    
# except ZeroDivisionError:
#     print("You had entered invalid number so plz try again by running this code.")

# Write a program that asks the user to enter an integer. 
# If the user enters text instead of a number, handle ValueError

# try:
#     name = input("Enter the valid name : ")
#     amount = int(input("Enter a number :"))
#     quantity = int(input("Enter the quantity : "))
#     res = amount / quantity
#     print(res)
    
# except ValueError:
#     print("You had entered invalid number so plz try again by running this code.")


# Create a dictionary containing 5 food items and their prices. 
# Ask the user for an item and handle KeyError if the item doesn't exist

# menu = {
#     "briyani" :170,
#     "mutton briyani" :210,
#     "coke" : 50,
#     "meals":120,
#     "diet coke": 70
# }

# try:
#     name = input("Enter dish from menu : ")
#     item = menu[name]
#     print(item)
# except KeyError:
#     print("The selected item is not in the menu so try again...")


# Modify the above program so that a 10% 
# discount is given when the total bill is above ₹500.

# class InSufficientAmountError(Exception):
#     pass
# menu_item = {
#     "briyani" :170,
#     "mutton briyani" :210,
#     "coke" : 50,
#     "meals":120
# }
# try:
#     name = input("Enter dish name  : ")
#     quantity  = int(input("Enter the quantity : "))
#     amount = int(input("Enter the amount : "))
#     item = menu_item[name]
#     total = item * quantity
#     discount = 0
#     actual_amount = total 
#     return_amount = amount - total
#     if actual_amount > 500 :
#         actual_amount = actual_amount*10/100
#     actual_amount
#     if total>amount:
#         raise InSufficientAmountError("Insufficient amount")


# except KeyError:
#     print("Enter a valid item from the menu.")
# except ZeroDivisionError:
#     print("Quantity shouldn't be Zero so minimun you need to add one.")
# except ValueError:
#     print("Enter the a valid number.")
# except NameError:
#     print("Enter the valid name or valid number.")   
# except InSufficientAmountError as e:
#     print(e)
# except Exception:
#     print("something happened go back to your code and check it.")

# else:
#     print(f"Item you selected from the memu : {name}")
#     print(f"The quantity you selected : {quantity}")
#     print(f"Amount you given to waiter : {amount}")
#     print(f"Total amount you need to pay : {total}")
#     print(f"The discount you got on this item : {actual_amount}")
#     print(f"Return amount you got : {return_amount}")
#     print(f"-------------------Payment successful : {total-actual_amount}-----------")
#     print("---------------------------------Happpy shooppingggggg................")
    
    
# finally:
#     print("------------------------------------------Visit Again .... ")
   
   
# Write a program where the user enters their age.
# If age is less than 0 → raise a custom InvalidAgeError
# If age is between 0 and 17 → print "Not eligible"
# If age is 18 or above → print "Eligible"   
class InvalidAgeError(Exception):
    pass

try:
    name = input("Enter you name : ")
    age = int(input("Enter your age : "))
    if age <0:
        raise InvalidAgeError("Enter a valid number")
    if age>=0 and age<=17:
        print("Not Eligible")
    if (age>18):
        print("Eligible")
except InvalidAgeError as e:
    print(e)
else:
    pass
    


