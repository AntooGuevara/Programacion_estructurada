def borrarpantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperartecla():
    input("\t 🕓 Oprima cualquier tecla para continuar ...")
    borrarpantalla()



def menuprincipal():
    opcion=input("\n\t\t..:::Sistema de Gestion de Agenda de Contactos:::.. \n\n\t\t 1️⃣  Agendar contacto \n\t\t 2️⃣  Mostrar contactos \n\t\t 3️⃣  Buscar contactos por nombre \n\t\t 4️⃣  Modificar contactos \n\t\t 5️⃣  Eliminar contacto \n\t\t 6️⃣ Salir \n\n\t\t 👉  Elige una opción (1-6):" )
    return opcion
    
def agregar_contacto(agenda):
    borrarpantalla()
    print("\n\t\t ..::Agregar contactos:::..")    
    nombre=input("\n\t\t Nombre del contacto ").upper().strip()

    if nombre in agenda:
        print("\n\t\t CONTACTO YA EXISTENTE")
        esperartecla()
    else:
        telefono=input("\n\t\t Telefono del contacto").strip()
        email=input("\n\t\t Email del contacto ").lower().strip()
        #Agregar atributos (nombre con los valores de telefono y email) al diccionario
        agenda[nombre]=[telefono,email]
        print("\n\t\t ACCION REALIZADA CON EXITO")
        esperartecla()
            
            
def mostrar_contactos(agenda):
    borrarpantalla()
    print("\n\t\t ..::Mostrar Contactos::..")
    if not agenda:
        print("\n\t\t NO EXISTEN CONTACTOS ")
    else:
        for nombre,datos in agenda.items():
            print(f"{'\n\tNombre: ' + nombre} \n\t {'Telefono: '+ datos[0]} \n\t {'Email: '+ datos[1]}")
    esperartecla()

def buscar_contacto(agenda):
    borrarpantalla()
    print("\n\t\t 🔎 Buscar Contacto 🔍")
    nombre = input("Ingresa el nombre del contacto a buscar: ").upper().strip()
    if nombre in agenda:
        datos = agenda[nombre]
        print(f"\n\tNombre: {nombre} \n\tTeléfono: {datos[0]} \n\tEmail: {datos[1]}")
    else:
        print(f"\n\t \u274C No se encontró el contacto '{nombre}' \u274C")

            
def modificar_contactos(agenda):
    borrarpantalla()
    print("\n\t\t \U0001F501 .::Modificar Contactos::. \U0001F501")
    if not agenda:
        print("\n\t\t \u26A0 No existen contactos en la agenda \u26A0")
    else:
        nom=input("Ingresa el nombre del contacto que desea modificar: ").upper().strip()
        encontro=0
        for nombre,datos in agenda.items():
            if nombre==nom:
                print(f"El contacto actual es: \n\t{nombre} \n\t{'telefono:'+datos[0]}\n\t{'E-mail:'+datos[1]}")
                tel=input("Ingrese el nuevo numero de telefono: ")
                mail=input("Ingrese el nuevo e-mail: ")
                datos[0]=tel
                datos[1]=mail
                encontro+=1
        if encontro==0:
            print(f"\n\t \u274C No se encontro un contacto con el nombre {nom} para modificar \u274C")

       
        
def eliminar_contacto(agenda):
    borrarpantalla()
    encontro = 0
    conta_eliminar = input("Ingresa el nombre del contacto que deseas eliminar: ").upper().strip()
    confirmar = ""
    for nombre, datos in agenda.items():
        if nombre == conta_eliminar:
            print(f"El contacto actual es: \n\t{nombre} \n\t{'telefono:' + datos[0]}\n\t{'E-mail:' + datos[1]}")
            while confirmar != "si" and confirmar != "no":
                confirmar = input("¿Estás seguro que deseas eliminar este contacto? (Si/No): ").lower().strip()
                if confirmar != "si" and confirmar != "no":
                    print("\n\t\t \u274C Respuesta inválida. Por favor escribe 'Si' o 'No' \u274C")
            if confirmar == "si":
                agenda.pop(nombre)
                print(f"\n\t \u2705 El contacto '{nombre}' ha sido eliminado exitosamente. \u2705")
                encontro += 1
    if encontro == 0:
        print(f"\n\t \u274C No se encontró un contacto con el nombre {conta_eliminar} \u274C")
