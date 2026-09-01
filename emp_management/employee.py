# from pymysql import connect
from database import my_connection

connection = my_connection()



def print_emps(emps):
    for emp in emps:
        print(f"Employee {emp[0]} information")
        print(f"EMP Name : {emp[1]}")
        print(f"EMP Age : {emp[2]}")
        print(f"EMP Salary : {emp[3]}")
        print(f"EMP Location : {emp[4]}")
        print("=====================================")

def get_all_emps():
    query = "select * from emps"
    cursor = connection.cursor()
    cursor.execute(query)
    emps = cursor.fetchall()
    print_emps(emps)
    cursor.close()
    connection.close()
  

   

  
    