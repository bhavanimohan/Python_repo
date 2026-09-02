# from pymysql import connect
from database import my_connection

connection = my_connection()

def del_emp():
    print("""select 1 to delete name :
          select 2 to delete age :
          select 3 to delete salary :
          select 4 to delete location : """)
    user_selection= int(input("Enter the number : "))
    if user_selection == 1:
        name_to_delete = (input("Enter the name that you wanna delete : "))
        query2 = "delete from emps where name = %s"
        values = (name_to_delete)
    if user_selection == 2:
        age_to_delete = int(input("Enter the age that you wanna delete : "))
        query2 = "delete from emps where age = %s"
        values = (age_to_delete)
    if user_selection == 3:
        salary_to_delete = float(input("Enter the salary that you wanna delete : "))
        query2 = "delete from emps where salary = %s"
        values = (salary_to_delete)
    if user_selection == 4:
        location_to_delete = input("Enter the location that you wanna delete : ")
        query2 = "delete from emps where location = %s"
        values = (location_to_delete)
    cursor = connection.cursor()
    cursor.execute(query2, values)
    connection.commit()
    print("Employees Deleted Successfully !!!")
    cursor.close()
    connection.close()
    
    