import cx_Oracle

try:    
    db=cx_Oracle.connect("hr","hr","localhost:1521/xe")
    cursor=db.cursor()
    sql="create table Person(pid number primary key,pname varchar(20))"
    cursor.execute(sql)
    print("Table created successfully")
    cursor.close()
    db.commit() # TCL --> commit saves the data permanently
    db.close()
except Exception as e:
    print(e) 
finally:
    print("Closing database")