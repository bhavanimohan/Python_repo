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
def delete_product(product_id):
    connection = my_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM products WHERE id=%s", (product_id,))
    connection.commit()
    print("Product deleted successfully!")
    cursor.close()
    connection.close()