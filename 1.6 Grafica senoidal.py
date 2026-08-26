import matplotlib.pyplot as mpl
import numpy as np
#Datos para plotear
t= np.arange(0.0, 2.0, 0.01)
s= np.sin(2*np.pi * t)
fig, ax = mpl.subplots()
ax.plot(t,s)
mpl.show()
