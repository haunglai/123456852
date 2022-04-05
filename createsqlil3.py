import sqlite3

conn=sqlite3.connect('mrsoft.db')
cursor=conn.cursor()
sql='insert into user (id,name) values(?,?)'
#cursor.execute(sql,(2,'xiaoming'))
data={(3,'andy'),(4,'kobe'),(5,'jordan')}
cursor.executemany(sql,data)
cursor.close()
conn.commit()
conn.close
