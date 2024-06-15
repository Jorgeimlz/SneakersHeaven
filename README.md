# Sneakers Heaven Management System

## Descripción
Este sistema de gestión de Sneakers Heaven permite administrar usuarios, productos, ventas y proveedores. 

## Requisitos

Para ejecutar este programa, necesitarás instalar los siguientes requisitos:

1. **Python 3.6+**: Asegúrate de tener Python instalado. Puedes descargarlo desde [Python.org](https://www.python.org/downloads/).

2. **Pip**: El gestor de paquetes de Python, normalmente incluido con Python. Para verificar, ejecuta:
    ```bash
    pip --version
    ```

3. **Instalación de dependencias**: Instala las dependencias necesarias con el siguiente comando:
    ```bash
    pip install pymongo
    ```

## Configuración

1. **Clonar el repositorio**:
    ```bash
    git clone https://github.com/tu-usuario/sneakers-heaven.git
    cd sneakers-heaven
    ```

2. **Configuración de la base de datos**:
    - Asegúrate de tener una instancia de MongoDB en funcionamiento.

## Reglas de Negocio

### Generales
1. **ID de MongoDB debe ser válido**:
    - Todos los ID utilizados (`empleadoId`, `usuarioId`, `productoId`, etc.) deben ser válidos `ObjectId` de MongoDB.
    - Un `ObjectId` válido debe tener 24 caracteres hexadecimales.

### Gestión de Usuarios
2. **Nombre del usuario no puede estar vacío**:
    - Al crear un usuario, el campo `nombre` no puede estar vacío.
3. **Email del usuario debe ser válido**:
    - Al crear un usuario, el campo `email` debe tener un formato válido.

### Gestión de Proveedores
4. **Nombre del proveedor no puede estar vacío**:
    - Al añadir un proveedor, el campo `nombre` no puede estar vacío.
5. **Email del proveedor debe ser válido**:
    - Al añadir un proveedor, el campo `email` debe tener un formato válido.

### Gestión de Productos
6. **Precio del producto debe ser mayor que cero**:
    - Al añadir un producto, el campo `precio` debe ser mayor que cero.
7. **Stock inicial no puede ser negativo**:
    - Al añadir un producto, el campo `stock` no puede ser negativo.
8. **Nuevo stock no puede ser negativo**:
    - Al actualizar el stock de un producto, el nuevo valor no puede ser negativo.

### Gestión de Ventas
9. **Cantidad vendida debe ser mayor que cero**:
    - Al registrar una venta, la cantidad vendida debe ser mayor que cero.
10. **Verificar que el producto existe y tiene suficiente stock**:
    - Al registrar una venta, se debe verificar que el producto existe y tiene suficiente stock.
11. **Empleado debe existir**:
    - Al registrar una venta, se debe verificar que el `empleadoId` exista en la colección `empleados`.
12. **Usuario debe existir**:
    - Al registrar una venta, se debe verificar que el `usuarioId` exista en la colección `usuarios`.
