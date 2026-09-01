
from database import my_connection

connection = my_connection()

def inserting(name_to_insert,age_to_insert,salary_to_insert,location_to_insert):
    query2 = "insert into emps(name,age,salary,location) values (%s,%s,%s,%s)"
    values = (name_to_insert,age_to_insert,salary_to_insert,location_to_insert)
    cursor = connection.cursor()
    cursor.execute(query2,values)
    connection.commit()  
    print("Student added successfully !!!!!")
    cursor.close()
    connection.close()