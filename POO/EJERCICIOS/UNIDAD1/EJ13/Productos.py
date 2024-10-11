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