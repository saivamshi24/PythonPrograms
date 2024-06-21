import cx_Oracle
try:#Execute the sql command
    db=cx_Oracle.connect("hr","hr","localhost:1521/xe")
    cursor=db.cursor()
    sql="delete from person where pid=2"
    cursor.execute(sql)
    db.commit()
    print("Record Deleted")
except Exception as e:
    db.rollback()
    print(e)
finally:
    db.close()