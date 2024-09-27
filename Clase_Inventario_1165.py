print("Examen v2 1165")
print("Angel Tadeo De Leon Ceniceros Matricula: 22308051281165")
# Zona de clases
class Inventario1165:
    # Zona de funciones
    # Diccionario CantidadActual
    def Diccionario_Nombre_Cantidad1165(self):
        CantidadActual={
            "Nombre: Huevos":"Cantidad: 30 kg",
            "Nombre: Betun":"Cantidad: 10",
            "Nombre: Moldes":"Cantidad: 10",
            "Nombre: Platos":"Cantidad: 55",
            "Nombre: Harina":"Cantidad: 15 kg",
            "Nombre: Leche":"Cantidad: 40 l",
            "Nombre: Ext.Vanilla":"Cantidad: 10"
        }
        for x,y in CantidadActual.items():
            print(x,y)
    # Diccionario InventarioID
    def Diccionario_ID_Nombre1165(self):
        InventarioID={
            "ID: 1":"Nombre: Cupcake Fresa",
            "ID: 2":"Nombre: Cupcake Vanilla",
            "ID: 3":"Nombre: Cupcake Chocolate",
            "ID: 4":"Nombre: CheeseCake",
            "ID: 5":"Nombre: Tarta de Manzana",
            "ID: 6":"Nombre: Pastel de Zanahoria",
            "ID: 7":"Nombre: Pastel de 3 Leches"
        }
        for x,y in InventarioID.items():
            print(x,y)
    # Diccionario Ubicaciones
    def Diccionario_Almacen_Ubicacion1165(self):
        Ubicacion={
            "Almacen A":"Calle Piña",
            "Almacen B":"Avenida Raton",
            "Almacen C":"Avenida Catabum",
            "Almacen D":"Calle Torres",
            "Almacen E":"Calle Epicon",
            "Almacen F":"Avenida Casahouse",
            "Almacen G":"Avenida Fresa"
        }
        for x,y in Ubicacion.items():
            print(x,y)
    # Diccionario Notas
    def Diccionario_Nombre_Notas1165(self):
        Notas={
            "Nombre: Cupcake Fresa":"Nota: Buena recepcion",
            "Nombre: Cupcake Vanilla":"Nota: Le falta sabor",
            "Nombre: Cupcake Chocolate":"Nota: Buena recepcion",
            "Nombre: CheeseCake":"Nota: Muy buena recepcion",
            "Nombre: Tarta de Manzana":"Nota: Falta de compras",
            "Nombre: Pastel de Zanahoria":"Nota: Falta de compras",
            "Nombre: Pastel de 3 Leches":"Nota: Muy buena recepcion"
        }
        for x,y in Notas.items():
            print(x,y)
# Zona de creacion del objeto
ObjetoInventario=Inventario1165()
# Zona de uso de objetos
print("Diccionario de IDs:")
ObjetoInventario.Diccionario_ID_Nombre1165()
print("Diccionario de Cantidades Actuales:")
ObjetoInventario.Diccionario_Nombre_Cantidad1165()
print("Diccionario de Ubicaciones:")
ObjetoInventario.Diccionario_Almacen_Ubicacion1165()
print("Diccionario de Notas:")
ObjetoInventario.Diccionario_Nombre_Notas1165()