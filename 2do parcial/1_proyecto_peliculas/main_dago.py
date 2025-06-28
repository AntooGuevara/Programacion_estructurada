import peliculas

opcion = True
while opcion:
    print(
        "\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Crear  \n\t\t 2.- Borrar \n\t\t 3.- Mostrar \n\t\t 4.- Agregar caracteristicas \n\t\t 5.- Modificar caracteristicas \n\t\t 6.- Borrar caracteristicas \n\t\t 7.- SALIR "
    )
    opcion = input("\t\t\t Elige una opción: ").upper()

    peliculas.borrarpantalla()
    match opcion:
        case "1":
            print(".:: Agregar Peliculas ::.")
            peliculas.crearPeliculas()
            peliculas.esperartecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperartecla()
        case "3":
            peliculas.mostrarPeliculas()
            input("Oprima cualquier tecla para continuar ...")
        case "4":
            peliculas.agregarCaracteristicaPeliculas()
            peliculas.esperartecla()
        case "5":
            peliculas.modificarCaracteristicasPeliculas()
            peliculas.esperartecla()
        case "6":
            peliculas.borrarCaracteristicaPeliculas()
            peliculas.esperartecla()
        case "7":
            opcion = False
            peliculas.borrarpantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case _:
            peliculas.borrarpantalla()
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")