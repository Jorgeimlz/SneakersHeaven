from database import get_database, log_audit
from bson import ObjectId

def add_supplier(db):
    supplier_data = {
        "nombre": input("Nombre del Proveedor: "),
        "direccion": input("Dirección: "),
        "telefono": input("Teléfono: "),
        "email": input("Email: "),
        "contactoPrincipal": input("Contacto Principal: ")
    }

    # Regla 6: El nombre del proveedor no puede estar vacío
    if not supplier_data["nombre"]:
        print("Error: El nombre del proveedor no puede estar vacío.")
        return

    # Regla 7: El email del proveedor debe ser válido (simplificación)
    if "@" not in supplier_data["email"] or "." not in supplier_data["email"]:
        print("Error: El email del proveedor no es válido.")
        return

    result = db.proveedores.insert_one(supplier_data)
    log_audit(db, "create", "proveedor", f"Proveedor {result.inserted_id} añadido")
    print("Proveedor añadido exitosamente.")

def list_suppliers(db):
    suppliers = db.proveedores.find()
    print("\n--- Listado de Proveedores ---")
    for supplier in suppliers:
        print(f"ID: {supplier['_id']}, Nombre: {supplier['nombre']}, Dirección: {supplier['direccion']}, Teléfono: {supplier['telefono']}, Email: {supplier['email']}, Contacto Principal: {supplier['contactoPrincipal']}")

def supplier_menu(db):
    while True:
        print("\n--- Submenú de Proveedores ---")
        print("1. Añadir Proveedor")
        print("2. Listar Proveedores")
        print("3. Regresar al Menú Principal")
        
        choice = input("Ingrese su opción: ")

        if choice == '1':
            add_supplier(db)
        elif choice == '2':
            list_suppliers(db)
        elif choice == '3':
            break
        else:
            print("Opción no válida. Por favor intente de nuevo.")

def update_supplier(db):
    supplier_id = input("ID del Proveedor a actualizar: ")
    supplier = db.proveedores.find_one({'_id': ObjectId(supplier_id)})

    if not supplier:
        print("Proveedor no encontrado.")
        return

    new_telefono = input(f"Nuevo Teléfono (actual: {supplier['telefono']}): ")
    if new_telefono and new_telefono != supplier['telefono']:
        db.proveedores.update_one({'_id': supplier_id}, {'$set': {'telefono': new_telefono}})
        print("Información del proveedor actualizada exitosamente.")
    else:
        print("No se realizó ninguna actualización.")
