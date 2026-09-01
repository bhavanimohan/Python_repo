from database import my_connection
from product import get_product_details
connection = my_connection()
print("Connection established successfully!")
while True:
    print("1. Get product details")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        get_product_details()
    if choice == "2":
        break
    if choice not in ["1", "2"]:
        print("Invalid choice. Please try again.")
connection.close()