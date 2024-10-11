# Calcular la media de todos los precios de los productos
from Producto import Producto

productos = [Producto("tomate", "fruta", 2.3, 100),
Producto("patata", "verdura", 1.5, 200),
Producto("cebolla", "verdura", 1.8, 150),
Producto("manzana", "fruta", 3.2, 50),
Producto("pera", "fruta", 2.7, 75)]

media = 0

for producto in productos:
        media = media + producto.precio
media= media / len(productos)
print(f"La media del precio de todos los productos es {media}")