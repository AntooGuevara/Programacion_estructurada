import agenda 

def main():
    agenda_contacto = {}
    opcion = True
    
    while opcion:
        agenda.borrarpantalla()
        opcion = agenda.menuprincipal()
        match opcion:
            case "1":
                agenda.agregar_contacto(agenda_contacto)
            case "2":
                agenda.mostrar_contactos(agenda_contacto)
            case "3":
                agenda.buscar_contacto(agenda_contacto)
            case "4":
                agenda.modificar_contactos(agenda_contacto)
            case "5":
                agenda.eliminar_contacto(agenda_contacto)
            case "6":
                agenda.borrarpantalla()
                print("SALISTE DEL SOFTWARE")
                
                opcion = False
            case _:
                print("INGRESE UN VALOR CORRECTO")
                agenda.esperartecla()
                

if __name__ == "__main__":
    main()
