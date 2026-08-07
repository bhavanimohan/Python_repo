# a = input("Tpye ON | OFF : ")
# Milk_powder=1000 
# Coffee_powder=500 
# Water=5000



# while True:

#     if a == "ON":
#         print("Welcome to Nani's Coffee Shop....!")
     
    
#         menu_list = input("Do you need menu card? Type Yes to proceed / No to exit: ")
#         if(menu_list == "Yes" or menu_list == "yes"):
#             print("Here is the memu card : ")
#             print("1) Latte ")
#             print("2) Espresso")
#             print("3) Milk coffee")
#             print("4) Hot Water")
#             user_input= input("Select which one do you prefer : ")
#         else:
#             user_input= input("Select which one do you prefer : ")
        
    
    
    
#         if(user_input == "1"):
#             cost = 40
#             quantity= int(input("May i know the Quantity : "))
#             if(quantity >10):
#                 print("We are not serving Latte Coffee RIght Now")
#                 break
            
            
#             print(f"You had selected Latte and the quantity is {quantity}")
#             print(f"Latte * {quantity} costs around : " + str(cost * quantity))
#             cash_from_user = int(input("Here is the amount : "))
#             cash_returned_to_customer = (cash_from_user - (cost * quantity))
#             print(f"here is the change amount : {cash_returned_to_customer}")
#             print("Enjoy your coffee...!!!") 
#             Milk_powder-=100 *quantity
#             Coffee_powder-=15*quantity
#             Water-=200*quantity
#             print("----------------------------------------")
#             print(f"Remaining Quantity of Milk_powder : {Milk_powder}")
#             print(f"Remaining Quantity of Coffee_powder : {Coffee_powder}")
#             print(f"Remainig Quantity of Water : {Water}")
#             print("----------------------------------------")
        
#         if(user_input == "2"):
#                 cost = 30
#                 quantity= int(input("May i know the Quantity : "))
#                 if(quantity >27):
#                     print("We are not serving Espresso Coffee Right Now")
#                     break
                
#                 print(f"You had selected Espresso and the quantity is {quantity}")
#                 print(f"Espresso * {quantity} costs around : " + str(cost * quantity))
#                 cash_from_user = int(input("Here is the amount : "))
#                 cash_returned_to_customer = (cash_from_user - (cost * quantity))
#                 print(f"here is the change amount : {cash_returned_to_customer}")
#                 print("Enjoy your coffee...!!!") 
#                 Milk_powder-=0 *quantity
#                 Coffee_powder-=18*quantity
#                 Water-=60*quantity
#                 print("----------------------------------------")
#                 print(f"Remaining Quantity of Milk_powder : {Milk_powder}")
#                 print(f"Remaining Quantity of Coffee_powder : {Coffee_powder}")
#                 print(f"Remainig Quantity of Water : {Water}")
#                 print("----------------------------------------")
              
#         if(user_input == "3"):
#                 cost = 25
#                 quantity= int(input("May i know the Quantity : "))
#                 if(quantity >20):
#                     print("We are not serving Milk Coffee Right Now")
#                     break
                    
#                 print(f"You had selected Milk Coffee and the quantity is {quantity}")
#                 print(f"Milk Coffee * {quantity} costs around : " + str(cost * quantity))
#                 cash_from_user = int(input("Here is the amount : "))
#                 cash_returned_to_customer = (cash_from_user - (cost * quantity))
#                 print(f"here is the change amount : {cash_returned_to_customer}")
#                 print("Enjoy your coffee...!!!")
#                 Milk_powder-=50 *quantity
#                 Coffee_powder-=10*quantity
#                 Water-=150*quantity
#                 print("----------------------------------------")
#                 print(f"Remaining Quantity of Milk_powder : {Milk_powder}")
#                 print(f"Remaining Quantity of Coffee_powder : {Coffee_powder}")
#                 print(f"Remainig Quantity of Water : {Water}") 
#                 print("----------------------------------------")
            
#         if(user_input == "4"):
#                 cost = 5
#                 quantity= int(input("May i know the Quantity : "))
#                 if(quantity >25):
#                     print("We are not serving Hot Water Right Now")
#                     break
                    
#                 print(f"You had selected Hot Water and the quantity is {quantity}")
#                 print(f"Hot Water * {quantity} costs around : " + str(cost * quantity))
#                 cash_from_user = int(input("Here is the amount : "))
#                 cash_returned_to_customer = (cash_from_user - (cost * quantity))
#                 print(f"the change amount : {cash_returned_to_customer}")
#                 print("Enjoy your coffee...!!!") 
#                 Milk_powder-=0 *quantity
#                 Coffee_powder-=0*quantity
#                 Water-=200*quantity
#                 print("----------------------------------------")
#                 print(f"Remaining Quantity of Milk_powder : {Milk_powder}")
#                 print(f"Remaining Quantity of Coffee_powder : {Coffee_powder}")
#                 print(f"Remainig Quantity of Water : {Water}")
#                 print("----------------------------------------")  
    
                 
                   
    
#     else:
#         print("coffee shop is closed.")
#         pass