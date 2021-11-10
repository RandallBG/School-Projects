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

        stateToFind = input("Select a state to search for a vendor");
        print(connection)
        query = f"SELECT * FROM vendors WHERE vendor_state = '{stateToFind}'"
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                # print(row)
                vendor_id = row[0]
                vendor_name = row[1]
                vendor_state = row[5]
                print(f"{vendor_id}\t{vendor_name}\t{vendor_state}")
except Error as e:
    print("ERROR: " + str(e))
