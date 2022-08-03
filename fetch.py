import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'cetpa')

cursor = con.cursor()



# query
# insert

query = "Select * from detail"
cursor.execute(query)

# x = cursor.fetchone()
# x = cursor.fetchall()
x = cursor.fetchmany(2)
print(x)