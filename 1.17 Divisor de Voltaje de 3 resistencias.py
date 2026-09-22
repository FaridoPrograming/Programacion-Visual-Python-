## Programa para calcular la caída de voltaje
# en un divisor con tres resistencias.

def voltage_divider(Vin, r1, r2, r3):

    # Calcular resistencia total
    r_total = r1 + r2 + r3
    # Voltaje en R1
    v_out1 = Vin * (r1 / r_total)
    # Voltaje en R2
    v_out2 = Vin * (r2 / r_total)
    # Voltaje en R3
    v_out3 = Vin * (r3 / r_total)
    return v_out1, v_out2, v_out3

# -----------------------------------
# Entrada de datos
# -----------------------------------

Vin = float(input("Ingrese el voltaje de la fuente (V): "))
r1 = float(input("Ingrese el valor de R1 (ohm): "))
r2 = float(input("Ingrese el valor de R2 (ohm): "))
r3 = float(input("Ingrese el valor de R3 (ohm): "))

# -----------------------------------
# Cálculo de voltajes
# -----------------------------------

v_out1, v_out2, v_out3 = voltage_divider(Vin, r1, r2, r3)

# -----------------------------------
# Mostrar resultados
# -----------------------------------

print("\n----- RESULTADOS -----")

print(f"Voltaje de entrada: {Vin:.2f} V")

print(f"Resistencia total: {r1 + r2 + r3:.2f} ohm")

print(f"Caída de voltaje en R1: {v_out1:.2f} V")
print(f"Caída de voltaje en R2: {v_out2:.2f} V")
print(f"Caída de voltaje en R3: {v_out3:.2f} V")

# Comprobación
print(f"Suma de voltajes: {v_out1 + v_out2 + v_out3:.2f} V")
