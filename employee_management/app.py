from employee import get_all_emps
from employee_update import update_emp
from employee_inserting import inserting
from employee_delete import del_emp



print("======= Employee Management Platform ===============")

while True:
    option = input("""To see all employess type :  1 : to get all employee details 
                   2 : insert values 
                   3 : update employee
                   4 : delete employee
                   5 : to Exit  - """)
    if option == "1":
        get_all_emps()
    if option == "2":
        name_to_insert=input("Enter the name you wanna insert : ")
        age_to_insert = int(input("Enter the age that wanna insert : "))
        salary_to_insert = float(input("Enter the salary that wanna insert : "))
        location_to_insert= input("Enter the location to insert : ")
        inserting(name_to_insert,age_to_insert,salary_to_insert,location_to_insert)
    if option == "3":
        
        update_emp()
    if option == "4":
        del_emp()
    if option == "5":
        break
    
        