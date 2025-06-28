""""
Dict:
    Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en un lugar de tener
    como las listas, indices numéricos tiene alfanuméricos. Es decir, es algo parecido como los objetos.
    
    Tambien se conoce como un arreglo asosiativo u objeto JSON
    
    El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""

import os
os.system("cls")
# EJEMPLO 1
#Lista de paises
paises=["Mexico", "Brasil", "Canada", "España"]
#Dict u objeto JSON
pais_mexico={"Nombre":"Mexico", 
        "Capital":"CDMX",
        "Poblacion":126000000,
        "Idioma":"Español",
        "status":True}

pais_brasil={"Nombre":"Brasil", 
        "Capital":"Brasilia",
        "Poblacion":213000000,
        "Idioma":"Portugues",
        "status":True}

pais_canada={"Nombre":"Canada", 
        "Capital":"Ottawa",
        "Poblacion":38000000,
        "Idioma":["frances" , "ingles"],
        "status":False  }

alumno1={"Nombre":"Juan",
         "apellid_paterno":"Garcia",
         "apellid_materno":"Lopez",
         "carrera":"TI",
         "area":"Software multiplataforma",
         "matricula":"123456",
         "modalidad":"bilingue",
         "semestre":"2",       
         }

print(alumno1)

for i in alumno1:
    print(i)
os.system("cls")
    
for i in alumno1:
    print(i, ":", alumno1[i])

for i in alumno1:
    print(f" {i} = {alumno1[i]}")

alumno1["telefono"]="618234549"

for i in alumno1:
    print(f" {i} = {alumno1[i]}")   


