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
        query = "SELECT * FROM invoices LIMIT 5"
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                print(row)
                inv_num = row['invoice_number']
                print(f"{row['invoice_number']}\t{inv_num}")
except Error as e:
    print("ERROR: " + str(e))
