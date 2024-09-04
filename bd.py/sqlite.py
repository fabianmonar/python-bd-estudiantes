import sqlite3
from estudiantes import Estudiante

# Conectar a la base de datos
conn = sqlite3.connect('universidad.db')
c = conn.cursor()

# Crear la tabla solo si no existe
c.execute(""" CREATE TABLE IF NOT EXISTS estudiantes(
    matricula TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    promedio REAL )""")

# Confirmar los cambios
conn.commit()

# Crear instancias de Estudiante
est_1 = Estudiante('222', 'Adriana', 'Cruz', 9.5)
est_2 = Estudiante('333', 'Fabian', 'Romero', 9.0)
est_3 = Estudiante('444', 'Alejandro', 'Cruz', 9.5)
est_4 = Estudiante('555', 'Karen', 'Barrera', 9.5)

# Función para insertar si no existe la matrícula
def insertar_estudiante(estudiante):
    c.execute("SELECT COUNT(*) FROM estudiantes WHERE matricula = ?", (estudiante.matricula,))
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO estudiantes VALUES (?, ?, ?, ?)", 
                  (estudiante.matricula, estudiante.nombre, estudiante.apellido, estudiante.promedio))
    else:
        print(f"El estudiante con matrícula {estudiante.matricula} ya existe en la base de datos.")

# Intentar insertar los estudiantes
insertar_estudiante(est_1)
insertar_estudiante(est_2)
insertar_estudiante(est_3)
insertar_estudiante(est_4)

# Confirmar los cambios
conn.commit()

# Consultar e imprimir los registros
c.execute("SELECT * FROM estudiantes")
estudiantes = c.fetchmany(5)
print(estudiantes)

# Cerrar la conexión
conn.close()