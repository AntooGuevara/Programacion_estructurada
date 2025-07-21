lista=[

]
calificaciones={}
def borrarpantalla():
    import os
    os.system("cls")

def esperartecla():
    input("\t 🕓 Oprima cualquier tecla para continuar ...")
    borrarpantalla()
    
def menu_principal():
    print("\n\t\t\t..::: CONSULTA DE CALIFICACIONES :::... \n\t\t..::: Sistema de Gestión de Calificaciones :::...\n\t\t\t 1️⃣  Agregar calificaciones  \n\t\t\t 2️⃣  Mostrar calificaciones \n\t\t\t 3️⃣  Calcular promedios \n\t\t\t 4️⃣  SALIR ")
    opcion = input("\t\t\t\t 👉 Elige una opción: ").upper()
    return opcion

def agregarcalificaciones(lista):
    borrarpantalla()
    print("👤 Agregar Calificaciones")
    nombre=input("📝 Ingresa el nombre del alumno: ").upper().strip()
    calificaciones=[]
    for i in range(1,4): #aqui trabaja con solo 3 valores (1,2,3), el 4 no se usa
        continuar=True
        while continuar:
            try:
                cal=float(input(f"📝 Ingresa la calificacion {i} "))
                if cal>=0 and cal<=10:
                    calificaciones.append(cal)
                    continuar=False
                else: 
                    print("❌ Ingresa un numero valido")
                    
            except ValueError:
                print("❌ Ingresa un valor numérico")
    lista.append([nombre]+calificaciones)
    print("✅ Accion realizada con exíto")


def mostrarcalificaciones(lista):
    borrarpantalla()
    print("\t\tMostrar calificaciones")
    if len(lista)>0:
        print(f"\n\t{'Nombre':<15} {'Cal 1':<10} {'Cal 2':<10} {'Cal 3':<10}")
        print(f"{'-'*80}")
        for fila in lista:
            print(f"\t{fila[0]:<15} {fila[1]:<10} {fila[2]:<10} {fila[3]:<10}")
        print(f"{'-'*80}")
        cuantos=len(lista)
        print(f"\t\tEn total son : {cuantos} alumnos")
    else: 
        print("❌ LISTA VACIA")
        
"""def calcularpromedios(lista):
    borrarpantalla()
    print("Calculo de promedios")
    if len(lista)>0:
        for fila in lista:
            promedio =sum(fila[1:])/3
            print(f"Alumno: {fila[0]}, Promedio: {promedio:}")
    else:
        print("❌ LISTA VACIA")"""

def calcularpromedios2(lista):
    borrarpantalla()
    print("\t\t 🖨️  Mostrar Calificaciones")
    if len(lista)>0:
        print(f"\n\t\t\t{'Alumno':<15} {'Promedio':<10}")
        print(f"{'-'*80}")
        for fila in lista:
            nombre=fila[0]
            promedio_grupal=0
            promedio=sum(fila[1:])/3
            print(f"\t\t\t{nombre:<15}{promedio:<10}") 
            
            promedio_grupal+=promedio
        print(f"{'-'*80}")
        promedio_grupal=promedio_grupal/len(lista)
        print(f"\t\t\tEl promedio grupal es: {promedio_grupal}")      
        esperartecla()   

    else:
        print("❌ NO EXISTEN CALIFICACIONES")
            
def buscarcalificacion(lista):
    borrarpantalla()
    print("\t\tBuscar Calificaciones")
    if len(lista)>0:
        nombre=input("📝 Ingresa el nombre del alumno a buscar: ").upper().strip()
        encontrado=False
        for fila in lista:
            if fila[0]==nombre:
                encontrado=True
                print(f"\n\t{'Nombre':<15} {'Cal 1':<10} {'Cal 2':<10} {'Cal 3':<10}")
                print(f"{'-'*80}")
                print(f"\t{fila[0]:<15} {fila[1]:<10} {fila[2]:<10} {fila[3]:<10}")
                print(f"{'-'*80}")
                promedio=sum(fila[1:])/3
                print(f"\tEl promedio de {fila[0]} es: {promedio:.2f}")
        if not encontrado:
            print("❌ El alumno no se encuentra en la lista")
    else:
        print("❌ LISTA VACIA")
        
    
    
        
            
           