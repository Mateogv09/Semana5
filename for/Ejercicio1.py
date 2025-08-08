# SISTEMA DE INVENTARIO NEONIX
valor_total = 0
ahorro_total = 0

print("===== NEONIX =====\n")

# CUANTOS PRODUCTOS QUIERES INGRESAR?
cantidad_productos = int(input("¿Cuantos productos desea registrar? "))

for i in range(cantidad_productos):
    print(f"\n--- Producto {i+1} ---")
    
    # PREGUNTAMOS LOS DATOS DEL PRODUCTO
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría (Camisetas, Pantalones, Zapatos, etc.): ")
    precio = float(input("Precio unitario: $"))
    stock = int(input("Cantidad en stock: "))
    
    # SI ES UNA CAMISA APLICAMOS EL 10% DE DESCUENTO
    descuento = 0
    if categoria.lower() == "camisetas":
        descuento = 0.10
        precio_descuento = precio - (precio * descuento)
    else:
        precio_descuento = precio

    # CALCULAMOS VALOR DE INVENTARIO
    valor_producto = precio_descuento * stock
    valor_total += valor_producto
    ahorro_total += (precio - precio_descuento) * stock

    # SE REVISA SI HAY POCO EN STOCK
    advertencia = " Reabastecer" if stock < 20 else " Stock suficiente"

    # REPORTE
    print("\n== REPORTE PARCIAL ==")
    print(f"Producto: {nombre}")
    print(f"Categoría: {categoria}")
    print(f"Precio unitario: ${precio}")
    if descuento > 0:
        print(f" Precio con descuento: ${precio_descuento:.2f}")
    print(f"Stock disponible: {stock} ({advertencia})")
    print(f"Valor en inventario: ${valor_producto:.2f}")
    print("=========================")

# DAMOS EL VALOR FINAL
print("\n===== REPORTE FINAL =====")
print(f" Valor total del inventario: ${valor_total:.2f}")
print(f" Ahorro total por descuentos aplicados: ${ahorro_total:.2f}")
print("=================================")