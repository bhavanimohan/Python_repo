# from pymysql import connect
from database import my_connection

connection = my_connection()

def del_emp(name_to_delete):
    query2 = "delete from emps where age = %s"
    values = (name_to_delete)
    cursor = connection.cursor()
    cursor.execute(query2,values)
    connection.commit() 
    print("Students Deleted Successfully !!!")
    cursor.close()
    connection.close()
    
    