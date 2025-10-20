num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

positivos = 0
negativos = 0
ceros = 0

for num in [num1, num2, num3]:
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        ceros += 1

if ceros > 0:
    print("Hay ceros entre los números")
elif positivos == 3:
    print("Todos los números son positivos")
elif negativos == 3:
    print("Todos los números son negativos")
else:
    print("Los números son mixtos (positivos y negativos)")