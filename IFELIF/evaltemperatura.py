temperatura = float(input("Ingresa la temperatura en °C: "))

if temperatura < 0:
    print("Hace mucho frío")
elif temperatura <= 20:
    print("Clima fresco")
elif temperatura <= 30:
    print("Clima agradable")
else:
    print("Hace mucho calor")