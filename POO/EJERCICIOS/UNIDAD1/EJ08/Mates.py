class Mates:
    @staticmethod
    def mayor(n1,n2):
        if n1 > n2:
            return n1
        else:
            return n2
        
    @staticmethod
    def producto(n1,n2,n3):
        return n1 * n2 * n3

    @staticmethod
    def potencia(base,exponente):
        resultado = 1
        for i in range(exponente):
            resultado = resultado * base
        return resultado