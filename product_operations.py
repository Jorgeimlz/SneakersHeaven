from database import get_database, log_audit
from bson import ObjectId

def add_product(db):
    product_data = {
        "nombre": input("Nombre del Producto: "),
        "descripcion": input("Descripción: "),
        "precio": float(input("Precio: ")),
        "stock": int(input("Stock inicial: "))
    }

    # Regla 1: El precio del producto debe ser mayor que cero
    if product_data["precio"] <= 0:
        print("Error: El precio del producto debe ser mayor que cero.")
        return

    # Regla 2: El stock inicial no puede ser negativo
    if product_data["stock"] < 0:
        print("Error: El stock inicial no puede ser negativo.")
        return

    result = db.productos.insert_one(product_data)
    log_audit(db, "create", "producto", f"Producto {result.inserted_id} añadido")
    print("Producto añadido exitosamente.")

def update_product_stock(db):
    product_id = input("ID del Producto: ")
    new_stock = int(input("Nuevo stock: "))

    # Regla 3: El nuevo stock no puede ser negativo
    if new_stock < 0:
        print("Error: El nuevo stock no puede ser negativo.")
        return

    db.productos.update_one({'_id': ObjectId(product_id)}, {'$set': {'stock': new_stock}})
    log_audit(db, "update", "producto", f"Stock del producto {product_id} actualizado a {new_stock}")
    print("Stock del producto actualizado exitosamente.")

def list_products(db):
    products = db.productos.find()
    print("\n--- Listado de Productos ---")
    for product in products:
        print(f"ID: {product['_id']}, Nombre: {product['nombre']}, Descripción: {product['descripcion']}, Precio: {product['precio']}, Stock: {product['stock']}")

def product_menu(db):
    while True:
        print("\n--- Submenú de Productos ---")
        print("1. Añadir Producto")
        print("2. Listar Productos")
        print("3. Regresar al Menú Principal")
        
        choice = input("Ingrese su opción: ")

        if choice == '1':
            add_product(db)
        elif choice == '2':
            list_products(db)
        elif choice == '3':
            break
        else:
            print("Opción no válida. Por favor intente de nuevo.")



