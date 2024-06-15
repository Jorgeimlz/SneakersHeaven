from bson import ObjectId
from database import get_database, log_audit

def create_user(db):
    user_data = {
        "nombre": input("Nombre: "),
        "email": input("Email: "),
        "telefono": input("Teléfono: "),
        "direccion": input("Dirección: ")
    }

    # Regla 8: El nombre del usuario no puede estar vacío
    if not user_data["nombre"]:
        print("Error: El nombre del usuario no puede estar vacío.")
        return

    # Regla 9: El email del usuario debe ser válido (simplificación)
    if "@" not in user_data["email"] or "." not in user_data["email"]:
        print("Error: El email del usuario no es válido.")
        return

    result = db.usuarios.insert_one(user_data)
    log_audit(db, "create", "usuario", f"Usuario {result.inserted_id} creado")
    print("Usuario creado exitosamente.")

def get_users(db):
    print("\nListado de Usuarios:")
    users = db.usuarios.find()
    for user in users:
        print(f"ID: {user['_id']}, Nombre: {user['nombre']}, Email: {user['email']}, Teléfono: {user['telefono']}, Dirección: {user['direccion']}")

def update_user(db):
    user_id = input("Ingrese el ID del usuario a actualizar: ")
    
    # Convertir user_id a ObjectId
    try:
        user_id = ObjectId(user_id)
    except Exception as e:
        print(f"ID de usuario inválido: {e}")
        return
    
    update_data = {
        "nombre": input("Nuevo nombre (dejar en blanco para no cambiar): "),
        "email": input("Nuevo email (dejar en blanco para no cambiar): "),
        "telefono": input("Nuevo teléfono (dejar en blanco para no cambiar): "),
        "direccion": input("Nueva dirección (dejar en blanco para no cambiar): ")
    }

    # Filtrar los campos vacíos
    update_data = {k: v for k, v in update_data.items() if v}
    
    # Regla 10: Verificar que al menos un campo sea actualizado
    if not update_data:
        print("Error: No se proporcionaron datos para actualizar.")
        return

    result = db.usuarios.update_one({'_id': user_id}, {'$set': update_data})
    if result.matched_count == 0:
        print("Usuario no encontrado.")
    else:
        log_audit(db, "update", "usuario", f"Usuario {user_id} actualizado")
        print("Usuario actualizado exitosamente.")

def delete_user(db):
    user_id = input("Ingrese el ID del usuario a eliminar: ")
    db.usuarios.delete_one({'_id': ObjectId(user_id)})
    log_audit(db, "delete", "usuario", f"Usuario {user_id} eliminado")
    print("Usuario eliminado exitosamente.")

def user_menu(db):
    while True:
        print("\n--- Submenú de Usuarios ---")
        print("1. Crear Usuario")
        print("2. Listar Usuarios")
        print("3. Actualizar Usuario")
        print("4. Eliminar Usuario")
        print("5. Regresar al Menú Principal")
        
        choice = input("Ingrese su opción: ")
        
        if choice == '1':
            create_user(db)
        elif choice == '2':
            get_users(db)
        elif choice == '3':
            update_user(db)
        elif choice == '4':
            delete_user(db)
        elif choice == '5':
            break
        else:
            print("Opción no válida. Por favor intente de nuevo.")
