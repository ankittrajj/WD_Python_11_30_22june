import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'cetpa')

cursor = con.cursor()

name = input("Enter your name")
age = int(input("enter your age"))
salary = float(input("Enter the salary"))

# query
# insert

query = "Insert into detail values('{}',{},{})".format(name,age,salary)
cursor.execute(query)
con.commit()
print("Data entered successfully!!")