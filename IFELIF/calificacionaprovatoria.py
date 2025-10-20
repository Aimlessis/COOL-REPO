calificacion = float(input("ingrese la calificacion"))

if calificacion >= 60 and calificacion < 100:
    print("aprovaste")
elif calificacion < 60 and calificacion > 0:
    print("reprovado")