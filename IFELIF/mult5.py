num = int(input("Ingrese numero para ver si es multiplo de 5: \n"))

if num == 0:
    print("es cero")
if num % 5 == 0:
    print("es multiplo")
else:
    print("no es multiplo")