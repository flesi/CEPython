# Diseñar una clase Python llamada “Producto” con los atributos nombre, categoría,
# precio y cantidad. Diseña en esta clase el método __str__ de forma que retorne
# todos los atributos en un dato de tipo cadena (str).
# Crear dos productos pertenecientes a esa clase y mostrar todos los datos de aquel
# producto que tenga mayor precio.
from Producto import Producto


p1 = Producto("Patatas","Aperitivos",2,10)
p2 = Producto("Aceitunas","Aperitivos",3,10)


if p1.precio > p2.precio:
    print(p1)
else:
    print(p2)