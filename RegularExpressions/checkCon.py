import cx_Oracle

try:    
    db=cx_Oracle.connect("hr","hr","localhost:1521/xe")
    cursor=db.cursor()
    if(cursor == None):
        raise Exception
    print("Connected to database")
    cursor.close()
    db.close()
except Exception as e:
    print(e) 
finally:
    print("Closing database")