"""""
Crear un programa que calcule e imprima cualquier tabla de multiplicar
   Requisitos:
    Con funcion que regrese valor y utilice parametros.
"""


def tablamult(num):
    num=numero
    respuesta=""
    for i in range (1,11):
        multi=num*i
        print(f"{num} x {i} = {multi}")
    return respuesta    

numero=input("dame un valor para calcular una tabla de multiplicar ")
print(f"Tabla de multiplicar del {numero}")
resultado=tablamult(numero)
print(f"{resultado}")  


