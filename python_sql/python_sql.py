from pymysql import connect

connection = connect(
    host = "localhost",
    user = "root",
    password="Ammananna@12",
    database="office"
    
)

query = "select * from emps"
cursor = connection.cursor()
a = cursor.execute(query)
res = cursor.fetchall()
print(res)

query1 = "select * from emps where id = 3"
cursor = connection.cursor()
b = cursor.execute(query1)
res1 = cursor.fetchall()
print(res1)

query2 = "insert into emps(name,age,salary,location) values ('chandu',18,23000,'ckn')"
cursor = connection.cursor()
c = cursor.execute(query2)
res2 = cursor.fetchall()
print(res2)

query = "select * from emps"
cursor = connection.cursor()
a = cursor.execute(query)
res = cursor.fetchall()
print(res)

query2 = "insert into emps(name,age,salary,location) values (%s,%s,%s,%s)"
values = ("chaitu",)
cursor = connection.cursor()
c = cursor.execute(query2)
res2 = cursor.fetchall()
print(res2)