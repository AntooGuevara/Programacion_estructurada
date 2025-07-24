import os

def borrarpantalla():
    os.system("cls")

def esperartecla():
    input("\t 🕓 Oprima cualquier tecla para continuar ...")
    borrarpantalla()

def menu_principal():
    print("\n\t.:: Sistema de Gestión de Renta de Brincolines y Rockolas ::.")
    print("\n\t1.- Registro")
    print("\t2.- Login")
    print("\t3.- Salir")
    opcion = input("\n\t👉 Elige una opción: ").upper().strip()
    return opcion
    

def menu_principal_brincolines_rockolas():
    print("\n\t.:: Menú Principal de Rentas ::.")
    print("\n\t1.- Brincolines")
    print("\t2.- Rockolas")
    print("\t3.- Volver")
    opcion = input("\n\t👉 Elige una opción: ").upper().strip()
    return opcion

def menu_brincolines():
    print("\n\t.:: Menú Brincolines ::.")
    print("\n\t1.- Crear pedido")
    print("\t2.- Mostrar pedidos")
    print("\t3.- Modificar pedido")
    print("\t4.- Eliminar pedido")
    print("\t5.- Volver")
    opcion = input("\n\t👉 Elige una opción: ").upper().strip()
    return opcion

def menu_rockolas():
    print("\n\t.:: Menú Rockolas ::.")
    print("\n\t1.- Crear pedido")
    print("\t2.- Mostrar pedidos")
    print("\t3.- Modificar pedido")
    print("\t4.- Eliminar pedido")
    print("\t5.- Volver")
    opcion = input("\n\t👉 Elige una opción: ").upper().strip()
    return opcion
