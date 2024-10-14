class Producto:

    def __init__(self,id,nombre,categoria,precio,stock):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock


    def __str__(self):
        return (f"ID: {self.id} | "
                f"Nombre: {self.nombre} | "
                f"Categoria: {self.categoria} | "
                f"Precio: {self.precio} | "
                f"Stock: {self.stock}"
                )
        
class Carrito:

    def __init__(self):
        self.productos = {}


    def mostrar_productos(self):
        if len(self.productos) == 0:
            print("El carrito esta vacio")
        else:
            for producto in self.productos:
                print(producto)
            
            
                
    def agregar_productos(self, producto, cantidad):
        if cantidad >= producto.stock:
            print(f"No hay suficiente Stock de {producto.nombre}")
            return
        pass
        
    def eliminar_producto(self, producto):
        if producto in self.productos:
            pass

    def actualizar_unidades(self):
        pass

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio * producto.catidad
        return total