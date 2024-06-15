def list_audits(db):
    while True:
        print("\n--- Listado de Auditorías ---")
        audits = db.auditorias.find().sort('timestamp', -1)  # Ordenar por timestamp descendente
        for audit in audits:
            timestamp = audit.get('timestamp', 'No especificado')
            action = audit.get('action', 'No especificado')
            entity = audit.get('entity', 'No especificado')
            details = audit.get('details', 'No especificado')
            print(f"Fecha/Hora: {timestamp}, Acción: {action}, Entidad: {entity}, Detalles: {details}")

        print("\n--- Opciones ---")
        print("1. Eliminar todas las auditorías")
        print("2. Regresar al Menú Principal")
        
        choice = input("Ingrese su opción: ")

        if choice == '1':
            delete_all_audits(db)
        elif choice == '2':
            break
        else:
            print("Opción no válida. Por favor intente de nuevo.")

def delete_all_audits(db):
    result = db.auditorias.delete_many({})
    print(f"Todas las auditorías han sido eliminadas. Total eliminadas: {result.deleted_count}")
