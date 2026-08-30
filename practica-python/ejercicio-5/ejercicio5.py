MAX_INTENTOS = 3
CONTRASENIA = "DdSTW2026"
def crearContrasenia():
    mayuscula = minuscula = longitud = False

    contrasenia = input("Ingrese una contraseña que cumpla con lo siguiente: \n1. Tenga por lo menos una letra mayuscula." \
        "\n2. Tenga por lo menos una letra minuscula.\n3. Tenga al menos 8 caracteres. \nContrasenia: ")

    for c in contrasenia:
        if c.islower():
            minuscula = True
        if c.isupper():
            mayuscula = True

    longitud = len(contrasenia) >= 8

    if mayuscula and minuscula and longitud:
        print("La contraseña ha sido guardada correctamente")
    if not mayuscula:
        print("No tiene letras mayusculas")
    if not minuscula:
        print("No tiene letras minusculas")
    if not longitud:
        print("Tiene menos de 8 caracteres")



crearContrasenia()
print("Inicio de sesion")

cont = 0
correcta = False
while cont < MAX_INTENTOS and not correcta:
    clave = input("Ingrese su contrasenia: ")
    if clave == CONTRASENIA:
        correcta = True
        print("Contrasenia correcta. Bienvenido")
    else:
        cont += 1

if cont == MAX_INTENTOS:
    print("Ha excedido el limite de intentos. Intentelo mas tarde")


