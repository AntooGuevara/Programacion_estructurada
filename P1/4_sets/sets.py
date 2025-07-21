""""
Es un tipo de datos que para tener una coleccion de valores pero no tiene ni indice ni orden.

Set es una coleccion desordenada, inmutable* y no indexeada.
No hay miembros duplicados

"""
import os
os.system("cls")
#EJEMPLO 1

personas={"Juan", "Pedro", "Maria"}
print(personas)  
personas.add("Jose")  #Añadir un elemento 
print(personas)
personas.pop() #Eliminar un elemento
print(personas)
personas.clear
print(personas)  #Limpiar el set

varios={3.12,True,"hola"}
print(varios)

#ejemplo crear un programa que solicite los emails de los alumnos de la utd
#y almacenar en una lista, posteriormente mostrar en pantalla los emails que no se repiten

os.system("cls")

opc="si"
emails=[]
while opc=="si":
    emails.append(input("Dame los emails de los alumnos: "))
    print(emails)
    opc=input("¿Deseas ingresar otro email? (si/no): ").lower()
    
    
#imprimir los emails sin duplicados
print(emails)
set1=set(emails)  #Convertir la lista a un set para eliminar duplicados
print(set1)
emails=list(set1)  #Convertir el set a una lista
print(emails)  #Imprimir la lista sin duplicados

