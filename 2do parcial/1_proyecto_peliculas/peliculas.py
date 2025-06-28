# peliculas.py
def borrarPantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def esperarTecla():
    input("Oprima cualquier tecla para continuar ...")

def agregarPeliculas(peliculas):
    borrarPantalla()
    print(".:: Alta de Peliculas ::.")
    pelicula = input("Ingresa el nombre: ").upper().strip()
    peliculas.append(pelicula)
    esperarTecla()

def consultarPeliculas(peliculas):
    borrarPantalla()
    print(".:: Consultar Peliculas ::.")
    if len(peliculas) > 0:
        for i in peliculas:
            print(i)
    else:
        print("No hay peliculas registradas.")
    esperarTecla()

def borrarPeliculas(peliculas):
    borrarPantalla()
    print(".:: Eliminar Peliculas ::.")
    pelicula_borrar = input("Ingresa el nombre de la pelicula a eliminar: ").upper().strip()
    if pelicula_borrar in peliculas:
        peliculas.remove(pelicula_borrar)
        print(f"La pelicula {pelicula_borrar} ha sido eliminada exitosamente.")
    else:
        print(f"La pelicula {pelicula_borrar} no se encuentra en la lista.")
    esperarTecla()

def modificarPeliculas(peliculas):
    borrarPantalla()
    print(".:: Modificar Peliculas ::.")
    pelicula_modificar = input("Ingresa el nombre de la pelicula que quieres modificar: ").upper().strip()
    if pelicula_modificar in peliculas:
        nuevo_nombre = input("Ingresa el nuevo nombre de la pelicula: ").upper().strip()
        index = peliculas.index(pelicula_modificar)
        peliculas[index] = nuevo_nombre
        print(f"La pelicula {pelicula_modificar} ha sido modificada a {nuevo_nombre}.")
    else:
        print(f"La pelicula {pelicula_modificar} no se encuentra en la lista.")
    esperarTecla()
