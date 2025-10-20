diasemana = {
    1: "Domingo",
    2: "Lunes",
    3: "Martes",
    4: "Miercoles",
    5: "Jueves",
    6: "Viernes",
    7: "Sabado"
}

seleccion = int(input("ingrese un numero del 1 al 7 para seleccionar el dia de la semana: \n"))

if seleccion > max(diasemana) or seleccion < min(diasemana):
    print("valor invalido")
    exit()

print(diasemana[seleccion])