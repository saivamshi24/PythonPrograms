import cx_Oracle

try:    
    db=cx_Oracle.connect("hr","hr","localhost:1521/xe")
    cursor=db.cursor()
    sql="Update person SET pname ='"+input('Enter Name')+"'"+"where pid=101"
    cursor.close()
    db.close()
except Exception as e:
    db.rollback # previous position 
    print(e) 
finally:
    print("Connection closed")