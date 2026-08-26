from math import sqrt
a = float(input("Ingresar el valor de a: "))
b = float(input("Ingresar el valor de b: "))
c = float(input("Ingresar el valor de c: "))
X1 = (-b + sqrt((b**2) - (4*a*c))) / 2*a
print("X1 = %2.2f"%(X1))
X2 = (-b - sqrt((b**2) - (4*a*c))) / 2*a
print("X2 = %2.2f"%(X2))
