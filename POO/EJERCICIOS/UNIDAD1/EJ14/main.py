from clases import *

# contacto_buscado = Agenda.buscarPorNombre("Ana")
# # print(contacto_buscado)

telefono = Agenda.getTelefono("Ana")
print(telefono)

Agenda.setTelefono("Ana","111111")
telefono = Agenda.getTelefono("Ana")
print(telefono)

# Agenda.listarContactos()
# print(Agenda.getNumContactos())