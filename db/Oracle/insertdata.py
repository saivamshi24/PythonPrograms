import cx_Oracle

try:    
    db=cx_Oracle.connect("hr","hr","localhost:1521/xe")
    cursor=db.cursor()
    sql="Insert into Person(pid,pname) values(101,'John')"
    cursor.execute(sql)
    db.commit() # permanent save
    print("Row inserted successfully")
    cursor.close()
    db.close()
except Exception as e:
    db.rollback # previous position 
    print(e) 
finally:
    print("Connection closed")