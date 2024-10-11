# Diseñar la clase “Empleado” con los atributos identificador, nombre, departamento,
# salario. Tener en cuenta que el salario será privado. Define un método para
# obtenerlo y otro para modificarlo.
# Programa el método __eq__(), de forma que indique si dos empleados son iguales o
# no en función de su salario.
# Crear varios empleados, mostrar sus datos y comparar si son iguales o no.


from Empleado import Empleado


e1 = Empleado("01","Pepe","DEV",1000)
e2 = Empleado("02","Jose","DEV",1000)
e3 = Empleado("03","Luis","DEV",2000)

print(e1)
print(e2)
print(e1==e2)

print(e1)
print(e3)
print(e1==e3)