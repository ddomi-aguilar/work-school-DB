#importar modulo
import sqlite3
#conexion
cx=sqlite3.connect('pruebaBD')

#crar cursor
cursor=cx.cursor()

#usar el cursor,creando una tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos ("+" id INTEGER PRIMARY KEY autoincrement,"+" TITULO VARCHR (255),"+" descripcion TEXT,"+" Precio INT (255)"+")")

#guardar cambios
cx.commit()

'''
#borrar datos
cursor.execute("DELETE from productos")
cx.commit() #guardar cambios
'''

'''
#insertar datos
cursor.execute("INSERT into productos VALUES (null,'Primer producto','descripcion primer producto',550)")
cx.commit #guardar cambios
'''

#insertar varios datos
productos= [
    ("computadora portatil","buena PC",700),
    ("telefono portatil","buena telefono",500),
    ("placa base","buena placa",80),
    ("tablet 5g","buena tablet",300),
]

cursor.executemany("INSERT into productos  VALUES (null,?,?,?)",productos)
cx.commit()


'''
#lista datos
cursor.execute("SELECT *FROM productos;")
'''
'''
#UPDATE
cursor.execute("UPDATE productos SET precio=700 WHERE precio=80")
cx.commit()
'''

#listar datos selecionados
cursor.execute("SELECT *FROM productos WHERE precio <=100;")
productos=cursor.fetchall()

for producto in productos:
    print("Numero de cuenta:",producto[0])
    print("Nombre:",producto[1])
    print("Apellido:",producto[2])
    print("Hora de lectura:",producto[3])
    print("\n")

productos=cursor.fetchall()

for producto in productos:
    print(producto)

    print("titulo:",producto[1])
    print("descripcion:",producto[2])
    print("descripcion:",producto[3])
    print("\n")

'''
cursor.execute ("SELECT titulo FROM productos;")
producto=cursor.fetchone()
print(producto)
'''



#cerrar conexion
cx.close



'''LOGICA DENTRO DE LA PLATAFORMA
 importar libreria
 crear la conexion
 crear el cursor
 acciones sobre la BD
 guardar cambios
 cerrar la conexion'''