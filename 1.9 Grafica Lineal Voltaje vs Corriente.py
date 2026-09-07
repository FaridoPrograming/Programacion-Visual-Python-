#Demostrar que la corriente y el voltaje tienen un comportamiento lineal
#Datos: V-I con una R= 10 Ohms
import matplotlib.pyplot as mpl
V = 10,20,30,40,50,60,70,80,90,100
I = 1,2,3,4,5,6,7,8,9,10
mpl.plot(V,I,color="green",marker="o",linestyle="-")
mpl.title("Comportamiento Voltaje contra Corriente")
mpl.xlabel("Voltaje")
mpl.ylabel("Corriente")
mpl.show()
