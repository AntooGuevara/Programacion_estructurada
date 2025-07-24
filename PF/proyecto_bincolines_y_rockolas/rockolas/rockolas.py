from conexion import conexion, cursor
import datetime

def crear(nombre, direccion, fecha, duracion):
    try:
        sql = "INSERT INTO rockolas (nombre_cliente, direccion, fecha, duracion) VALUES (%s, %s, %s, %s)"
        val = (nombre, direccion, fecha, duracion)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except:
        return False

def mostrar():
    try:
        cursor.execute("SELECT * FROM rockolas")
        return cursor.fetchall()
    except:
        return []

def modificar(id, nombre, direccion, fecha, duracion):
    try:
        sql = "UPDATE rockolas SET nombre_cliente=%s, direccion=%s, fecha=%s, duracion=%s WHERE id=%s"
        val = (nombre, direccion, fecha, duracion, id)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except:
        return False

def eliminar(id):
    try:
        sql = "DELETE FROM rockolas WHERE id=%s"
        cursor.execute(sql, (id,))
        conexion.commit()
        return True
    except:
        return False
