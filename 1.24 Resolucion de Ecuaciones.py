def ResEc(a,b,c,d,e,f):
    #ax + by= e
    #cx + dy= f
    x = (d*e - b*f)/(a*d - b*c)
    y = (a*f - c*e)/(a*d - b*c)
    return(x,y)
a,b,c,d,e,f = map(int,input("Ingresa todos los coeficientes separados por una coma: ").split(","))
xsol, ysol = ResEc(a,b,c,d,e,f)
print("La solucion es x = ", xsol, "y = ", ysol)
