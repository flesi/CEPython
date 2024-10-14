class Empleado:
    def __init__(self,identificador,nombre,departamento,salario):
        self.identificador = identificador
        self.nombre = nombre
        self.departemento = departamento
        self._salario = salario

    def __str__(self):
        return (f"Identificador: {self.identificador} | "
                f"Nombre: {self.nombre} | "
                f"Departamento: {self.departemento} | "
                f"Salario: {self._salario} | ")