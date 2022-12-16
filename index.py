import sqlite3

def main():
    # Insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla
    id = int(input("Introduce una id"))
    nm = input("Introduce un nombre").capitalize()
    ap = input("Introduce un apellido").capitalize()
    crear_alumnos(id, nm, ap)
    # Búsqueda de un alumno por nombre y mostrar los datos por consola.
    nombre = input("Buscar nombre de alumno...").capitalize()
    buscar_alumnos(nombre)

def buscar_alumnos(nombre):
    conn = sqlite3.connect('db/instituto.db')
    cursor = conn.cursor()
    query = f'SELECT nombre, apellido FROM alumnos WHERE nombre = "{nombre}"'
    rows = cursor.execute(query)
    for row in rows:
        print(row)
    cursor.close()
    conn.close()

# crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto
def crear_alumnos(id, nombre, apellido):
    conn = sqlite3.connect('db/instituto.db')
    cursor = conn.cursor()
    query = '''INSERT INTO alumnos(id, nombre, apellido) VALUES(?, ?, ?)'''
    cursor.execute(query, (id, nombre, apellido))
    conn.commit()
    cursor.close()
    conn.close()

# "id"    "nombre"   "apellido"
# "1"	  "Jordi"	 "Alsina"
# "2"	  "Laia"	 "Wisiston"
# "3"	  "Sara"	 "Smith"
# "4"	  "Alex"	 "Erinson"
# "5"	  "Sonia"	 "Hamilton"
# "6"	  "Karla"	 "Perez"
# "7"	  "Cesar"	 "Yi"
# "8"	  "Ona"	     "Martin"
# "9"	  "Jordi"	 "Erinson"
# "10"    "Laia"	 "Giberk"

if __name__ == '__main__':
    main()