import peliculas as p

peliculas = []
opcion = True

while opcion:
    p.borrarPantalla()
    print("Selecciona una opción:")
    print("1. Agregar película")
    print("2. Eliminar película")
    print("3. Modificar película")
    print("4. Consultar películas")
    print("5. Salir")
    opcion = input("Opción: ")

    match opcion:
        case "1":
            p.agregarPeliculas(peliculas)

        case "2":
            p.borrarPeliculas(peliculas)

        case "3":
            p.modificarPeliculas(peliculas)

        case "4":
            p.consultarPeliculas(peliculas)

        case "5":
            print("Saliendo del programa...")
            opcion = False

        case _:
            print("Opción no válida.")
            p.esperarTecla()
