"""
Sistema de ecuaciones a resolver
4_I1 + 3_I2 = 2
3_I1 + 5_I2 = 6
"""
import numpy as np

# Matriz de coeficientes (A) con las resistencias/términos de las corrientes
A = np.array([
    [4, 3],
    [3, 5]])

# Vector de términos independientes (B) con los voltajes
B = np.array([2, 6])

# Resolver el sistema de ecuaciones AX = B
I = np.linalg.solve(A, B)

print(f"Corriente I1: {I[0]:.4f} A")
print(f"Corriente I2: {I[1]:.4f} A")
print(f"Corriente I3: {I[1] + I[0]:.4f} A")
