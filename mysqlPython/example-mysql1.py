# first install the mysql connector module
# at the command line:
# py -m pip install mysql-connector-python

from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password="",
        database="ap",
    ) as connection:
        print(connection)
        query = "UPDATE vendors SET vendor_name = 'ABC Acme Inc.' WHERE vendor_id = 1"
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
except Error as e:
    print("ERROR: " + str(e))
