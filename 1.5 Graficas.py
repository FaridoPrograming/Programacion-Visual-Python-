import matplotlib.pyplot as mpl
#create data points
x = [1,2,3,4,5]
y = [2,4,6,8,10]
#create plot line
mpl.plot(x,y,color="green",marker="o",linestyle="-")
mpl.title("Voltaje vs Corriente")
mpl.xlabel("Voltaje de la fuente")
mpl.ylabel("Corriente directa del diodo")
mpl.show()
