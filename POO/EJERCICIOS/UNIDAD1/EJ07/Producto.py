class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        print(f"""
                Nombre: {self.nombre} 
                Categoria: {self.categoria} 
                Precio:  {self.precio}
                Cantidad: {self.cantidad}
            """)
        
    def actualizar_cantidad(self, cantidad):
        self.cantidad = self.cantidad + cantidad
