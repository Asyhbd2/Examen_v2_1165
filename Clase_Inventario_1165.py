print("Examen v2 1165")
print("Angel Tadeo De Leon Ceniceros Matricula: 22308051281165")
# Zona de clases
class Inventario1165:
    # Zona de funciones
    # Diccionario CantidadActual
    def Diccionario_Clientes1165(self):
        Clientes={
            "Cliente ID:":1423,
            "Nombre:":"Carlos",
            "Correo:":"hola@gmail.com",
            "Telefono:":"656 231 2314",
            "Direccion:":"Calle piña",
            "FechaRegistro:":"10/2/24",
            "Preferencias:":"Cheescake"
        }
        for x,y in Clientes.items():
            print(x,y)
    # Diccionario Productos
    def Diccionario_Productos1165(self):
        Productos={
            "Producto ID:":23,
            "Nombre:":"Cupcake Vanilla",
            "Descripcion":"Cupcake sabor Vanilla",
            "Precio":30,
            "Categoria":"Cupcakes",
            "Stock":50,
            "FechaIngreso":"23/4/23"
        }
        for x,y in Productos.items():
            print(x,y)
   # Diccionario Proveedores
    def Diccionario_Proveedores1165(self):
        Proveedor={
            "Proveedor ID:":123,
            "Nombre:":"Carlos",
            "Correo:":"hola@gmail.com",
            "Telefono:":"656 231 2314",
            "Direccion:":"Calle piña",
            "FechaRegistro:":"10/2/24",
            "Producto Suministro:":"Cajas"
        }
        for x,y in Proveedor.items():
            print(x,y)
    # Diccionario Notas

    def Diccionario_Inventario1165(self):
        Inventario={
            "Inventario ID:":3,
            "Producto ID:":42,
            "Cantidad Inicial:":50,
            "Cantidad Actual:":23,
            "Fecha Actualizacion:":"3/3/20",
            "Ubicacion:":"Calle Torres",
            "Notas:":"Todo en buen estado"
        }
        for x,y in Inventario.items():
            print(x,y)
# Zona de creacion del objeto
ObjetoInventario=Inventario1165()
# Zona de uso de objetos
print("Diccionario de Clientes:")
ObjetoInventario.Diccionario_Clientes1165()
print("Diccionario de Productos:")
ObjetoInventario.Diccionario_Productos1165()
print("Diccionario de Inventario:")
ObjetoInventario.Diccionario_Inventario1165()
print("Diccionario de Proveedores:")
ObjetoInventario.Diccionario_Proveedores1165()
