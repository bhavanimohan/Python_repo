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
    cursur = connection.cursor()
    cursur.execute(query)
    emps = cursur.fetchall()
    print_emps(emps)
def update_emp():
    query2 = "update emps set name = 'cutie' where name = 'anusha'"
    cursor = connection.cursor()
    cursor.execute(query2)
    connection.commit()   

def del_emp():
    query2 = "delete from emps where age = 18"
    cursor = connection.cursor()
    cursor.execute(query2)
    connection.commit()    

def inserting():
    query2 = "insert into emps(name,age,salary,location) values ('chandu',18,23000,'ckn')"
    cursor = connection.cursor()
    c = cursor.execute(query2)
    connection.commit()    
    