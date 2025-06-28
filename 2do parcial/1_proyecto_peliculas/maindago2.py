# Crear un proyeto que permita gestionar (administrar) peliculas, colocar un menu de opciones
# para agregar, eliminar, modificar y consultar peliculas
# Notas:
# 1.- Utilizar funciones y mandar llamar desde otro archivo
# 2.- Utilizar listas para almacenar los nombres de peliculas
import peliculas

opcion = True
while opcion:
    print(
        "\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Agregar  \n\t\t 2.- Eliminar \n\t\t 3.- Actualizar \n\t\t 4.- Consultar \n\t\t 5.- Buscar \n\t\t 6.- Vaciar \n\t\t 7.- SALIR "
    )
    opcion = input("\t\t\t Elige una opción: ").upper()
    peliculas.borrarpantalla()
    match opcion:
        case "1":
            peliculas.borrarpantalla()
            print(".:: Agregar Peliculas ::.")
            peliculas.agregarpeliculas()
            peliculas.esperartecla()
        case "2":
            peliculas.borrarpeliculas()
            peliculas.esperartecla()
        case "3":
            peliculas.borrarpantalla()
            print(".:: Modificar Peliculas ::.")
            input("Oprima cualquier tecla para continuar ...")
        case "4":
            peliculas.consultarpeliculas()
            peliculas.esperartecla()
        case "5":
            peliculas.buscarpeliculas()
            peliculas.esperartecla()
        case "6":
            peliculas.vaciarpeliculas()
            peliculas.esperartecla()

        case "7":
            peliculas.agregarcaracteristicapeliculas()
            peliculas.esperartecla()

        case "8":
            peliculas.modificarcaracteristicaspeliculas()
            peliculas.esperartecla()

        case "9":
            peliculas.borrarcaracteristicas()
            peliculas.esperartecla()

        case "10":
            opcion = False
            peliculas.borrarpantalla()
            print("\n\tTerminaste la ejecucion del SW")

        case _:
            peliculas.borrarpantalla()
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")
