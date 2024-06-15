from bson import ObjectId
from datetime import datetime
from database import get_database, log_audit

def is_valid_objectid(oid):
    try:
        ObjectId(oid)
        return True
    except Exception:
        return False

def record_sale(db):
    empleado_id = input("ID del Empleado: ")
    if not is_valid_objectid(empleado_id):
        print("Error: El ID del Empleado no es válido.")
        return

    usuario_id = input("ID del Usuario: ")
    if not is_valid_objectid(usuario_id):
        print("Error: El ID del Usuario no es válido.")
        return

    # Verificar que el empleado exista
    empleado = db.empleados.find_one({'_id': ObjectId(empleado_id)})
    if not empleado:
        print("Error: El empleado no existe.")
        return

    # Verificar que el usuario exista
    usuario = db.usuarios.find_one({'_id': ObjectId(usuario_id)})
    if not usuario:
        print("Error: El usuario no existe.")
        return

    fecha_venta = datetime.strptime(input("Fecha de Venta (YYYY-MM-DD): "), "%Y-%m-%d")
    flete = float(input("Flete: "))
    pais_envio = input("País de Envío: ")
    ciudad_envio = input("Ciudad de Envío: ")
    direccion_envio = input("Dirección de Envío: ")
    detalles = []

    while True:
        producto_id = input("ID del Producto (deja vacío para terminar): ")
        if not producto_id:
            break
        if not is_valid_objectid(producto_id):
            print("Error: El ID del Producto no es válido.")
            continue

        producto_id = ObjectId(producto_id)
        precio_unitario = float(input("Precio Unitario: "))
        cantidad = int(input("Cantidad: "))
        descuento = float(input("Descuento: "))
        subtotal = precio_unitario * cantidad - descuento
        total = subtotal + flete
        detalles.append({
            "productoId": producto_id,
            "precioUnitario": precio_unitario,
            "cantidad": cantidad,
            "descuento": descuento,
            "subtotal": subtotal,
            "total": total
        })

    sale_data = {
        "empleadoId": ObjectId(empleado_id),
        "usuarioId": ObjectId(usuario_id),
        "fechaVenta": fecha_venta,
        "flete": flete,
        "paisEnvio": pais_envio,
        "ciudadEnvio": ciudad_envio,
        "direccionEnvio": direccion_envio,
        "detalles": detalles
    }
    
    result = db.ventas.insert_one(sale_data)
    log_audit(db, "create", "venta", f"Venta {result.inserted_id} registrada")
    print("Venta registrada exitosamente.")

def list_sales(db):
    sales = db.ventas.find()
    print("\n--- Listado de Ventas ---")
    for sale in sales:
        print(f"ID: {sale['_id']}")
        print(f"Empleado ID: {sale['empleadoId']}")
        print(f"Usuario ID: {sale['usuarioId']}")
        print(f"Fecha de Venta: {sale['fechaVenta']}")
        print(f"Flete: {sale['flete']}")
        print(f"País de Envío: {sale['paisEnvio']}")
        print(f"Ciudad de Envío: {sale['ciudadEnvio']}")
        print(f"Dirección de Envío: {sale['direccionEnvio']}")
        print("Detalles:")
        for detalle in sale['detalles']:
            print(f"  Producto ID: {detalle['productoId']}")
            print(f"  Precio Unitario: {detalle['precioUnitario']}")
            print(f"  Cantidad: {detalle['cantidad']}")
            print(f"  Descuento: {detalle['descuento']}")
            print(f"  Subtotal: {detalle['subtotal']}")
            print(f"  Total: {detalle['total']}")
        print("-" * 30)

def sales_menu(db):
    while True:
        print("\n--- Submenú de Ventas ---")
        print("1. Registrar Venta")
        print("2. Listar Ventas")
        print("3. Regresar al Menú Principal")
        
        choice = input("Ingrese su opción: ")

        if choice == '1':
            record_sale(db)
        elif choice == '2':
            list_sales(db)
        elif choice == '3':
            break
        else:
            print("Opción no válida. Por favor intente de nuevo.")
