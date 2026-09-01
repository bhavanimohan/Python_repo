[33mcommit a8b10d78ad3bad9d6361e613f8093c7bbc74e784[m[33m ([m[1;36mHEAD[m[33m -> [m[1;32mmain[m[33m, [m[1;31morigin/main[m[33m, [m[1;31morigin/HEAD[m[33m)[m
Author: Bhavani Mohan <bhavanimohan200@gmail.com>
Date:   Tue Sep 1 22:02:09 2026 +0530

    Update product module

[1mdiff --git a/Inventory_management_system/product.py b/Inventory_management_system/product.py[m
[1mindex cd883d7..4134d86 100644[m
[1m--- a/Inventory_management_system/product.py[m
[1m+++ b/Inventory_management_system/product.py[m
[36m@@ -35,4 +35,12 @@[m [mdef update_product(product_id, name, category, price, quantity, supplier):[m
     connection.commit()[m
     print("Product updated successfully!")[m
     cursor.close()[m
[32m+[m[32m    connection.close()[m
[32m+[m[32mdef delete_product(product_id):[m
[32m+[m[32m    connection = my_connection()[m
[32m+[m[32m    cursor = connection.cursor()[m
[32m+[m[32m    cursor.execute("DELETE FROM products WHERE id=%s", (product_id,))[m
[32m+[m[32m    connection.commit()[m
[32m+[m[32m    print("Product deleted successfully!")[m
[32m+[m[32m    cursor.close()[m
     connection.close()[m
\ No newline at end of file[m
