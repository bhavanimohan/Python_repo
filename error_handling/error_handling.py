menu_item = {
    "briyani" :170,
    "mutton briyani" :210,
    "coke" : 50,
    "meals":120
}

try:
    name = input("Enter dish name  ")
    quantity  = int(input("Enter the quantity : "))
    amount = int(input("Enter the amount : "))
    item = menu_item[name]
    total = item * quantity
    discount = total / quantity
    actual_amount = total - discount
    return_amount = amount - total
    
    
    

    
except KeyError:
    print("Enter a valid item from the menu.")
except ZeroDivisionError:
    print("Quantity shouldn't be Zero so minimun you need to add one.")
    
except Exception:
    print("something happened go back to your code and check it.")
    
        
    
    
    
    
else:
    print(f"Item you selected from the memu : {name}")
    print(f"The quantity you selected : {quantity}")
    print(f"Amount you given to waiter : {amount}")
    print(f"Total amount you need to pay : {total}")
    print(f"The discount you got on this item : {discount}")
    print(f"Return amount you got : {return_amount}")
    print(f" Payment successful : {actual_amount}")
    print("Happpy shooppingggggg................")
    
    
finally:
    print("Visit Again .... ")