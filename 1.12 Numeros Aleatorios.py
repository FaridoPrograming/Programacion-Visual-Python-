#Programa que genera numeros aleatorios
while True:
    from random import randint
    no = randint(1,10)
    guess=int(input("Adivina el numero: "))
    if guess == no:
        print ("Lo lograste!!!")
    else:
        print("SJSJSJSJ perdedor, el numero es: ",no)
#Importa separar las lineas del codigo de manera correcta para que while encierre los bloques que ocupara
