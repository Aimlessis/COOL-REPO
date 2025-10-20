precio = float(input("Ingresa el precio del producto: $"))

if precio < 50:
    descuento = 0
elif precio <= 100:
    descuento = precio * 0.05
else:
    descuento = precio * 0.10

precio_final = precio - descuento
print(f"Precio final: ${precio_final:.2f}")