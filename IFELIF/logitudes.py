a = float(input("Ingresa la primera longitud: "))
b = float(input("Ingresa la segunda longitud: "))
c = float(input("Ingresa la tercera longitud: "))

if a + b > c and a + c > b and b + c > a:
    print("Sí pueden formar un triángulo")
else:
    print("No pueden formar un triángulo")