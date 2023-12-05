
import mysql.connector
#CREATE DATABASE IF NOT EXISTS master_python;
#use master_python;


#conexion
database=mysql.connector.connect(host="localhost",user="root",password=" ")


#print(database)

cursor=database.cursor(buffered=True)
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python1")
cursor.execute("SHOW DATABASE")

for bd in cursor:
    print(bd)
    

#crear tabla
cursor.execute(""" CREATE TABLE IF NOT EXIST vehiculos
               (id int(10) auto_increment not null,
               marca varchat(40) not null, 
               modelo varchar(40) not null, 
               precio float(10,2) not null
               )""")    

cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)


cursor.execute("INSERT INTO vehiculos VALUES (null,'opel','astra',18,500)")
database.commit()

#para insertar varios
coches=[
    ('seat','ibiza',5000),
    ('chevrolet','blazer',2000000),
    ('mercedez','claseG',5000000)
]    

cursor.execute.many("INSERT INTO vehiculos VALUES (null,%s,%s,%s),coches")
