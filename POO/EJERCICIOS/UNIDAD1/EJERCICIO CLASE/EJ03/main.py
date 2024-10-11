# clase producto
# atributo: nombre, categoria, precio, proveedor
# categorias: fruta, verdura, refresco, carne, pescado
# metodos: constructor, es_refresco(true o false)
from Producto import Producto
p1 = Producto("Coca-Cola","refresco",2,"Coca-Cola")
p2 = Producto("Manzana","fruta",1,"Frutas David")

print(p1.es_refresco())
print(p2.es_refresco())

