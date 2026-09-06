def analizarTemperaturas(registros):
    tempMax = max(registros)
    tempMin = min(registros)
    tempProm = sum(registros) / len(registros)
    return tempMax, tempMin, tempProm

temperaturas = [18.5, 22.0, 5.8, 10.2]

max, min, promedio = analizarTemperaturas(temperaturas)

print(f"Temperaturas: {temperaturas}")
print(f"Temperatura mas alta: {max}")
print(f"Temperatura mas baja: {min}")
print(f"Temperatura promedio: {promedio}")