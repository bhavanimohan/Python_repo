from pymysql import connect
def my_connection():
    connection = connect(
        host='localhost',
        user='root',
        password='Ammananna@12',
        database='ims'
    )
    return connection