from database import my_connection
connection = my_connection()
def get_product_details():
    connection = my_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    print_products(products)
    

def print_products(products):

    for product in products:

        print("----------------------------------------")
        print(f"Product ID : {product[0]}")
        print(f"Name       : {product[1]}")
        print(f"Category   : {product[2]}")
        print(f"Price      : ₹{product[3]}")
        print(f"Quantity   : {product[4]}")
        print(f"Supplier   : {product[5]}")
        print("----------------------------------------")
def delete_product(product_id):
    user_selection = int(input("""Enter the number to delete by :
                               1. ID 
                               2. Name
                               3. Category """))  
    if user_selection == 1:
        product_id = int(input("Enter the id to delete : "))
        user_confirmation = input(f"Are you sure you want to delete the product with ID {product_id}? (yes/no): ")
        if user_confirmation.lower() == "yes":
            query = "DELETE FROM products WHERE id=%s"
            values = (product_id)
            connection = my_connection()
            cursor = connection.cursor()
            cursor.execute(query, values)
            connection.commit()
            print("Product deleted successfully!")
            cursor.close()
            connection.close()
            print("Product deletion Agreed.")
        else:
            print("Product deletion Not Agreed.")
            return     
            
        
    if user_selection == 2:
        product_name = input("Enter the name to delete : ")
        query = "DELETE FROM products WHERE name=%s"
        values = (product_name)
        user_confirmation = input(f"Are you sure you want to delete the product with name {product_name}? (yes/no): ")
        if user_confirmation.lower() == "yes":
            connection = my_connection()
            cursor = connection.cursor()
            cursor.execute(query, values)
            connection.commit()
            print("Product deleted successfully!")
            cursor.close()
            connection.close()
        else:
            print("Product deletion Not Agreed.")
            return
        
    if user_selection == 3:
        product_category = input("Enter the category to delete : ")
        query = "DELETE FROM products WHERE category=%s"
        values = (product_category)
        user_confirmation = input(f"Are you sure you want to delete the product with category {product_category}? (yes/no): ")
        if user_confirmation.lower() != "yes":
            print("Product deletion Agreed.")
            connection = my_connection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM products WHERE id=%s", (product_id,))
            connection.commit()
            print("Product deleted successfully!")
            cursor.close()
            connection.close()
        else:
            print("Product deletion Not Agreed.")
            return

        
def add_product(name,category,price,quantity,supplier):
    connection = my_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO products (name, category, price, quantity, supplier) VALUES (%s, %s, %s, %s, %s)", (name, category, price, quantity, supplier))
    connection.commit()
    print("Product added successfully!")
    cursor.close()
    connection.close()
def update_product(product_id, name, category, price, quantity, supplier):
    connection = my_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE products SET name=%s, category=%s, price=%s, quantity=%s, supplier=%s WHERE id=%s", (name, category, price, quantity, supplier, product_id))
    connection.commit()
    print("Product updated successfully!")
    cursor.close()
    connection.close()

def search_product():
    user_selection = int(input("""Enter the number to search by : 
                               1. Name 
                               2. Category 
                               3. Supplier : """))
    if user_selection == 1:
        name_to_search = input("Enter the name to search : ")
        query = "SELECT * FROM products WHERE name LIKE %s"
        values = ('%' + name_to_search + '%',)
    if user_selection == 2:
        category_to_search = input("Enter the category to search : ")
        query = "SELECT * FROM products WHERE category LIKE %s"
        values = ('%' + category_to_search + '%',)
    if user_selection == 3:
        supplier_to_search = input("Enter the supplier to search : ")
        query = "SELECT * FROM products WHERE supplier LIKE %s"
        values = ('%' + supplier_to_search + '%',)
    connection = my_connection()
    cursor = connection.cursor()
    cursor.execute(query, values)
    products = cursor.fetchall()
    if products:
        print_products(products)
    else:
        print("No products found with the given name.")
    cursor.close()
    connection.close()
