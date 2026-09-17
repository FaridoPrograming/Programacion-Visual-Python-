colores_valores = {
        "negro":0, "cafe":1,"rojo":2,"naranja":3,"amarillo":4,
        "verde":5,"azul":6,"violeta":7,"gris":8,"blanco":9
        }
colores_multiplicadores = {
        "negro":1, "cafe":10,"rojo":100,"naranja":1000,"amarillo":10000,
        "verde":100000,"azul":1000000,"violeta":10000000,"dorado":0.1,"plateado":0.01
        }
colores_tolerancia = {
        "cafe":1%, "rojo":2%,"dorado":5%,"plateado":10%,"sin banda":20%
        }
def calcular_resistencia():
    print("Calculadora de resistencias de 4 bandas")
b1=input("Color de la banda 1: ").lower()
b2=input("Color de la banda 2: ").lower()
mult=input("Color de la banda 3 (multiplicador): ").lower()
tol=input("Color de la banda 4 (tolerancia): ").lower()
if b1 in colores_valores and b2 in colores_valores and mult in colores_multiplicadores and tol in colores_tolerancia
else:
    print("Error: Uno de los colores ingresados no es reconocido. Intenta de nuevo")
