import numpy as np
import matplotlib.pyplot as plt

# Constants
q = 1.6e-19  # Carga de un electrón (C)
k = 1.38e-23  # constante de Boltzmann (J/K)
T = 300  # Temperatura en grados Kelvin
n = 1  # Factor de idealidad
Is = 1e-12  # Corriente de saturacion inversa (A)

# rango de voltaje para polarizacion directa
voltages = np.linspace(0, 1, 100)  # Voltage from 0V to 1 V

# Diode current calculation using Shockley equation
def diode_current(V):
    return Is * (np.exp((q * V) / (n * k * T)) - 1)

# Calculate currents
currents = diode_current(voltages)

# Plotting the VI characteristics
plt.figure(figsize=(8, 6))
plt.plot(voltages, currents, label="Diode IV Curve", color="blue")
# plt.yscale("log")  # Log scale for current (optional for better visualization)
plt.title("VI Characteristics of a Diode (Forward Bias)")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()
plt.show()
