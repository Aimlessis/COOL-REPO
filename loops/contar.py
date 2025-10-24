num = int(input("Ingresa un número entero positivo: "))
contador = 0
while num > 0:
    contador += 1
    num //= 10
print("El número tiene", contador, "dígitos")