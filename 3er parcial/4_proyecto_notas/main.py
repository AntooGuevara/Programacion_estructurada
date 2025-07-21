import funciones 
import conexionBD

def main():
    opcion=True
    while opcion:
        funciones.borrarpantalla()
        opcion=funciones.menu_principal()
        
        if opcion=="1" or opcion=="REGISTRO":
            print("Estoy en la opcion 1")
        elif opcion=="2" or opcion=="LOGIN":
            print("Estoy en la opcion 3")
        elif opcion=="3" or opcion=="SALIR":
            print("SALIR DEL SISTEMA")
            funciones.esperartecla()
            opcion=False
        else:
            print("INGRESA UN VALOR VÁLIDO")
            opcion=True
            funciones.esperartecla()
            
        
    
        
if __name__=="__main__":
        main()
    


