import cx_Oracle
try:
    con=cx_Oracle.connect("hr","hr","localhost:1521/xe")
    cursor=con.cursor()
    sql="select * from person"
    cursor.execute(sql)
    results=cursor.fetchall()
    print(results)
    for rec in results: #2 Robert
    #now print all fetched records
        print(rec[0],rec[1])
except Exception as e:
    print(e)
finally:
    con.close()