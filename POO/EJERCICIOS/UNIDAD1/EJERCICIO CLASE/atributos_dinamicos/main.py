from clases import Empleado

e1 = Empleado("Ana",1500)
e2 = Empleado("Carlos",1500)

print(hasattr(e1, "salario"))

print(getattr(e1, "salario"))
print(e1._salario)


delattr(e1,"salario")

print(hasattr(e1, "salario"))