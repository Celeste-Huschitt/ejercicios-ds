def aCelsius(temperatura):
    return (temperatura - 32) / 1.8

def aFahrenheit(temperatura):
    return (temperatura*1.8) + 32

valido = sisValido = False

while not valido or not sisValido:
    try:
        temp = float(input("Ingrese una temperatura: "))
        valido = True
    except ValueError:
        print("No ingreso un numero valido")
        continue

    sistema = input("Ingrese el sistema de medicion original: ")
    sistema = sistema.lower()

    if sistema == "celsius" or sistema == "fahrenheit":
        sisValido = True
    else:
        print("No ingreso un sistema valido")
        continue

if sistema == "celsius":
    print(f"La temperatura {temp} °C es equivalente a {aFahrenheit(temp)}°F\n")
else:
    print(f"La temperatura {temp} °F es equivalente a {aCelsius(temp)}°C\n")
