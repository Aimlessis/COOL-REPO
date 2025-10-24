n = int(input("Ingresa un número entero positivo: "))
factorial = 1
while n > 0:
    factorial *= n
    n -= 1
print("El factorial es:", factorial)