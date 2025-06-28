#forma 1
import modulos

modulos.borrarpantalla()
print(modulos.saludos("Antonio"))

#forma 2
from modulos import *

#borrarpantalla()
print(saludos("Emir Velazquez"))

nombre=input("Ingresa tu nombre")
telefono=input("Ingresa tu número de teléfono")
nom,tel=datos4(nombre,telefono)

print(f"\tNombre completo: {nom}\n\tTeléfono{tel}")    