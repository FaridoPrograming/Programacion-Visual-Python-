#Funciones que realizan algunos componentes electronicos
while True:
    comp=str(input("Ingresa el componente que deseas conocer: ").lower())
#El ".lower" lee el string tanto en mayuscula como en minuscula
    match comp:
        case "transistor":
            print ("amplifica")
        case "diodo":
            print ("ractifica")
        case "capacitor":
            print ("almacena energia en campos electricos")
        case "inductor":
            print ("almacena energia en campos magneticos")
        case "resistencia":
            print ("limita el paso de corriente")
        case "diodo zener":
            print ("regulador de voltaje")
        case "salir":
            print ("Saliendo del programa")
            break
