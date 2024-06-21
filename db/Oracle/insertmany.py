import cx_Oracle

try:    
    db=cx_Oracle.connect("hr","hr","localhost:1521/xe")
    cur=db.cursor()
    sql="Insert into person(pid,pname) values('%d','%s')" \
    %(int(input('Person Id')),input('Person name'))
    cur.execute(sql)
    db.commit()
    db.close()
except Exception as e:
    db.rollback()
    print(e)
finally:
    print("Database connection closed")        
