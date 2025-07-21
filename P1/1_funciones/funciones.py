""""
una fincion es un conjunto de insturcciones agrupadas bajo un nombre en particular como un programa más pequeño
que cumple una funcion especifica. La funcion se puede reutilizar con el simple hecho de invocarla, es decir,
mandarla a llamar. 

Sintaxis: 
    Def nombredeMifuncion(parametros)
        bloque o conjunto de instrucciones
    
    nombredeMifuncion(parametros)
    
Las funciones pueden ser de 4 tipos:
   Funciones de tipo "Procedimiento"
    1- Funcion que no recibe parametros y no sergresa valor.
    3- Funcion que recibe parametros y no regresa valor.
   Funciones de tipo "Función"
    2- Funcion que recibe parametros y no regresa valor.
    4- Funcion que recibe parametros y regresa valor. 
"""
#FUNCION TIPO 1:
def datos1():
    print("FUNCION1")
    nombre=input("ingresa tu nombre")
    tel=input("ingresa tu telefono")
    print(f"nombre: {nombre} y su telefono es {tel}")
    
#FUNCION TIPO 3:
def datos3(nombre,tel):
    print("FUNCION3")    
    nombre=nombre
    tel=tel
    print(f"nombre: {nombre} y su telefono es {tel}")    
 
#FUNCION TIPO 2
def datos2():
    print("FUNCION2")
    nombre=input("Nombre") 
    tel=input("Telefono") 
    return nombre,tel
    
#FUNCION TIPO 4
def datos4():
    print("FUNCION4")
    nombre=nombre
    tel=tel
    return nombre,tel

#LLAMAR FUNCIONES
datos1   

nombre3=input("Ingresa tu nombre ")
tel3=input("Ingresa tu telefono ")
datos3(nombre3,tel3)

nombre2,tel2=datos2()
print(f"Nombre: {nombre2} \n Telefono: {tel2}")

nombre4=input("Nombre")
tel4=input("Telefono")
nombre4,tel4=datos4(nombre4,tel4)
print(f"Nombre: {nombre4} \n Telefono:{tel4}")
