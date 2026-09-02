from pymysql import connect
from database import my_connection


def update_emp(to_update,to_replace):
    
    connection = my_connection()
    query2 = "update emps set name = %s where name = %s"
    values = (to_update,to_replace)
    cursor = connection.cursor()
    cursor.execute(query2,values)
    connection.commit()
    print("Students Updated Successfully !!!")
    cursor.close()
    connection.close()