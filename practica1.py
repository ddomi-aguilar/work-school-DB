#importar modulo
import sqlite3
#conexion
cx=sqlite3.connect('pruebaBD')

#crar cursor
cursor=cx.cursor()

#usar el cursor,creando una tabla
cursor.execute("CREATE TABLE IF NOT EXISTS alumnos ("+" id INTEGER PRIMARY KEY autoincrement,"+" TITULO VARCHR (255),"+" descripcion TEXT,"+" horas INT (255)"+")")

#guardar cambios
cx.commit()


#insertar varios datos
alumnos= [
    ("Daniela","Hueramo",80),
    ("Miguel","Vargas",80,)
    
]

cursor.executemany("INSERT into alumnos  VALUES (null,?,?,?)",alumnos)
cx.commit()


#listar datos selecionados
cursor.execute("SELECT *FROM alumnos WHERE horas <=100;")
alumnos=cursor.fetchall()


for alumno in alumnos:
    print("Numero de cuenta:",alumno[0])
    print("Nombre:",alumno[1])
    print("Apellido:",alumno[2])
    print("Horas:",alumno[3])
    print("\n")

alumnos=cursor.fetchall()


#cerrar conexion
cx.close
