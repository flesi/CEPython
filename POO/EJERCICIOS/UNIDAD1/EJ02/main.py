# En este ejercicio utilizaremos la misma clase que en el ejercicio anterior y
# añadiremos un método llamado “nombre_completo” que retorne en una cadena los
# atributos marca y modelo concatenados y separados por un guión (Seat-Ibiza).
# Crear dos objetos y probar el método.
from Vehiculo import Vehiculo

v1 = Vehiculo("Ford","Focus",2010,5000)
v2 = Vehiculo("Reanault","Megane",2016,7000)

print(v1.nombre_completo())
print(v2.nombre_completo())