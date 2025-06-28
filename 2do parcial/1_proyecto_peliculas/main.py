""""crear un proyecto que permita gestionar (administrar) peliculas, colocar un menú de opciones para colocar,
eliminar, modificar y consultar peliculas. 
Notas:
1- utilizar funciones y mandar a llamar desde otro archivo
2- utilizar listas para almacenar nombres de las peliculas
3-

"""

import os
import peliculas as p
opcion=True
while opcion:

    opcion=input("selecciona una opcion: \n1. Agregar pelicula\n2. Eliminar pelicula\n3. Modificar pelicula\n4. Consultar peliculas\n5. Salir\n")

    match opcion:
            case "1":
                    p.borrar_pantalla()
                    print("Agregar pelicula")
                    p.agregar_pelicula()

            case "2":
                    p.eliminar_pelicula()
                    p.borrar_pantalla()
                    print("Eliminar pelicula")

            case "3":
                    p.borrar_pantalla()
                    p.modificar_pelicula()
                    print("Modificar pelicula")
                    modificar=input("Ingresa el nombre de la pelicula que quieras modificar: ")
            case "4": 
                    p.borrar_pantalla()
                    print("consultar peliculas")
                    p.consultar_peliculas
            case '5': 
                    print("Salir")
                    opcion=False
            
                          

