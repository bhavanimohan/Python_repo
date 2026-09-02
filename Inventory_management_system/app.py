from database import my_connection
from product import get_product_details, update_product, delete_product,search_product,get_same_products,get_same_model_products

connection = my_connection()
print("Connection established successfully!")
while True:
    print("1. Get product details")
    print("2. Update product")
    print("3. Delete product")
    print("4. Search product")
    print("5. Get same products")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        get_product_details()
    if choice == "2":
        update_product()
    if choice == "3":
        delete_product()
    if choice == "4":
        search_product()
    if choice == "5":
        get_same_products()
    if choice == "6":
        get_same_model_products()
    if choice == "7":
        print("Exiting...")
        break

