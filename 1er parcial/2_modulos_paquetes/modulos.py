''''
Un modulo es simplemente un archivo con extensión .py que contiene un 
código de python (funciones, clases, variables, etc.)

Un paquete es una carpeta que contiene varios módulos, (arhivos py)
y un archivo especial llamado __init__.py, que le indica a python que
esa carpeta debe tratarse como un paquete.
'''

import os

#FUNCION TIPO 1:
def datos1():
    nombre=input("ingresa tu nombre")
    tel=input("ingresa tu telefono")
    print(f"nombre: {nombre} y su telefono es {tel}")
    
#FUNCION TIPO 3:
def datos3(nombre,tel):
    nombre=nombre
    tel=tel
    print(f"nombre: {nombre} y su telefono es {tel}")    
 
#FUNCION TIPO 2
def datos2():
    nombre=input(" Nombre ") 
    tel=input(" Telefono ") 
    return nombre,tel
    
#FUNCION TIPO 4
def datos4(nombre,tel):
    nombre=nombre
    tel=tel
    return nombre,tel

def borrarpantalla():
    os.system("cls")
    
def esperetecla():
    input("  ORPIMA CUALQUIER TECLA  ")    
    
def saludos(nombre):
    nom=nombre
    return f"\n Hola, bienvenido {nom}"