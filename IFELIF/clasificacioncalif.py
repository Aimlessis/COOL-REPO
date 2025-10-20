calificacion = float(input("Ingresa la calificación (0-100): "))

if calificacion >= 90:
    letra = "A"
elif calificacion >= 80:
    letra = "B"
elif calificacion >= 70:
    letra = "C"
elif calificacion >= 60:
    letra = "D"
else:
    letra = "F"

print(f"Calificación: {letra}")