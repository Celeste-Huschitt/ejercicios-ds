def sumaNumeros():
    n = int(input("Ingrese la cantidad de numero naturales a sumar: "))

    suma = 0
    for i in range(1, n + 1):
        suma += i

    print(f"Resultado de la suma: {suma}")
    
def divisores3():
    valido = False
    while not valido:
        min = int(input("Ingrese el limite inferior del rango: "))
        max = int(input("Ingrese el limite superior del rango: "))

        if min <= max:
            valido = True
        else:
            print("El tope minimo es mayor al maximo")

    for n in range(min, max + 1):
        if n%3 == 0:
            print(n)
         

opcion = 'a'
while opcion != 'c':
    print("Menu principal \na. Suma de los primeros numeros naturales. \n" \
            "b. Mostrar los divisores de 3 en un rango dado. \n" \
            "c. Salir.")
    opcion = input("Ingrese una opcion: ")

    match opcion:
        case 'a': 
            sumaNumeros()
        case 'b':
            divisores3()
        case 'c':
            break
        case _:
            print("Opcion invalida")
