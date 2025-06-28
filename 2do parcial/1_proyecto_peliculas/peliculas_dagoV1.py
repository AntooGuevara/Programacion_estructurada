peliculas=[]

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()  

def agregarPeliculas():
  borrarPantalla()
  print(".:: Alta de Peliculas ::. ")
  pelicula=input("Ingresa el nombre: ".upper().strip())
  peliculas.append(pelicula)
  input("Pelicula agregada exitosamente. " + pelicula + "\n" + "Oprima cualquier tecla para continuar ...")
  
def consultarPeliculas():
  borrarPantalla()
  print(".:: Consultar Peliculas ::.")
  if len(peliculas) > 0:
    print("Lista de Peliculas: ")
    for i in peliculas:
        print(i)
  else:
        print("No hay peliculas registradas.")
        

def vaciarPeliculas():
  borrarPantalla()
  print(".:: Vaciar Peliculas ::.")
  resp=input("¿Estas seguro de vaciar la lista de peliculas? (S/N): ").upper().strip()
  if resp=="S":
    peliculas.clear()
    print("Lista de peliculas vaciada exitosamente.")
  else:
    print("Operación cancelada. La lista de peliculas no se ha modificado.")
    
def buscarPeliculas():
 borrarPantalla()
 print(".:: Buscar Peliculas ::.")
 pelicula_buscar=input("Ingresa el nombre de la pelicula a buscar: ".upper().strip())
 encontro=0
 if not (pelicula_buscar in peliculas):
   print("La pelicula " + pelicula_buscar + " no se encuentra en la lista.")
 else:
   for i in range(0, len(peliculas)):
     if pelicula_buscar==peliculas[i]:
        
       print((f"La pelicula " + pelicula_buscar + " se encuentra en la lista y esta en la casilla:  {i}"))
       encontro+=1
       if encontro>0:
          print(f"La pelicula {pelicula_buscar} se encuentra {encontro} veces en la lista.")
          input("Oprima cualquier tecla para continuar ...")
          
      
      
def borrarPeliculas():
  borrarPantalla()
  print(".:: Eliminar Peliculas ::.")
  pelicula_eliminar=input("Ingresa el nombre de la pelicula a eliminar: ".upper().strip())
  encontro=0
  if not (pelicula_eliminar in peliculas):
    print("La pelicula " + pelicula_eliminar + " no se encuentra en la lista.")
  else: resp="si"
  
  while pelicula_eliminar in peliculas and resp=="si":
    encontro+=1
    borrarPantalla()
    print(".:: Eliminar Peliculas ::.")
    print("Lista de Peliculas: ")
    for i in range(0, len(peliculas)):
        print(f"{i+1}. {peliculas[i]}")
    
    pelicula_eliminar=input("Ingresa el nombre de la pelicula a eliminar: ".upper().strip())
    resp=input("¿Estas seguro de eliminar la pelicula? (si/no): ".upper().strip())
  
  #ESTE ES OTRO
  for i in range(0,len(peliculas)):
    if pelicula_eliminar == peliculas[i]:
      peliculas.remove(pelicula_eliminar)
      print(f"Pelicula eliminada exitosamente: " , pelicula_eliminar , " y se encontraba en la casilla:" ,   (i+1))  
    else:
      print("La pelicula " + pelicula_eliminar + " no se encuentra en la lista.")
      
      if encontro>0:
        print(f"la pelicula se encontro {encontro} veces en la lista")
        encontro+=1
      
      
        
#Caracteristicas de las peliculas

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t .:: Agregar Caracteristica a Peliculas ::.\n")
    atributo=input("Ingresa la nueva caracteristica de la Pelicula: ").lower().strip()
    valor=input("Ingresa el valor de la caracteristica de la pelicula: ").upper().strip()
    peliculas.update({atributo:valor})

def modificarCaracteristicasPeliculas():
    borrarPantalla()
    print("\n\t .::Modificar caracteristica a peliculas::.\n")
    atributo = input("\n¿Qué atributo deseas modificar? (nombre, categoria, clasificacion, genero, idioma): ").lower().strip()
    if atributo in peliculas:
        nuevo_valor = input(f"Ingrese el nuevo valor para '{atributo}': ").upper().strip()
        peliculas[atributo] = nuevo_valor
        print(f"\n\tEl valor se ha actualizado '{atributo}' a: {nuevo_valor}")
    else:
        print("\n\tEl atributo ingresado no es válido.")

def borrarCaracteristicas():
    borrarPantalla()
    print("\n\t .::Modificar caracteristica a peliculas::.\n")
    atributo = input("Ingresa la caracteristica que deseas modificar: ").lower().strip()
    if atributo in peliculas:
        nuevo_valor = input("Ingresa el nuevo valor de la caracteristica: ").upper().strip()
        peliculas.update({atributo: nuevo_valor})
        print("\n\t ..::: Caracteristica modificada con exito! :::..")
    else:
        print("\n\t La caracteristica no existe.")
    input("\n\t Oprima cualquier tecla para continuar...")

   
def eliminarPeliculas():
   borrarPantalla()
   print("\n\t.:: Borrar Películas ::.\n")
   pelicula_buscar=input("Ingrese el nombre de la pelicula que desea buscar: ").upper().strip()
   encontro=0
   if not(pelicula_buscar in peliculas): 
      print("\n\t\t ¡No se encuentra la pelicula a buscar!")   
   else: 
      resp="si"  
      while pelicula_buscar in peliculas and resp=="si":
          resp=input("¿Deseas quitar o borrar la pelicula del sistema (Si/No)?").lower()
          if resp=="si":
            posicion=peliculas.index(pelicula_buscar)
            print(f"\nLa pelicula que se borro es: {pelicula_buscar} y estaba en la casilla: {posicion+1}")
            peliculas.remove(pelicula_buscar) 
            encontro+=1
            print("\n\t\t::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
      print(f"Se borro {encontro} pelicula(s) con este titulo")             
                

        
    
      
 
 
  