#EJEMPL1O: 
# Crear una lista de numeros e imprimir el contenido.
import os
num=[10,22,43,4,75]
print(num)

for i in num:
    print (i)
    
for i in range (0, len(num)):
    print (num[i])    
 
os.system("cls")
#EJEMPLO 2
#Crear una lista de palabras y posteriormente buscar la coindicencia de una palabra

buscarpalabra=input("dame la palabra a buscar ")


palabra=["hola","adios","vaca","burro","vaca"]
contador=palabra.count(buscarpalabra)

print(f"el número de veces que se encontró una palabra es de: {contador}")

#1er forma
if buscarpalabra in palabra:
    print(f"si se encontró la palabra")
else:
    print("no se encontró la palabra")

#2da forma
encontro=False
for i in palabra:
    if i == buscarpalabra:
        encontro=True
       
if encontro:    
    print(f"si se encontró la palabra")
else:
    print(f"no se encontró la palabra ")
    
#3er forma
encontro=False
for i in range(0, len(palabra)):
    if palabra[i]==buscarpalabra:
        encontro=True
       
if encontro:    
    print(f"si se encontró la palabra")
else:
    print(f"no se encontró la palabra ")
    
    
os.system("cls")
#EJEMPLO 3
#Añadir elementos a una lista


numeros=[]

opcion=True
while opcion:
    numero=float(input("dame un número entero o decimal "))
    numeros.append(numero)
    resp=input("deseas agregar otro número ").lower()
    print(numeros)
    if resp=="si":
        opcion=True
    else:
        opcion=False
      
os.system("cls")  
#EJEMPLO 4
#Crear una lista multidimensional que sea una agenda

agenda=[
        ["Carlos","6183493498"],
        ["Alberto","6673842812"],
        ["Martin","6673451234"],
        
       ]

print(agenda)

for i in agenda:
    print(i)
    
for r in range(0,3):
    for c in range(0,2):
        print(agenda[r],[c])
        
cadena=""
for r in range(0,3):
    for c in range(0,2):
        cadena+=f"{agenda[r] [c]},"
    cadena+="\n"
print(cadena)
        
        
        