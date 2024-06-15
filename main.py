from database import get_database
from user_operations import user_menu
from product_operations import product_menu
from sales_operations import sales_menu
from supplier_operations import supplier_menu
from audit_operations import list_audits

def main_menu():
    db = get_database()
    while True:
        print("\n--- Sneakers Heaven Management System ---")
        print("1. Gestión de Usuarios")
        print("2. Gestión de Productos")
        print("3. Gestión de Ventas")
        print("4. Gestión de Proveedores")
        print("5. Ver Auditorías")
        print("6. Salir")
        
        choice = input("Ingrese su opción: ")

        if choice == '1':
            user_menu(db)
        elif choice == '2':
            product_menu(db)
        elif choice == '3':
            sales_menu(db)
        elif choice == '4':
            supplier_menu(db)
        elif choice == '5':
            list_audits(db)
        elif choice == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor intente de nuevo.")

if __name__ == '__main__':
    main_menu()
