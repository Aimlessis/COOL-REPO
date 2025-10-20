a = float(input("Ingresa el primer lado: "))
b = float(input("Ingresa el segundo lado: "))
c = float(input("Ingresa el tercer lado: "))

if a == b == c:
    print("Triángulo equilátero")
elif a == b and a != c or a == c and a != b or b == c and a != b:
    print("Triángulo isósceles")
else:
    print("Triángulo escaleno")