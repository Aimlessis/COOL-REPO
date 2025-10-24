contraseña_correcta = "secreta"
while True:
    contraseña = input("Ingresa la contraseña: ")
    if contraseña == contraseña_correcta:
        break
print("Contraseña correcta!")