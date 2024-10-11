# Contar cuántos productos tienen un precio entre 2 y 3 (excluidos).
from Producto import Producto

productos = [Producto("tomate", "fruta", 2.3, 100),
Producto("patata", "verdura", 1.5, 200),
Producto("cebolla", "verdura", 1.8, 150),
Producto("manzana", "fruta", 3.2, 50),
Producto("pera", "fruta", 2.7, 75)]

cantidad = 0
for producto in productos:
    if producto.precio < 2 and producto.precio > 3:
        cantidad+=1

print(f"La cantidad de productos entre 2 y 3 {cantidad}")