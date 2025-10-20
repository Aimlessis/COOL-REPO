peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print(f"IMC: {imc:.1f} - {categoria}")