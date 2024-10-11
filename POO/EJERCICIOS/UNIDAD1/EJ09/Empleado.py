class Empleado:
    def __init__(self,identificador,nombre,departamento,salario):
        self.identificador = identificador
        self.nombre = nombre
        self.departemento = departamento
        self._salario = salario

    def obtener_salario(self):
        return self._salario
    
    def modificar_salario(self,cantidad):
        self._salario = self._salario + cantidad

    def __eq__(self, otro):
        return self._salario == otro._salario