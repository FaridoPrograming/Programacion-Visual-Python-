def fibonacci_ascendente(n):
    a, b = 0, 1
    contador = 0
    while contador < n:
        print(a)
        a, b = b, a + b
        contador += 1

# Ejemplo: Imprimir los primeros 10 números
fibonacci_ascendente(15)
