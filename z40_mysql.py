import mysql.connector

con = mysql.connector.connect(host='localhost', user='root', db='cmt')
cursor = con.cursor()
# print(con)

# SELECT * FROM kunde
cursor.execute('SELECT * FROM kunde')
# # print(cursor.fetchmany(10))
print(cursor.fetchall())
# print(cursor.fetchone())

# cursor.execute("INSERT INTO kunde (vorname, nachname) VALUES ('Maria', 'Huber')")
# cursor.commit()
# print(cursor.fetchone())
#
# cursor.execute('SELECT * FROM kunde')
#
# print(cursor.fetchall())
# con.commit()
