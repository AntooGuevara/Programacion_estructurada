from conexion import conexion, cursor
import datetime
from datetime import datetime

def crear(nombre, direccion, duracion):
    try:
        fecha_actual = datetime.now().strftime('%Y-%m-%d')  # Formato YYYY-MM-DD
        sql = "INSERT INTO rockolas (nombre_cliente, direccion, fecha, duracion) VALUES (%s, %s, %s, %s)"
        val = (nombre, direccion, fecha_actual, duracion)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al crear rockola: {e}")
        return False

def mostrar():
    try:
        cursor.execute("SELECT * FROM rockolas")
        return cursor.fetchall()
    except:
        return []

from datetime import datetime

def modificar(id, nombre, direccion, duracion):
    try:
        fecha_actualizacion = datetime.now().strftime('%Y-%m-%d')
        sql = """UPDATE rockolas 
                SET nombre_cliente=%s, direccion=%s, duracion=%s, fecha=%s
                WHERE id=%s"""
        val = (nombre, direccion, duracion, fecha_actualizacion, id)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al modificar rockola: {e}")
        return False

def eliminar(id):
    try:
        sql = "DELETE FROM rockolas WHERE id=%s"
        cursor.execute(sql, (id,))
        conexion.commit()
        return True
    except:
        return False