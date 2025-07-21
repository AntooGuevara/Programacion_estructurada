import mysql.connector

try:
    conexion=mysql.connector.connect(
        host="Localhost",
        user="root",
        password="",
        database="bd_notas"
    )
    cursor=conexion.cursor()
    
except:
    print(f"En este momento no es posible comunicarse con el sistema, intentelo más tarde")