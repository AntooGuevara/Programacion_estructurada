''''
List(Array)
Son colecciones o conjuntos de datos/valores bajo un mimso nombre,
para acceder a los valores se hace con un índice numérico.

Nota: sus valores si son modificables.

La lista es una coleccion ordenada y modificable.
Permite miembros duplicados.
'''
import os
os.system("clr")
#Funciones más comúnes en las listas

paises=["México", "Brasil","España","Canada"]

numeros=[23,12,100,34]

#Ordenar ascendentemente
print(numeros)
numeros.sort()
print(numeros)

print(paises)
paises.sort()
print(paises)

#Añadir o Ingresar o Insertar elementos a una lista

#1er forma
print(paises)
paises.append("Honduras") 
#2da forma
paises.insert(1,"Honduras")
print(paises)

#Eliminar/borrar o Ingresar o Insertar elementos a una lista

#1er forma
paises.pop(1)
print(paises)
#2da forma
paises.remove("Honduras")
print(paises)

#Buscar un elemento en una lista

#1er forma

resp=("brasil" in paises)
if resp:
    print("Si encontre el pais")
else:

    print("No encontré el país")

#2da forma

for i in range(0, len(paises)):
    if paises[i]=="Brasil":
        print("Si encontré el pais")
        
    else:
        print("No encontré el país")
        
#Cuántas veces aparece un elemento dentro de una lista

#numeros=[23,12,100,34]

print(f"El número 12 aparece: {numeros.count(12)} vez o veces")

numeros.append	(12)
print(f"Este número 12 aparece: {numeros.count(12)} vez o veces")


#Identificar o conocer el indice de un valor

#paises=["México", "Brasil","España","Canada"]

indice=paises.index("España")
print(indice)
paises.pop(indice)
print(paises)

#Recorrer los valores de una lista
#1er forma
for i in paises:
    print(i)
    
#2da forma
for i in range(0, len(paises)):
    print(f"El valor {i} es: {paises[i]}")    
    
#Funcion que permite unir contenido de listas
print(paises)
print(numeros)
paises.extend(numeros)
print(paises)