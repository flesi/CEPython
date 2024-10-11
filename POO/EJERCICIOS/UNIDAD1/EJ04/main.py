# Modificar la clase “Producto” del ejercicio anterior añadiendo un método que
# actualice la cantidad de un producto sumándole un valor pasado como parámetro.
# Mostrar los datos de un producto antes y después de ser modificada su cantidad.
from Producto import Producto

p1 = Producto("Patatas","Aperitivos",2,10)

print(p1)

p1.actualizar_cantidad(10)

print(p1)