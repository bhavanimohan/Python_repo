# from pymysql import connect
from database import my_connection


def update_emp():
    print("""select 1 to change name :
          select 2 to change age :
          select 3 to change salary :  
          select 4 to change location : """)
    user_selection= int(input("Enter the number :  "))
    if user_selection == 1:
        id = int(input("Enter the id where  you wanna update : "))
        to_update_name = input("Enter the name that you wanna update it : ")
        query = "update emps set name = %s where id = %s"
        values = (to_update_name,id)
        
    elif user_selection == 2:
        id = int(input("Enter the id where you wanna update : "))
        to_update_age = int(input("Enter the age that you wanna update it : "))
        query = "update emps set age = %s where id = %s"
        values = (to_update_age,id)
    elif user_selection == 3:
        id = int(input("Enter the id where you wanna update : "))
        to_update_salary = float(input("Enter the salary that you wanna update it : "))
        query = "update emps set salary = %s where id = %s"
        values = (to_update_salary,id)
    elif user_selection == 4:
        id = int(input("Enter the id where you wanna update : "))
        to_update_location = input("Enter the location that you wanna update it : ")
        query = "update emps set location = %s where id = %s"
        values = (to_update_location,id)

    connection = my_connection()
    cursor = connection.cursor()
    cursor.execute(query,values)
    connection.commit()
    print("Employees Updated Successfully !!!")
    cursor.close()
    connection.close()