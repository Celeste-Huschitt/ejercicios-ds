
print("Calculadora de viaje")

try:
    costoPasaje = float(input("Ingrese el costo del pasaje: "))
    costoAlojamiento = float(input("Ingrese el costo del alojamiento por noche: "))
    cantidadNoches = int(input("Ingrese la cantidad de noches del viaje: "))
    dineroDisponible = float(input("Ingrese el dinero disponible: "))

    costoViaje = (costoAlojamiento * cantidadNoches) + costoPasaje

    if costoViaje <= dineroDisponible:
        print(f"Tienes dinero suficiente. Costo del viaje: {costoViaje}")
    else:
        print(f"No tienes dinero suficiente para pagar el viaje. \nDinero disponible: {dineroDisponible} \nCosto del viaje: {costoViaje}")

except ValueError:
    print("No ingreso un numero valido")



