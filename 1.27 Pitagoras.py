from math import sqrt
def Pitagora(a,b):
    c=sqrt(a**2+b**2)
    return c
a,b=map(int,input("Ingresar catetos").split(","))
c=Pitagora(a,b)
print (c)
