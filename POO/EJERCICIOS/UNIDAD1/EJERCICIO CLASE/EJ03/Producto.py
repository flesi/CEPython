class Producto:
    def __init__(self,nombre,categoria,precio,proveedor):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.proveedor = proveedor
    
    def es_refresco(self):
        if self.categoria == "refresco":
            return True
        else:
            return False