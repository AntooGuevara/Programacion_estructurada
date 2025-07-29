import funciones as f
import getpass
from usuarios import usuarios as usuario
from brincolines.brincolines import crear, mostrar, modificar, eliminar
from rockolas.rockolas import crear as crear_rockola, mostrar as mostrar_rockola, modificar as modificar_rockola, eliminar as eliminar_rockola
import rockolas.rockolas as rockolas
import datetime

# Menú de registro e inicio de sesión
def main():
    opcion = True
    while opcion:
        f.borrarpantalla()
        opcion = f.menu_principal()

        if opcion == "1" or opcion == "REGISTRO":
            f.borrarpantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre = input("\t ¿Cuál es tu nombre?: ").upper().strip()
            apellidos = input("\t ¿Cuáles son tus apellidos?: ").upper().strip()
            email = input("\t Ingresa tu email: ").lower().strip()
            password = getpass.getpass("\t Ingresa tu contraseña: ").strip()

            resultado = usuario.registrar(nombre, apellidos, email, password)
            if resultado:
                print(f"\n\t✅ {nombre} {apellidos} se registró correctamente con el email: {email}")
                f.esperartecla()
                f.borrarpantalla()  
                
            else:
                print(f"\n\t❌ No fue posible registrar al usuario, intente de nuevo.")
            f.esperartecla()
            f.borrarpantalla()

        elif opcion == "2" or opcion == "LOGIN":
            f.borrarpantalla()
            print("\n \t ..:: Inicio de Sesión ::..")
            email = input("\t Ingresa tu E-mail: ").lower().strip()
            password = getpass.getpass("\t Ingresa tu contraseña: ").strip()

            registro = usuario.iniciar_sesion(email, password)
            if registro:
                print(f"\n\t✅ Bienvenido {registro[1]} {registro[2]}")
                f.esperartecla()
                menu_brincolines_rockolas()  # redirigir al menú de brincolines y rockolas
            else:
                print(f"\n\t❌ Email o contraseña incorrectos.")
                f.esperartecla()
                f.borrarpantalla()

        elif opcion == "3" or opcion == "SALIR":
            print("Terminó la ejecución del sistema.")
            opcion = False
            f.esperartecla()
            f.borrarpantalla()
        else:
            print("Opción no válida.")
            opcion = True
            f.esperartecla()
            f.borrarpantalla()

def menu_brincolines_rockolas():
    while True:
        f.borrarpantalla()
        opcion2 = f.menu_principal_brincolines_rockolas()
        if opcion2 == "1" or opcion2 == "BRINCOLINES":
            f.borrarpantalla()
            while True:
                f.borrarpantalla()
                op = f.menu_brincolines()
                if op == "1":  # Crear pedido
                    nombre = input("Nombre cliente: ").strip()
                    direccion = input("Dirección: ").strip()
                    duracion = int(input("Duración (horas): "))
                    if crear(nombre, direccion, duracion):
                        print("✅ Pedido creado con éxito.")
                    else:
                        print("❌ Error al crear el pedido.")
                    f.esperartecla()
                    f.borrarpantalla()

                elif op == "2":  # Mostrar pedidos
                    f.borrarpantalla()
                    pedidos = mostrar()
                    if len(pedidos) > 0:
                        print(f"{'ID':<10} {'NOMBRE':<20} {'DIRECCION':<30} {'FECHA':<15} {'DURACION':<10}")
                        print("-"*85)
                        for p in pedidos:
                            print(f"{p[0]:<10} {p[1]:<20} {p[2]:<30} {p[3].strftime('%Y-%m-%d'):<15} {p[4]:<10}")
                        print("-"*85)
                    else:
                        print("❌ No hay pedidos en brincolines.")
                    f.esperartecla()
                    f.borrarpantalla()

                elif op == "3":  # Modificar pedido
                    f.borrarpantalla()
                    pedidos = mostrar()
                    if len(pedidos) > 0:
                        print(f"{'ID':<10} {'NOMBRE':<20} {'DIRECCION':<30} {'FECHA':<15} {'DURACION':<10}")
                        print("-"*85)
                        for p in pedidos:
                            print(f"{p[0]:<10} {p[1]:<20} {p[2]:<30} {p[3].strftime('%Y-%m-%d'):<15} {p[4]:<10}")
                        print("-"*85)
                        try:
                            id = int(input("ID a modificar: "))
                            nombre = input("Nuevo nombre: ")
                            direccion = input("Nueva dirección: ")
                            duracion = int(input("Nueva duración: "))
                            if modificar(id, nombre, direccion, duracion):
                                print("✅ Modificado correctamente.")
                            else:
                                print("❌ Error al modificar.")
                        except ValueError:
                            print("❌ ID inválido.")
                    f.esperartecla()
                    f.borrarpantalla()

                elif op == "4":  # Eliminar pedido
                    f.borrarpantalla()
                    pedidos = mostrar()
                    if len(pedidos) > 0:
                        print(f"{'ID':<10} {'NOMBRE':<20} {'DIRECCION':<30} {'FECHA':<15} {'DURACION':<10}")
                        print("-"*85)
                        for p in pedidos:
                            print(f"{p[0]:<10} {p[1]:<20} {p[2]:<30} {p[3].strftime('%Y-%m-%d'):<15} {p[4]:<10}")
                        print("-"*85)
                        try:
                            id = int(input("ID a eliminar: "))
                        except ValueError:
                            print("❌ ID inválido.")
                            f.esperartecla()
                            f.borrarpantalla()
                            continue
                        if eliminar(id):
                            print("✅ Eliminado correctamente.")
                        else:
                            print("❌ Error al eliminar.")
                    else:
                        print("❌ No hay pedidos para eliminar en brincolines.")
                    f.esperartecla()
                    f.borrarpantalla()

                elif op == "5":  # Volver
                    break
                else:
                    print("Opción inválida.")
                    f.esperartecla()
                    f.borrarpantalla()

        elif opcion2 == "2" or opcion2 == "ROCKOLAS":
            f.borrarpantalla()
            while True:
                f.borrarpantalla()
                op = f.menu_rockolas()
                if op == "1":  # Crear pedido
                    f.borrarpantalla()
                    nombre = input("Nombre cliente: ").strip()
                    direccion = input("Dirección: ").strip()
                    duracion = int(input("Duración (horas): "))
                    if crear_rockola(nombre, direccion, duracion):
                        print("✅ Pedido creado con éxito.")
                    else:
                        print("❌ Error al crear el pedido.")
                    f.esperartecla()
                    f.borrarpantalla()

                elif op == "2":  # Mostrar pedidos
                    f.borrarpantalla()
                    pedidos = rockolas.mostrar()
                    if len(pedidos) > 0:
                        print(f"{'ID':<10} {'NOMBRE':<20} {'DIRECCION':<30} {'FECHA':<15} {'DURACION':<10}")
                        print("-"*85)
                        for p in pedidos:
                            print(f"{p[0]:<10} {p[1]:<20} {p[2]:<30} {p[3].strftime('%Y-%m-%d'):<15} {p[4]:<10}")
                        print("-"*85)
                    else:
                        print("❌ No hay pedidos en rockolas.")
                    f.esperartecla()
                    f.borrarpantalla()

                elif op == "3":  # Modificar pedido
                    f.borrarpantalla()
                    pedidos = mostrar_rockola()
                    if len(pedidos) > 0:
                        print(f"{'ID':<10} {'NOMBRE':<20} {'DIRECCION':<30} {'FECHA':<15} {'DURACION':<10}")
                        print("-"*85)
                        for p in pedidos:
                            print(f"{p[0]:<10} {p[1]:<20} {p[2]:<30} {p[3].strftime('%Y-%m-%d'):<15} {p[4]:<10}")
                        print("-"*85)
                        try:
                            id = int(input("ID a modificar: "))
                            nombre = input("Nuevo nombre: ")
                            direccion = input("Nueva dirección: ")
                            duracion = int(input("Nueva duración: "))
                            if modificar_rockola(id, nombre, direccion, duracion):
                                print("✅ Modificado correctamente.")
                            else:
                                print("❌ Error al modificar.")
                        except ValueError:
                            print("❌ ID inválido.")
                            f.esperartecla()
                            f.borrarpantalla()
                            

                elif op == "4":  # Eliminar pedido
                    f.borrarpantalla()
                    pedidos = rockolas.mostrar()
                    if len(pedidos) > 0:
                        print(f"{'ID':<10} {'NOMBRE':<20} {'DIRECCION':<30} {'FECHA':<15} {'DURACION':<10}")
                        print("-"*85)
                        for p in pedidos:
                            print(f"{p[0]:<10} {p[1]:<20} {p[2]:<30} {p[3].strftime('%Y-%m-%d'):<15} {p[4]:<10}")
                        print("-"*85)
                        try:
                            id = int(input("ID a eliminar: "))
                        except ValueError:
                            print("❌ ID inválido.")
                            f.esperartecla()
                            f.borrarpantalla()
                            continue
                        if rockolas.eliminar(id):
                            print("✅ Eliminado correctamente.")
                        else:
                            print("❌ Error al eliminar.")
                    else:
                        print("❌ No hay pedidos para eliminar en rockolas.")
                    f.esperartecla()
                    f.borrarpantalla()

                elif op == "5":  # Volver
                    break
                else:
                    print("Opción inválida.")
                    f.esperartecla()
                    f.borrarpantalla()

        elif opcion2 == "3" or opcion2 == "VOLVER":
            return
        else:
            print("Opción no válida.")
            f.esperartecla()
            f.borrarpantalla()


#para que ejecute todos los menú
if __name__ == "__main__":
    main() 