from database import my_connection
from product import get_product_details, update_product, delete_product

connection = my_connection()
print("Connection established successfully!")
while True:
    print("1. Get product details")
    print("2. Update product")
    print("3. Delete product")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        get_product_details()
    if choice == "2":
        product_id = int(input("Enter the id to update : ")) 
        name = input("Enter the name : ") 
        category = input("Enter the category to update : ") 
        price = float(input("Enter the price : "))
        quantity = int(input("Enter the quantity : "))
        supplier = input("Enter the supplier : ")
        update_product(product_id, name, category, price, quantity, supplier)

    if choice == "3":
        product_id = int(input("Enter the id to delete : "))
        delete_product(product_id)
    if choice == "4":
        break