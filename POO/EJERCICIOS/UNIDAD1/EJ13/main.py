# Diseñar una aplicación Python que simule el funcionamiento de un carrito de la compra. Para ello debes tener en cuenta que al carrito se añadirán una o varias unidades de una serie de productos. 
# Necesitas crear un listado de productos disponibles. De cada producto se guarda un id, nombre, categoría, precio y stock.
# El carrito debe permitir:
# mostrar lista de productos.
# añadir nuevos productos.
# eliminar un producto.
# actualizar las unidades de un producto.
# calcular el importe total.

from Clases import Producto,Carrito

producto1 = Producto(1, "Manzana", "Frutas", 0.5, 100)
producto2 = Producto(2, "Pan", "Alimentos", 1.0, 50)
producto3 = Producto(3, "Leche", "Lácteos", 0.8, 30)

carrito = Carrito()

carrito.agregar_productos(producto1, 2)

carrito.mostrar_productos()
