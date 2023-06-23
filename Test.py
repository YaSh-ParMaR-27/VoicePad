import cx_Oracle
import traceback

conn = None
try:
    conn = cx_Oracle.connect("sonic/sonic@127.0.0.1/xe")
    print("Connected successfully to the db")
    print("db version : ", conn.version)
    print("User name : ",conn.username)
except cx_Oracle.DatabaseError:
    print("Sorry Connection failed!")
    print(traceback.format_exc())
finally:
    if conn is not None:
        conn.close()
        print("Disconnected Successfully!")
