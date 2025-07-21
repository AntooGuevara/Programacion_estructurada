#DICT U OBJETO para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma)

#            "nombre":"",
#           "categoria":"",
#            "clasificacion":"",
#            "genero":"idioma",
#            }

pelicula={}
def borrarpantalla():
    import os
    os.system("cls")


def esperartecla():
    input("\t Oprima cualquier tecla para continuar ...")
    borrarpantalla()



def crearPeliculas():
    borrarpantalla()
    print("\n\t.::\U0001F4DD Alta de Peliculas \U0001F4DD::. ")
    pelicula.update({"nombre":input("Ingresa el nombre: ".upper().strip())}) 
    pelicula.update({"categoria":input("Ingresa la categoria: ".upper().strip())}) 
    pelicula.update({"clasificacion":input("Ingresa la clasificacion: ".upper().strip())}) 
    pelicula.update({"genero":input("Ingresa el genero: ".upper().strip())}) 
    pelicula.update({"idioma":input("Ingresa el idioma: ".upper().strip())}) 
    input("\n\t\t :::\u2705 LA OPERACION SE REALIZO CON EXITO! \u2705:::")

def borrarPeliculas():
   borrarpantalla()
   print("\n\t .::\U0001F4DB Borrar o Quitar TODAS las Peliculas \U0001F4DB::. \n")
   resp=input("\U0001F4DBDeseas quitar o borrar todas las peliculas del sistema? (Si/No): ").lower()
   if resp=="si":
       pelicula.clear()
       input("\n\t\t ::: \u2705 LA OPERACION SE REALIZO CON EXITO! \u2705:::")

def mostrarPeliculas():
    borrarpantalla()
    print("\n\t.:: \U0001F50D Consultar o Mostrar la Pelicula \U0001F50D::. \n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"\t{(i)} : {pelicula[i]}")
    else:
        print("\t \u26A0 No hay peliculas en el sistema \u26A0")

def agregarCaracteristicaPeliculas():
    borrarpantalla()
    print("\n\t .:: \U0001F4DD Agregar Caracteristica a Peliculas \U0001F4DD::.\n")
    atributo=input("Ingresa la nueva caracteristica de la Pelicula: ").lower().strip()
    valor=input("\U0001F4DD Ingresa el valor de la caracteristica de la pelicula: ").upper().strip()
    pelicula.update({atributo:valor})

def modificarCaracteristicasPeliculas():
    borrarpantalla()
    print("\n\t .::🔁 Modificar Características de Película 🔁::.\n")
    if len(pelicula) > 0:
        for clave, valor in pelicula.items():
            print(f"\t {clave} : {valor}")
        atributo = input("\n¿Qué atributo deseas modificar?: ").lower().strip()
        if atributo in pelicula:
            nuevo_valor = input(f"Ingrese el nuevo valor para {atributo}: ").upper().strip()
            pelicula[atributo] = nuevo_valor
            print("\n\t✅ ¡Modificación exitosa!")
        else:
            print("\n\t⚠ El atributo no existe.")
    else:
        print("\t⚠ No hay películas en el sistema.")
    esperartecla()


def borrarCaracteristicaPeliculas():
    borrarpantalla()
    print("\n\t .:: 🗑️ Borrar Característica de Película ::.\n")
    if len(pelicula) > 0:
        for clave, valor in pelicula.items():
            print(f"\t{clave} : {valor}")
        atributo = input("\n¿Qué característica deseas borrar?: ").lower().strip()
        try:
            pelicula.pop(atributo)
            print("\n\t✅ Característica eliminada con éxito.")
        except KeyError:
            print(f"\n\t⚠ Error: la característica '{atributo}' no existe.")
        except Exception as e:
            print(f"\n\t⚠ Ocurrió un error inesperado: {e}")
    else:
        print("\t⚠ No hay películas registradas.")
    esperartecla()
    
def borrarCaracteristicaPeliculas2():
    borrarpantalla()
    print("\n\t .:: 🗑️ Borrar Característica de Película ::.\n")
    if len(pelicula) > 0:
        for clave, valor in pelicula.items():
            print(f"\t{clave} : {valor}")
        atributo = input("\n¿Qué característica deseas borrar?: ").lower().strip()
        if atributo in pelicula:
            pelicula.pop(atributo)
            print("\n\t✅ Característica eliminada con éxito.")
        else:
            print("\n\t⚠ Característica no encontrada.")
    else:
        print("\t⚠ No hay películas registradas.")
    esperartecla()
