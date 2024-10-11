class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return (f"Nombre: {self.nombre} | " 
                f"Categoria: {self.categoria} | " 
                f"Precio:  {self.precio} | "
                f"Cantidad: {self.cantidad}")
        
    def actualizar_cantidad(self, cantidad):
        self.cantidad = self.cantidad + cantidad