while True:
    sen1 = float(input("Temperatura 1: "))
    sen2 = float(input("Temperatura 2: "))
    if (sen1>25 or sen2>25):
        print ("su temperatura es mayor a la establecida")
    else:
        print ("La temperatura esta normal")
