angulo = float(input("Ingresa el valor del ángulo en grados: "))

if angulo < 0:
    print("Error: El ángulo no puede ser negativo")
elif angulo == 0:
    print("El ángulo es nulo (0°)")
elif angulo < 90:
    print("El ángulo es agudo (<90°)")
elif angulo == 90:
    print("El ángulo es recto (90°)")
elif angulo < 180:
    print("El ángulo es obtuso (>90° y <180°)")
elif angulo == 180:
    print("El ángulo es llano (180°)")
else:
    print("El ángulo es cóncavo (>180°)")