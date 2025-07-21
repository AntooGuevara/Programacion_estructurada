def borrarpantalla():
    import os
    os.system("cls")
def esperartecla():
    input("\n\t\t Oprime cualquier tecla para continuar" )
    
    
def menu_principal():
    print("\n\t\t\t..::: SISTEMA DE GESTION DE NOTAS :::... \n\t\t\n\t\t\t 1️⃣  Registro  \n\t\t\t 2️⃣  Login \n\t\t\t 3️⃣  salir ")
    opcion = input("\t\t\t\t 👉 Elige una opción: ").upper()
    return opcion