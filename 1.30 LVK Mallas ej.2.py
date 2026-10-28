"""
Sistema de ecuaciones a resolver
600_I1 - 270_I2 - 330_I3 = 12
-270_I1 + 10600_I2 - 10000_I3 = 0
-330_I1 - 10000_I2 + 11150_I3 = 0
"""
import numpy as np

# Matriz de coeficientes (A) con las resistencias/términos de las corrientes
A = np.array([
    [600, -270, -330],
    [-270, 10600, -10000],
    [-330, -10000, 11150]])

# Vector de términos independientes (B) con los voltajes
B = np.array([12, 0, 0])

# Resolver el sistema de ecuaciones AX = B
I = np.linalg.solve(A, B)
print(A)
print(f"Corriente I1: {I[0]:.4f} A")
print(f"Corriente I2: {I[1]:.4f} A")
print(f"Corriente I3: {I[2]:.4f} A")
print(f"Corriente Total: {I[0] + I[1] + I[2]:.4f} A")

print ("Checando\n", np.dot(A, I))
