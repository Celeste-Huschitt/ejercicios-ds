def calcularPrecioFinal(precioBase, porcentajeDescuento=10, esVip=False):
    if precioBase < 0 or porcentajeDescuento < 0:
        raise ValueError("El precio base y/o porcentaje de descuento no pueden ser negativos")

    descuento = precioBase * (porcentajeDescuento/100)
    precio = precioBase - descuento

    if esVip:
        descuentoVip = precio * 0.05
        precio -= descuentoVip

    return precio


p1 = calcularPrecioFinal(1000)
print(f"Precio final: ${p1:.2f}")  

p2 = calcularPrecioFinal(1000, porcentajeDescuento=15)
print(f"Precio final: ${p2:.2f}")

p3 = calcularPrecioFinal(1000, esVip=True)
print(f"Precio final: ${p3:.2f}") 

p4 = calcularPrecioFinal(1000, 20, True)
print(f"Precio final: ${p4:.2f}")  

try:
    calcularPrecioFinal(-500)
except ValueError as e:
    print(f"Error: {e}")