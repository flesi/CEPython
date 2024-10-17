class Contacto:
    def __init__(self,nombre,telefono,correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"Nombre: {self.nombre} - Telefono: {self.telefono} - Correo: {self.correo}"

    def __repr__(self):
        return f"Contacto({self.nombre}, {self.telefono}, {self.correo})"

    def __eq__(self, contacto):
        return self.correo == contacto.correo

class Agenda:
    listaContactos = [
        Contacto("Ana"  , "44444444", "ana@gmail.com"),
        Contacto("Luis" , "5555555" , "luis@gmail.com"),
        Contacto("Eva"  , "6666666" , "eva@gmail.com"),
        Contacto("Fran" , "7777777" , "fran@gmail.com"),
        Contacto("Elena", "8988888" , "elena@gmail.com")
    ]

    @classmethod
    def buscarPorNombre(cls,nombre_buscado):
        for contacto in cls.listaContactos:
            if contacto.nombre.lower() == nombre_buscado.lower():
                return contacto
        return None
    
    @classmethod
    def getCorreo(cls,nombre_buscado):
        contacto = cls.buscarPorNombre(nombre_buscado)
        if contacto:
            return contacto.correo
        else:
            return None

    @classmethod
    def getTelefono(cls, nombre_buscado):
        contacto = cls.buscarPorNombre(nombre_buscado)
        if contacto:
            return contacto.telefono
        else:
            return None

    @classmethod
    def setTelefono(cls,nombre_buscado,nuevo_telefono):
        contacto = cls.buscarPorNombre(nombre_buscado)
        if contacto:
            contacto.telefono = nuevo_telefono
            return True
        else:
            return False

    @classmethod
    def setCorreo(cls, nombre_buscado, nuevo_correo):
        contacto = cls.buscarPorNombre(nombre_buscado)
        if contacto:
            contacto.correo = nuevo_correo
            return True
        else:
            return False

    @classmethod
    def listarContactos(cls):
        for contacto in cls.listaContactos:
            print(contacto)

    @classmethod
    def getNumContactos(cls):
        return len(cls.listaContactos)