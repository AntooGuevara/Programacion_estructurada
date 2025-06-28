import peliculas_dago as p

opcion=True
while opcion:
    p.borrarPantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Agregar  \n 2.- Eliminar \n 3.- Actualizar \n 4.- Consultar \n 5.- Buscar \n 6.- Vaciar \n 7.- SALIR  \n 8.- Agregar Caracteristicas \n 9.- Modificar Caracteristicas \n 10.- Borrar Caracteristicas")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            p.agregarPeliculas()
            p.esperarTecla()
            print(".:: Agregar Peliculas ::.")
        case "2":
            p.borrarPeliculas()
            p.esperarTecla()
            print(".:: Eliminar Peliculas ::.") 
        case "3":
            p.modificarPeliculas()  
            p.esperarTecla()
            print(".:: Modificar Peliculas ::.") 
        case "4":
            p.consultarPeliculas()
            p.esperarTecla()
            print(".:: Consultar Peliculas ::.")
        case "5":
            p.buscarPeliculas()
            p.esperarTecla()
            print(".:: Buscar Peliculas ::.") 
        case "6":
            p.vaciarPeliculas()
            p.esperarTecla() 
            print(".:: Vacias Peliculas ::.") 
        case "7":
            opcion=False
            p.borrarPantalla()    
            print("Terminaste la ejecucion del SW")
        case "8":
            p.borrarPantalla()
            print("Agregar caracteristicas a las peliculas" ) 
            p.esperarTecla()
            p.agregarCaracteristicaPeliculas() 
        case "9":
            p.borrarPantalla()
            print("Modificar caracteristicas a las peliculas" ) 
            p.esperarTecla()
            p.modificarCaracteristicasPeliculas()   
        case "10":
            p.borrarPantalla()
            print("Borrar caracteristicas a las peliculas" ) 
            p.esperarTecla()
            p.borrarCaracteristicas() 
        case _:
            p.borrarPantalla()
            input("Opción invalida vuelva a intentarlo ... por favor")