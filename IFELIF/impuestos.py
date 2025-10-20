salario = float(input("Ingresa tu salario mensual: $"))

if salario < 10000:
    impuesto = 0
    porcentaje = 0
elif salario <= 30000:
    impuesto = salario * 0.10
    porcentaje = 10
else:
    impuesto = salario * 0.20
    porcentaje = 20

salario_neto = salario - impuesto

print(f"\n--- RESULTADOS ---")
print(f"Salario bruto: ${salario:,.2f}")
print(f"Tasa de impuesto: {porcentaje}%")
print(f"Impuesto a pagar: ${impuesto:,.2f}")
print(f"Salario neto: ${salario_neto:,.2f}")